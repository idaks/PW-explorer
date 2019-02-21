#!/usr/bin/env python3

import pandas as pd
import numpy as np
import os
import sqlite3
import copy
from .pwe_helper import mkdir_p


def get_sqlite_schema(dfs):

    # this approach will take constant time since there is just one row in the exported database.
    TEST_DB_LOCATION = os.path.abspath("test.db")
    conn_t = sqlite3.connect(TEST_DB_LOCATION)
    for rl_name, df in dfs.items():
        t = df.ix[0:0]
        t.to_sql(str(rl_name), conn_t, if_exists='replace')
    schema_q = conn_t.execute("SELECT * FROM sqlite_master WHERE type='table' ORDER BY name;")
    schemas = []
    for row in schema_q.fetchall():
        schemas.append(row[4])
    for rl_name, df in dfs.items():
        conn_t.execute('DROP TABLE ' + str(rl_name))
    conn_t.commit()
    conn_t.close()
    os.remove(TEST_DB_LOCATION)
    return schemas


def export_to_sqlite_db(export_loc, dfs, db_name):

    mkdir_p(export_loc)
    sql_db_loc = os.path.join(export_loc, '{}.{}'.format(str(db_name), 'db'))
    sql_conn = sqlite3.connect(sql_db_loc)

    for rl_name, df in dfs.items():
        df.to_sql(rl_name, sql_conn, if_exists='replace')

    sql_conn.commit()
    sql_conn.close()

    return True


def export_as_asp(pws, simple_or_triples='simple', rel_facts_with_arity: bool=True, include_pw_ids: bool=True,
                  attr_defs: dict=None, pw_ids_to_output: list=None, rels_to_output: list=None,
                  pw_ids_remapper: dict=None):
    """
    Export the PWs as asp facts for further use.
    :param pws: List of PossibleWorld objects
    :param simple_or_triples: 'simple' or 'triples'. Defaults to 'simple' i.e. of the form rel_name(pw_id, attrs....)
    (pw_id only included if include_pw_ids is True). Triples is of the form triple(fact_id, type, value).
    :param rel_facts_with_arity: Retain original relation names i.e. that include arity information in the
    name eg. 'node_2'. If False, then 'node' would be use. Default: True
    :param include_pw_ids: Whether to include a pw_id field. Default: True. Might want to set as False if only
    outputting one PW or similar cases.
    :param attr_defs: if 'simple' export type, then statements of the form
    '% define rel_name(pw_id, attr1_name, attr2_name...)' will be included to aid future reparsing
    (pw_id only included if include_pw_ids is True).
    :param pw_ids_to_output: list of pw_ids (before remapping if asked for) of pws to output facts of.
    Default: None i.e. all pws are output
    :param rels_to_output: list of relations to output. Default: None i.e. all relation types are output.
    Must be of the form 'relName_arity' i.e. matching those in the pw.rls
    :param pw_ids_remapper: to remap the pw_id of the pws. Those not in the dictionary are not remapped,
    so make sure that if you say remap 1 to 2, 2 to 4, then you must remap 4 to something else unless you want
    the two to be combined,
    Default behavior is to preserve the original pw_ids.
    :return: list of asp facts in the requested type (simple or triples)
    """
    if pw_ids_to_output:
        pws = list(filter(lambda pw: pw.pw_id in pw_ids_to_output, pws))
    if rels_to_output or pw_ids_remapper:
        pws = copy.deepcopy(pws)
    # Now we can manipulate these freely
    if rels_to_output:
        for pw in pws:
            unwanted_rel_names = set(pw.rls.keys()) - set(rels_to_output)
            for unwanted_key in unwanted_rel_names: del pw.rls[unwanted_key]
    if pw_ids_remapper:
        for pw in pws:
            if pw.pw_id in pw_ids_remapper:
                pw.pw_id = pw_ids_remapper[pw.pw_id]

    if simple_or_triples == 'simple':
        return export_as_asp_facts(pws, rel_facts_with_arity=rel_facts_with_arity, include_pw_ids=include_pw_ids,
                                   attr_defs=attr_defs)
    elif simple_or_triples == 'triples':
        return export_as_asp_triples(pws, rel_facts_with_arity=rel_facts_with_arity, include_pw_ids=include_pw_ids)
    else:
        print("Export type not recognized. Must be one of 'simple' or 'triples'" )
        return None


def export_as_asp_facts(pws, rel_facts_with_arity: bool=True, attr_defs: dict=None, include_pw_ids: bool=True):

    # output the pws as rel_name(pw_id, attrs....) and optimization(pw_id, optimized_value)
    pw_rel_facts = []
    for pw in pws:
        if pw.pw_soln is not None:
            if include_pw_ids:
                pw_rel_facts.append('optimization({}, {}).'.format(pw.pw_id, pw.pw_soln))
            else:
                pw_rel_facts.append('optimization({}).'.format(pw.pw_soln))
        for rl_name, rl_facts in pw.rls.items():
            if not rel_facts_with_arity:
                rl_name = rl_name.rsplit('_', maxsplit=1)[0]
            for rl_fact in rl_facts:
                temp = []
                if include_pw_ids:
                    temp.append(pw.pw_id)
                temp.extend(rl_fact)
                temp = [str(t) for t in temp]
                pw_rel_facts.append('{}{}.'.format(rl_name,
                                                   '({})'.format(','.join(temp)) if len(temp) > 0 else ''))

    # add attr_def rules if they are provided
    attr_def_rules = []
    if attr_defs is None:
        attr_defs = {}
    for rel_name, attrs in attr_defs.items():
        if not rel_facts_with_arity:
            rel_name = rel_name.rsplit('_', maxsplit=1)[0]
        if include_pw_ids:
            attrs = ['PW_ID'] + attrs
        attr_def_rules.append('% define {}({})'.format(rel_name, ','.join(attrs)))

    return attr_def_rules + pw_rel_facts


def export_as_asp_triples(pws, rel_facts_with_arity: bool=True, include_pw_ids: bool=True):

    TRIPLES_FACT_NAME = 'triple'
    TRIPLES_RELATION_NAME_KEYWORD = 'rel'
    TRIPLE_PW_ID_KEYWORD = 'pw'

    def create_triple(arg1, arg2, arg3):
        return '{}({},{},{}).'.format(TRIPLES_FACT_NAME, arg1, arg2, arg3)

    facts_counter = 0
    facts = []


    for pw in pws:
        for rl_name, rl_facts in pw.rls.items():
            if not rel_facts_with_arity:
                rl_name = rl_name.rsplit('_', maxsplit=1)[0]
            for rl_fact in rl_facts:
                facts_counter += 1
                fact_id = facts_counter
                facts.append(create_triple(fact_id, TRIPLES_RELATION_NAME_KEYWORD, rl_name))
                if include_pw_ids:
                    facts.append(create_triple(fact_id, TRIPLE_PW_ID_KEYWORD, pw.pw_id))
                for i, rl_fact_attr in enumerate(rl_fact):
                    facts.append(create_triple(fact_id, i+1, rl_fact_attr))

    return facts


def export(export_format, export_loc, dfs):

    if export_format not in ['csv', 'h5', 'msg', 'pkl']:
        return False

    mkdir_p(export_loc)

    for rl_name, df in dfs.items():
        fname = os.path.join(export_loc, '{}.{}'.format(rl_name, export_format))
        if export_format == 'csv':
            df.to_csv(fname)
        elif export_format == 'h5':
            df.to_hdf(fname, mode='w', key='df')
        elif export_format == 'msg':
            df.to_msgpack(fname)
        elif export_format == 'pkl':
            df.to_pickle(fname)

    return True
