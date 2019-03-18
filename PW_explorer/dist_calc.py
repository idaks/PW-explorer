from .query import PWEQuery

class PWEDistanceCalculation:

    @staticmethod
    def sym_diff_dist(pw_id_1, pw_id_2, relations, dfs, pws, rls_to_use: list=None):

        if pw_id_1 == pw_id_2:
            return 0

        if not rls_to_use:
            rls_to_use = [i for i in range(len(relations))]

        dist = 0
        for rl_name in rls_to_use:
            redundant_cols = PWEQuery.redundant_column(expected_pws=len(pws), dfs=dfs, rl_name=rl_name,
                                                       pws_to_consider=[pw_id_1, pw_id_2], do_print=False)[0]
            cols_to_consider = set(list(dfs[rl_name])[1:])
            for t in redundant_cols:
                if t in cols_to_consider:
                    cols_to_consider.remove(t[2])
            cols_to_consider = list(cols_to_consider)

            wt1 = 1  # TBD
            k1 = 1  # TBD

            x1 = PWEQuery.difference_both_ways(dfs=dfs, rl_name=rl_name, pw_id_1=pw_id_1, pw_id_2=pw_id_2,
                                               col_names=cols_to_consider, do_print=False)
            dist += wt1 * len(x1) ** k1 if x1 is not None else 0

        return dist

    @staticmethod
    def euler_overlap_diff_dist(pw_id_1, pw_id_2, rl_name, col_name, dfs, pws):

        x1 = PWEQuery.freq(total_num_pws=len(pws), dfs=dfs, rl_name=rl_name, col_names=[col_name], values=['"><"'],
                           pws_to_consider=[pw_id_1], do_print=False)[1][0]
        x2 = PWEQuery.freq(total_num_pws=len(pws), dfs=dfs, rl_name=rl_name, col_names=[col_name], values=['"><"'],
                           pws_to_consider=[pw_id_2], do_print=False)[1][0]
        return abs(x1 - x2)
