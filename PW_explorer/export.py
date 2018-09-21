#!/usr/bin/env python3
# EXPORT AND SCHEMA GENERATION SCRIPT:

import pandas as pd
import numpy as np
import os
import sqlite3
import argparse
from pwe_helper import get_current_project_name, set_current_project_name, \
    get_save_folder, load_from_temp_pickle, mkdir_p


def get_sqlite_schema(dfs, relations):

    # this approach will take constant time since there is just one row in the exported database.
    TEST_DB_LOCATION = os.path.abspath("test.db")
    conn_t = sqlite3.connect(TEST_DB_LOCATION)
    for i, df in enumerate(dfs):
        t = df.ix[0:0]
        t.to_sql(str(relations[i].relation_name), conn_t, if_exists='replace')
    schema_q = conn_t.execute("SELECT * FROM sqlite_master WHERE type='table' ORDER BY name;")
    schemas = []
    for row in schema_q.fetchall():
        schemas.append(row[4])
    for i, df in enumerate(dfs):
        conn_t.execute('DROP TABLE ' + str(relations[i].relation_name))
    conn_t.commit()
    conn_t.close()
    os.remove(TEST_DB_LOCATION)
    return schemas


def export_to_sqlite_db(export_loc, dfs, relations, db_name):

    mkdir_p(export_loc)
    sql_db_loc = os.path.join(export_loc, '{}.{}'.format(str(db_name), 'db'))
    sql_conn = sqlite3.connect(sql_db_loc)

    for i, df in enumerate(dfs):
        rel_name = str(relations[i].relation_name)
        df.to_sql(rel_name, sql_conn, if_exists='replace')

    sql_conn.commit()
    sql_conn.close()

    return True


def export(export_format, export_loc, dfs, relations):

    if export_format not in ['csv', 'h5', 'msg', 'pkl']:
        return False

    mkdir_p(export_loc)

    for i, df in enumerate(dfs):
        rel_name = str(relations[i].relation_name)
        fname = os.path.join(export_loc, '{}.{}'.format(rel_name, export_format))
        if export_format == 'csv':
            df.to_csv(fname)
        elif export_format == 'h5':
            df.to_hdf(fname, mode='w', key='df')
        elif export_format == 'msg':
            df.to_msgpack(fname)
        elif export_format == 'pkl':
            df.to_pickle(fname)

    return True


def __main__():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--project_name", type=str, help="provide session/project name used while parsing")
    parser.add_argument("-s", "--schema", action="store_true", help="generate sql schemas", default=False)
    parser.add_argument("-sql", action="store_true", help="include if you want to export a sql db", default=False)
    parser.add_argument("-csv", action="store_true", help="include if you want to export in csv", default=False)
    parser.add_argument("-h5", action="store_true", help="include if you want to export in hdf5 format", default=False)
    parser.add_argument("-msg", action="store_true", help="include if you want to export in msgpack format",
                        default=False)
    parser.add_argument("-pkl", action="store_true", help="include if you want to export in pickle format",
                        default=False)
    args = parser.parse_args()

    project_name = ''
    if args.project_name is None:
        project_name = get_current_project_name()
        if project_name is None:
            print("Couldn't find current project. Please provide a project name.")
            exit(1)
    else:
        project_name = args.project_name

    export_to_sql = args.sql
    export_to_csv = args.csv
    export_to_hdf = args.h5
    export_to_msg = args.msg
    export_to_pkl = args.pkl

    dfs = load_from_temp_pickle(project_name, 'dfs')
    relations = load_from_temp_pickle(project_name, 'relations')

    if export_to_sql:
        if export_to_sqlite_db(get_save_folder(project_name, 'sql_export'), dfs, relations, project_name):
            print("Successfully exported to sql")
        else:
            print("SQL Export Failed")
    if export_to_csv:
        if export('csv', get_save_folder(project_name, 'csv_export'), dfs, relations):
            print("Successfully exported to csv")
        else:
            print("CSV Export Failed")
    if export_to_hdf:
        if export('h5', get_save_folder(project_name, 'h5_export'), dfs, relations):
            print("Successfully exported to hdf")
        else:
            print("HDF Export Failed")
    if export_to_msg:
        if export('msg', get_save_folder(project_name, 'msg_export'), dfs, relations):
            print("Successfully exported to msg")
        else:
            print("MSGPACK Export Failed")
    if export_to_pkl:
        if export('pkl', get_save_folder(project_name, 'pkl_export'), dfs, relations):
            print("Successfully exported to pkl")
        else:
            print("PICKLE Export Failed")

    if args.schema:
        schemas = get_sqlite_schema(dfs, relations)
        print('\n'.join(schemas))

    set_current_project_name(project_name)


if __name__ == '__main__':
    __main__()