#!/usr/bin/env python3

import pandas as pd
import numpy as np
from .pwe_query import PWEQuery


def sym_diff_dist(pw_id_1, pw_id_2, relations, dfs, pws, rls_to_use: list=None):

    if pw_id_1 == pw_id_2:
        return 0

    if not rls_to_use:
        rls_to_use = [i for i in range(len(relations))]

    dist = 0
    for rl_id in rls_to_use:
        redundant_cols = PWEQuery.redundant_column(relations=relations, expected_pws=len(pws),  dfs=dfs, rl_id=rl_id,
                                                   pws_to_consider=[pw_id_1, pw_id_2], do_print=False)[0]
        cols_to_consider = set(list(dfs[rl_id])[1:])
        for t in redundant_cols:
            if t in cols_to_consider:
                cols_to_consider.remove(t[2])
        cols_to_consider = list(cols_to_consider)

        wt1 = 1  # TBD
        k1 = 1  # TBD

        x1 = PWEQuery.difference_both_ways(relations=relations, dfs=dfs,  rl_id=rl_id, pw_id_1=pw_id_1, pw_id_2=pw_id_2,
                                           col_names=cols_to_consider, do_print=False)
        dist += wt1 * len(x1) ** k1 if x1 is not None else 0

    return dist


def euler_overlap_diff_dist(pw_id_1, pw_id_2, rl_id, col_name, dfs, pws, relations):

    x1 = PWEQuery.freq(relations=relations, expected_pws=len(pws), dfs=dfs, rl_id=rl_id, col_names=[col_name],
                       values=['"><"'], pws_to_consider=[pw_id_1], do_print=False)[1][0]
    x2 = PWEQuery.freq(relations=relations, expected_pws=len(pws), dfs=dfs, rl_id=rl_id, col_names=[col_name],
                       values=['"><"'], pws_to_consider=[pw_id_2], do_print=False)[1][0]
    return abs(x1 - x2)
