import sys
from sys import argv

script, fname = argv

orig_data = open(fname).readlines()

#preprocssing such as removing warnings




temp_data = open(fname, 'w')
temp_data.writelines(orig_data[3:])

