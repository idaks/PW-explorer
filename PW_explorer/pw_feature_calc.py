#!/usr/bin/env python3

import numpy as np
from .query import PWEQuery
from .helper import pw_slicer


class PWEFeatureCalculation:

    @staticmethod
    def custom_feature_calculation(pws_rel_dfs, rel_schemas, pw_objs, func=lambda pw_dfs, rel_schemas, pw_obj: 0):

        features = {}
        for pw_obj in pw_objs:
            pw_id = pw_obj.pw_id
            dfs, _ = pw_slicer(pws_rel_dfs, None, [pw_id])
            features[pw_id] = func(dfs, rel_schemas, pw_obj)
        return features

    @staticmethod
    def euler_complexity_analysis(expected_pws, dfs, rl_name, col_name, pws_to_consider: list = None, do_print=True):

        if not pws_to_consider:
            pws_to_consider = [j for j in range(1, expected_pws + 1)]

        complexities = np.zeros(len(pws_to_consider))

        for i, pw in enumerate(pws_to_consider):
            complexities[i] = PWEQuery.freq(expected_pws, dfs, rl_name, [col_name], ['"><"'], [pw], False)[1][0]

        if np.max(complexities) != np.min(complexities):
            complexities = (complexities - np.min(complexities)) / (np.max(complexities) - np.min(complexities))
        if do_print:
            paired_pw_compl = list(zip(pws_to_consider, complexities))
            paired_pw_compl = sorted(paired_pw_compl, key=lambda x: x[1], reverse=True)
            print('PWs:         ', str([x[0] for x in paired_pw_compl]))
            print('Complexities:', str([x[1].round(2) for x in paired_pw_compl]))

        return complexities
