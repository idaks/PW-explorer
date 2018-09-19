from sys import argv

script, fname = argv

orig_data = open(fname).readlines()

# also check if the first 3 lines have already been removed
start = 0
for i, line in enumerate(orig_data):
    if line.strip() == 'Solving...':
        start = i + 1
        break

# pre-processing such as removing warnings


temp_data = open(fname, 'w')
temp_data.writelines(orig_data[start:])
