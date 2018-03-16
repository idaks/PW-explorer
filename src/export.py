# EXPORT AND SCHEMA GENERATION SCRIPT:

import pandas as pd
import numpy as np
import sqlite3
import argparse
from .helper import get_current_project_name, set_current_project_name, \
    get_file_save_name, get_save_folder, load_from_temp_pickle


def __main__():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--project_name", type=str, help="provide session/project name used while parsing")
    parser.add_argument("-s", "--schema", action="store_true", help="generate sql schemas", default=False)
    parser.add_argument("-sql", action="store_true", help="include if you want to export a sql db", default=False)
    parser.add_argument("-csv", action="store_true", help="include if you want to export in csv", default=False)
    parser.add_argument("-h5", action="store_true", help="include if you want to export in hdf5 format", default=False)
    parser.add_argument("-msg", action="store_true", help="include if you want to export in msgpack format", default=False)
    parser.add_argument("-pkl", action="store_true", help="include if you want to export in pickle format", default=False)
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
    conn = None

    if export_to_sql:
        conn = sqlite3.connect(get_save_folder(project_name, 'exports') + get_file_save_name(project_name, 'sql'))

    for i, df in enumerate(dfs):
        if export_to_csv:
            df.to_csv(get_save_folder(project_name, 'csv_export') + str(relations[i].relation_name) + '.csv')
        if export_to_hdf:
            df.to_hdf(get_save_folder(project_name, 'h5_export') + str(relations[i].relation_name) + '.h5',
                      str(relations[i].relation_name), mode='w')
        if export_to_sql:
            df.to_sql(str(relations[i].relation_name), conn, if_exists='replace')
        if export_to_msg:
            df.to_msgpack(
                get_save_folder(project_name, 'msg_export') + str(relations[i].relation_name) + '.msg')
        if export_to_pkl:
            df.to_pickle(get_save_folder(project_name, 'pkl_export') + str(relations[i].relation_name) + '.pkl')

    if export_to_csv:
        print("Successfully exported to csv")
    if export_to_sql:
        print("Successfully exported to sql")
    if export_to_msg:
        print("Successfully exported to msg")
    if export_to_hdf:
        print("Successfully exported to hdf")
    if export_to_pkl:
        print("Successfully exported to pkl")

    # creating schemas for SQLite
    # code to print schema of the tables created
    if args.schema:
        schemas = []
        if export_to_sql:
            schema_q = conn.execute("SELECT * FROM sqlite_master WHERE type='table' ORDER BY name;")
            print('Sqlite Schema:')
            for row in schema_q.fetchall():
                print(str(row[4]))
                schemas.append(row[4])
        else:
            conn_t = sqlite3.connect("test.db")
            for i, df in enumerate(dfs):
                t = df.ix[0:0]
                t.to_sql(str(relations[i].relation_name), conn_t, if_exists='replace')
            schema_q = conn_t.execute("SELECT * FROM sqlite_master WHERE type='table' ORDER BY name;")
            print('Sqlite Schema:')
            for row in schema_q.fetchall():
                print(str(row[4]))
                schemas.append(row[4])
            for i, df in enumerate(dfs):
                conn_t.execute('DROP TABLE ' + str(relations[i].relation_name))
            conn_t.commit()
            conn_t.close()
    # this approach will take constant time since there is just one row in the exported database.

    if export_to_sql:
        conn.commit()
        conn.close()

    set_current_project_name(project_name)


if __name__ == '__main__':
    __main__()