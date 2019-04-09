#!/usr/bin/env python3

import pandas as pd
import os
import sqlite3
from .helper import mkdir_p
from .Input_Parsers.Meta_Data_Parser.meta_data_parser import (
    ASP_COMMENT_SYMBOL,
    ASP_SYNTAX_ATTRIBUTE_DEF_KEYWORD,
)


class PWEExport:

    @staticmethod
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

    @staticmethod
    def export_to_sqlite_db(export_loc, dfs, db_name):

        mkdir_p(export_loc)
        sql_db_loc = os.path.join(export_loc, '{}.{}'.format(str(db_name), 'db'))
        sql_conn = sqlite3.connect(sql_db_loc)

        for rl_name, df in dfs.items():
            df.to_sql(rl_name, sql_conn, if_exists='replace')

        sql_conn.commit()
        sql_conn.close()

        return True

    @staticmethod
    def export_as_asp_facts(pws, rel_facts_with_arity: bool=False, attr_defs: dict=None, include_pw_ids: bool=True):
        """
        :param pws: List of PossibleWorld objects
        :param rel_facts_with_arity: Include Arity in the Relation Names
        :param attr_defs: if provided, then statements of the form
        '% schema rel_name(pw_id, attr1_name, attr2_name...)' will be included to aid future reparsing
        (pw_id only included if include_pw_ids is True).
        :param include_pw_ids: Include PW-ID information
        :return: list of asp facts as strings
        """
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
            attr_def_rules.append('{} {} {}({})'.format(ASP_COMMENT_SYMBOL, ASP_SYNTAX_ATTRIBUTE_DEF_KEYWORD,
                                                        rel_name, ','.join(attrs)))

        return attr_def_rules + pw_rel_facts

    @staticmethod
    def export_wfs_model_as_asp_facts(dfs, rel_facts_with_arity: bool = False, attr_defs: dict = None):
        """
        For use with Well-Founded Semantics Model
        :param dfs: Dictionary of Dataframes for each relation, keyed by relation name
        :param rel_facts_with_arity: Include Arity in the Relation Names
        :param attr_defs: if provided, then statements of the form
        '% schema rel_name(pw_id, attr1_name, attr2_name...)' will be included to aid future reparsing
        (pw_id only included if include_pw_ids is True).
        :return: list of asp facts as strings
        """
        # output the pws as rel_name(wfs_value, attrs....)
        pw_rel_facts = []

        for rl_name, df in dfs.items():
            if not rel_facts_with_arity:
                rl_name = rl_name.rsplit('_', maxsplit=1)[0]
            wfs_status_keyword = list(df.columns)[0]
            cols = list(df.columns)[1:]
            for idx, row in df.iterrows():
                temp = [row[wfs_status_keyword]]
                for j, col in enumerate(cols):
                    temp.append(row[col])
                pw_rel_facts.append('{}({}).'.format(rl_name, ','.join(temp)))

        # add attr_def rules if they are provided
        attr_def_rules = []
        if attr_defs is None:
            attr_defs = {}
        for rel_name, attrs in attr_defs.items():
            if not rel_facts_with_arity:
                rel_name = rel_name.rsplit('_', maxsplit=1)[0]
            attrs = ['WFS_VALUE'] + attrs
            attr_def_rules.append('{} {} {}({})'.format(ASP_COMMENT_SYMBOL, ASP_SYNTAX_ATTRIBUTE_DEF_KEYWORD,
                                                        rel_name, ','.join(attrs)))

        return attr_def_rules + pw_rel_facts

    ASP_TRIPLES_ATTR_NAMES = ['FACT_ID', 'SUBJECT', 'VALUE']

    @staticmethod
    def export_as_asp_triples(pws, rel_facts_with_arity: bool = False, include_pw_ids: bool = True, output_type='list'):
        """
        :param pws: List of PossibleWorld Objects
        :param rel_facts_with_arity: Include Arity in the Relation Names
        :param include_pw_ids: Include PW-ID information
        :param output_type: 'str': As a list of strings that can be output into a file,
                            'db': As a Pandas Dataframe,
                            'list': As a list of tuples (well triples) (Default).
                            NOTE: Defaults to 'list' even if some unrecognizable argument is passed in.
        :return: Depending on output_type
        """

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
                    facts.append((fact_id, TRIPLES_RELATION_NAME_KEYWORD, rl_name))
                    if include_pw_ids:
                        facts.append((fact_id, TRIPLE_PW_ID_KEYWORD, pw.pw_id))
                    for i, rl_fact_attr in enumerate(rl_fact):
                        facts.append((fact_id, i+1, rl_fact_attr))

        if output_type == 'str':
            facts = [create_triple(fact[0], fact[1] ,fact[2]) for fact in facts]
            facts.insert(0, '{} {} {}'.format(ASP_COMMENT_SYMBOL, ASP_SYNTAX_ATTRIBUTE_DEF_KEYWORD,
                                              create_triple(*PWEExport.ASP_TRIPLES_ATTR_NAMES)))
        elif output_type == 'db':
            facts = pd.DataFrame(data=facts, columns=PWEExport.ASP_TRIPLES_ATTR_NAMES)

        return facts

    @staticmethod
    def export_wfs_model_as_asp_triples(dfs, attr_name_or_idx: str='idx', rel_facts_with_arity: bool = False,
                                        output_type='list'):
        """
        For use with well-founded semantics model.
        :param dfs: Dictionary of Dataframes for each relation, keyed by relation name
        :param attr_name_or_idx: options: 'attr_name', 'idx' (Default).
                                 'attr_name' produces triples like triple(17, NODE_ID, 1) or triple(17, x1, 1).
                                 'idx' produces triples like triple(17, 1, 1). triple(17, 2, red).
        :param rel_facts_with_arity: Include Arity in the Relation Names
        :param output_type: 'str': As a list of strings that can be output into a file,
                            'db': As a Pandas Dataframe,
                            'list': As a list of tuples (well triples) (Default).
                            NOTE: Defaults to 'list' even if some unrecognizable argument is passed in.
        :return: Depending on output_type
        """

        TRIPLES_FACT_NAME = 'triple'
        TRIPLES_RELATION_NAME_KEYWORD = 'rel'
        TRIPLE_WFS_VALUE_KEYWORD = 'wfs_value'

        def create_triple(arg1, arg2, arg3):
            return '{}({},{},{}).'.format(TRIPLES_FACT_NAME, arg1, arg2, arg3)

        facts_counter = 0
        facts = []

        for rl_name, df in dfs.items():
            if not rel_facts_with_arity:
                rl_name = rl_name.rsplit('_', maxsplit=1)[0]
            wfs_status_keyword = list(df.columns)[0]
            cols = list(df.columns)[1:]
            for i, row in df.iterrows():
                facts_counter += 1
                fact_id = facts_counter
                facts.append((fact_id, TRIPLES_RELATION_NAME_KEYWORD, rl_name))
                facts.append((fact_id, TRIPLE_WFS_VALUE_KEYWORD, row[wfs_status_keyword]))
                for j, col in enumerate(cols):
                    if attr_name_or_idx == 'attr_name':
                        facts.append((fact_id, col, row[col]))
                    elif attr_name_or_idx == 'idx':
                        facts.append((fact_id, j+1, row[col]))

        if output_type == 'str':
            facts = [create_triple(fact[0], fact[1], fact[2]) for fact in facts]
            facts.insert(0, '{} {} {}'.format(ASP_COMMENT_SYMBOL, ASP_SYNTAX_ATTRIBUTE_DEF_KEYWORD,
                                              create_triple(*PWEExport.ASP_TRIPLES_ATTR_NAMES)))
        elif output_type == 'db':
            facts = pd.DataFrame(data=facts, columns=PWEExport.ASP_TRIPLES_ATTR_NAMES)

        return facts

    @staticmethod
    def export(export_format, export_loc, dfs):

        if export_format not in ['csv', 'pkl']:
            return False

        mkdir_p(export_loc)

        for rl_name, df in dfs.items():
            fname = os.path.join(export_loc, '{}.{}'.format(rl_name, export_format))
            if export_format == 'csv':
                df.to_csv(fname)
            elif export_format == 'pkl':
                df.to_pickle(fname)

        return True
