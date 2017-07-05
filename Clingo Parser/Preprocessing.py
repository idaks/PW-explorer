import sys
from sys import argv

script, fname = argv

orig_data = open(fname).readlines()

#also check if the first 3 lines have already been removed
#preprocessing such as removing warnings




temp_data = open(fname, 'w')
temp_data.writelines(orig_data[3:])

