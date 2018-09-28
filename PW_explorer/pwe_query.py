#!/usr/bin/env python3

import pandas as pd


class PWEQuery:

    @staticmethod
    def intersection(relations: list, expected_pws: int, dfs: list, rl_id=0, col_names: list=None,
                     pws_to_consider: list=None, do_print: bool=True):

        if not pws_to_consider:
            pws_to_consider = [j for j in range(1, expected_pws + 1)]

        if not col_names:
            col_names = list(dfs[rl_id])[1:]

        df = dfs[rl_id]
        s1 = df[df.pw == pws_to_consider[0]]
        for j in pws_to_consider[1:]:
            s1 = pd.merge(s1, df[df.pw == j], how='inner', on=col_names)
        s1 = s1[col_names]
        if do_print:
            print("Intersection for the relation", str(relations[rl_id].relation_name), "on features",
                  str(', '.join(map(str, col_names))), "for PWs", str(', '.join(map(str, pws_to_consider))))
            if len(s1) > 0:
                print(str(s1))
            else:
                print("NULL")

        return s1

    @staticmethod
    def union(relations: list, expected_pws: int, dfs: list, rl_id: int=0, col_names: list=None,
              pws_to_consider: list=None, do_print: bool=True):

        if not pws_to_consider:
            pws_to_consider = [j for j in range(1, expected_pws + 1)]

        if not col_names:
            col_names = list(dfs[rl_id])[1:]

        df = dfs[rl_id]
        s1 = df[df.pw == pws_to_consider[0]]
        for j in pws_to_consider[1:]:
            s1 = pd.merge(s1, df[df.pw == j], how='outer', on=col_names)
        s1 = s1[col_names]

        if do_print:
            print("Intersection for the relation", str(relations[rl_id].relation_name), "on features",
                  str(', '.join(map(str, col_names))), "for PWs", str(', '.join(map(str, pws_to_consider))))
            if len(s1) > 0:
                print(str(s1))
            else:
                print("NULL")

        return s1

    @staticmethod
    def freq(relations: list, expected_pws: int, dfs: list, rl_id: int=0, col_names: list=None, values: list=None,
                   pws_to_consider: list=None, do_print: bool=True):

        all_tuples = None
        freqs = []

        if not pws_to_consider:
            pws_to_consider = [j for j in range(1, expected_pws + 1)]

        if col_names and values and len(col_names) != len(values):
            print('Lengths of col_names and values don\'t match.')
            return None

        if not col_names:
            col_names = list(dfs[rl_id])[1:]

        if not values:
            all_tuples = PWEQuery.union(relations, expected_pws, dfs, rl_id, col_names, pws_to_consider, False)
        else:
            k = [values]
            all_tuples = pd.DataFrame(k, columns=col_names)

        df = dfs[rl_id]
        for j in range(len(all_tuples)):
            expr = ''
            for k in range(len(col_names) - 1):
                expr += str(col_names[k]) + ' == ' + "'" + str(all_tuples.ix[j][k]) + "'" + ' and '
            expr += str(col_names[-1]) + ' == ' + "'" + str(all_tuples.ix[j][-1]) + "'"
            expr += ' and pw in [' + str(', '.join(map(str, pws_to_consider))) + ']'
            s3 = df.query(expr)
            tmp = len(s3)
            if do_print:
                print("Frequency of tuple " + str(tuple(all_tuples.ix[j])) + ' of the relation ' + str(
                    relations[rl_id].relation_name) + ' for attributes ' + str(
                    ', '.join(map(str, col_names))) + ' in PWs ' + str(
                    ', '.join(map(str, pws_to_consider))) + " is: " + str(tmp))
            freqs.append(tmp)

        return all_tuples, freqs

    @staticmethod
    def num_tuples(relations: list, dfs: list, rl_id: int, pw_id: int, do_print: bool=True):

        df = dfs[rl_id]
        c = len(df[df.pw == pw_id])
        if do_print:
            print("There exist " + str(c) + " tuples of relation " + str(relations[rl_id].relation_name) + " in PW " + str(
                pw_id))
        return c

    @staticmethod
    def difference(relations: list, dfs: list, rl_id: int, pw_id_1: int, pw_id_2: int, col_names: list=None,
                         do_print: bool=True):

        if not col_names:
            col_names = list(dfs[rl_id])[1:]

        df = dfs[rl_id]
        x1 = df[df.pw == pw_id_1][col_names]
        x2 = df[df.pw == pw_id_2][col_names]

        diff = pd.concat([x1, x2, x2]).drop_duplicates(keep=False)
        if do_print:
            print(
                "Following is the difference between PWs {} and {} in features {} of "
                "relation {}\n".format(pw_id_1, pw_id_2, str(', '.join(map(str, col_names))),
                                       str(relations[rl_id].relation_name)))
            print(str(diff))
        return diff

    @staticmethod
    def difference_both_ways(relations: list, dfs: list, rl_id: int, pw_id_1: int, pw_id_2: int,
                             col_names: list=None, do_print: bool=True):

        if not col_names:
            col_names = list(dfs[rl_id])[1:]

        x1 = PWEQuery.difference(relations, dfs, rl_id, pw_id_1, pw_id_2, col_names, False)
        x2 = PWEQuery.difference(relations, dfs, rl_id, pw_id_2, pw_id_1, col_names, False)

        diff = x1.append(x2, ignore_index=True)

        if do_print:
            print("Following tuples are in one of PW {} or {}, but not both, for relation {} and features {}\n".format(
                pw_id_1, pw_id_2, str(relations[rl_id].relation_name), str(', '.join(map(str, col_names)))))
            print(str(diff))
        return diff

    @staticmethod
    def redundant_column(relations: list, expected_pws: int, dfs: list, rl_id: int=0, col_names: list=None,
                               pws_to_consider: list=None, do_print: bool=True):

        if not pws_to_consider:
            pws_to_consider = [j for j in range(1, expected_pws + 1)]

        if not col_names:
            col_names = list(dfs[rl_id])[1:]

        # PW specific:
        redundant_pw_specific = []

        df = dfs[rl_id]

        for ft in col_names:
            x1 = df.groupby('pw')[ft].nunique()
            for i in pws_to_consider:
                if x1.ix[i] <= 1:
                    redundant_pw_specific.append((i, rl_id, ft))
                    if do_print:
                        print('Column ' + str(ft) + ' is redundant in relation ' + str(
                            relations[rl_id].relation_name) + ' in PW ' + str(i))

        # Across all PWs:
        redundant_across_pws = []
        x1 = df[df.pw.isin(pws_to_consider)]
        for ft in col_names:
            if x1[ft].nunique() <= 1:
                redundant_across_pws.append((pws_to_consider, rl_id, ft))
                if do_print:
                    print('Column ' + str(ft) + ' is redundant in relation ' + str(
                        relations[rl_id].relation_name) + ' for PWs ' + str(', '.join(map(str, pws_to_consider))))

        return redundant_pw_specific, redundant_across_pws

    @staticmethod
    def unique_tuples(relations: list, expected_pws: int, dfs: list, rl_id: int=0, col_names: list=None,
                      pws_to_consider: list=None, do_print: bool=True):

        if not pws_to_consider:
            pws_to_consider = [j for j in range(1, expected_pws + 1)]

        if not col_names:
            col_names = list(dfs[rl_id])[1:]

        relevant_tuples, freqs = PWEQuery.freq(relations, expected_pws, dfs, rl_id, col_names, [], pws_to_consider,
                                               False)
        unique_tuples = []
        df = dfs[rl_id]

        for i, f in enumerate(freqs):
            if f == 1:
                expr = ''
                for k in range(len(col_names) - 1):
                    expr += str(col_names[k]) + ' == ' + "'" + str(relevant_tuples.ix[i][k]) + "'" + ' and '
                expr += str(col_names[-1]) + ' == ' + "'" + str(relevant_tuples.ix[i][-1]) + "'"
                expr += ' and pw in [' + str(', '.join(map(str, pws_to_consider))) + ']'
                s3 = df.query(expr)
                s3 = s3.reset_index(drop=True)
                unique_pw = s3.ix[0]['pw']

                unique_tuples.append((relevant_tuples.ix[i], unique_pw))

                if do_print:
                    print('The unique tuple ', tuple(relevant_tuples.ix[i]), 'occurs only in PW', unique_pw)

        return unique_tuples
