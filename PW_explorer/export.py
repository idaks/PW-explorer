#!/usr/bin/env python3

import pandas as pd
import numpy as np
import os
import sqlite3
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
