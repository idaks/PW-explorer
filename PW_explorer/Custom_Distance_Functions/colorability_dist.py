#!/usr/bin/env python3
import copy
from collections import defaultdict


def get_colors_list(df, id):
    idx = list(map(int, list(df[df.pw == id].x1)))
    clrs = list(df[df.pw == id].x2)

    ordered_clrs = [x for _, x in sorted(zip(idx, clrs))]
    return ordered_clrs


# get the underlying pattern in the form of a list of ints
def get_pattern(sequence):
    pattern = []
    pattern_dict = {}
    count_unique = 0

    for element in sequence:

        if element in pattern_dict:
            pattern.append(pattern_dict[element])
        else:
            pattern.append(count_unique)
            pattern_dict[element] = count_unique
            count_unique += 1

    return pattern, count_unique


def compare_patterns(p1, p2, check_cyclical_equivalence=True):
    if len(p1) != len(p2):
        return False

    if p1 == p2:
        return True

    if not check_cyclical_equivalence:
        return False

    n = len(p2)
    t2 = copy.copy(p2)

    for i in range(n - 1):
        temp = t2.pop()
        t2.insert(0, temp)
        new_pattern, _ = get_pattern(t2)
        if new_pattern == p1:
            return True

    return False


def dist_helper(s1, s2):
    pattern_s1, unique_s1 = get_pattern(s1)
    pattern_s2, unique_s2 = get_pattern(s2)

    # print s1, s2

    if unique_s1 != unique_s2:
        return 1

    dist_ = 0 if compare_patterns(pattern_s1, pattern_s2) else 1
    # print dist_

    return dist_


def dist(pw_id_1, pw_id_2, **kwargs):

    kwargs = defaultdict(lambda: None, kwargs)
    dfs = kwargs['dfs']
    relations = kwargs['relations']
    if dfs is None or relations is None:
        print("None objects passed in.")
        return -1

    if pw_id_1 == pw_id_2:
        return 0

    col_rel_name = 'col_2'
    df = dfs[col_rel_name]

    s1 = get_colors_list(df, pw_id_1)
    s2 = get_colors_list(df, pw_id_2)

    return dist_helper(s1, s2)


#### DOESN't WORK COMPLETELY. NEED TO GENERATE NEW PATTERN EVERY TIME. NO SHORTCUTS ########

# check if two patterns are the same (cyclically equivalent)
# def compare_patterns(s1, s2):

# 	if s1 == s2:
# 		return True

# 	return cyclically_equivalent(s1, s2)

# check if two lists are cyclically equivalent
# def cyclically_equivalent(s1,s2):

# 	n, i, j = len(s1), 0, 0
# 	if n != len(s2):
# 		return False

# 	while i < n and j < n:
# 		k = 1
# 		while k <= n and s1[(i+k) % n] == s2[(j+k) % n]:
# 			k += 1
# 		if k > n:
# 			return True
# 		if s1[(i+k) % n] > s2[(j+k) % n]:
# 			i += k
# 		else:
# 			j += k
# 	return False


# Basically given u and v, check if u is a sublist of vv (v followed by another copy of v)
# def alternate_cyclically_equivalent(s1, s2):

# 	if len(s1) != len(s2):
# 		return False

# 	u = s1.copy()
# 	v = s2.copy()
# 	v.extend(v)

# 	return is_sublist(v, u)

# check if s is a sublist of l
# def is_sublist(l, s):

# 	is_a_subset = False
# 	if s == []:
# 		is_a_subset = True
# 	elif s == l:
# 		is_a_subset = True
# 	elif len(s) > len(l):
# 		is_a_subset = False
# 	else:
# 		for i in range(len(l)):
# 			if l[i] == s[0]:
# 				n = 1
# 				while (n < len(s)) and (l[i+n] == s[n]):
# 					n += 1
# 				if n == len(s):
# 					is_a_subset = True
# 					break

# 	return is_a_subset
