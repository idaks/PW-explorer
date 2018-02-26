#!/usr/bin/env python3
from sys import argv

#get the underlying pattern in the form of a list of ints
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

	return pattern

#check if two patterns are the same (cyclically equivalent)
def compare_patterns(s1, s2):

	if s1 == s2:
		return True

	return cyclically_equivalent(s1, s2)

#check if two lists are cyclically equivalent
def cyclically_equivalent(s1,s2):

	n, i, j = len(s1), 0, 0
	if n != len(s2):
		return False

	while i < n and j < n:
		k = 1
		while k <= n and s1[(i+k) % n] == s2[(j+k) % n]:
			k += 1
		if k > n:
			return True
		if s1[(i+k) % n] > s2[(j+k) % n]:
			i += k
		else:
			j += k
	return False


#Basically given u and v, check if u is a sublist of vv (v followed by another copy of v)
def alternate_cyclically_equivalent(s1, s2):

	if len(s1) != len(s2):
		return False

	u = s1.copy()
	v = s2.copy()
	v.extend(v)

	return is_sublist(v, u)

#check if s is a sublist of l
def is_sublist(l, s):

	is_a_subset = False
	if s == []:
		is_a_subset = True
	elif s == l:
		is_a_subset = True
	elif len(s) > len(l):
		is_a_subset = False
	else:
		for i in range(len(l)):
			if l[i] == s[0]:
				n = 1
				while (n < len(s)) and (l[i+n] == s[n]):
					n += 1
				if n == len(s):
					is_a_subset = True
					break

	return is_a_subset


def dist(s1, s2):

	pattern_s1 = get_pattern(s1)
	pattern_s2 = get_pattern(s2)

	return compare_patterns(pattern_s1, pattern_s2)


# script, sequence = argv
# print(get_pattern(sequence))

