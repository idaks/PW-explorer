import sys
from sys import argv
import argparse
import string
import os
import subprocess32 as subprocess

parser = argparse.ArgumentParser()
parser.add_argument("fnames", type = str, help = "provide the clingo files", nargs= '+')
parser.add_argument("project_name", type = str, help = 'provide a suitable session/project name to reference these results in future scripts')
parser.add_argument("-n", "--num_solutions", type = int, default = 0, help = "number of solutions to generate using clingo, optional, generates all by default")
args = parser.parse_args()

fnames = args.fnames
project_name = args.project_name

for fname in fnames:
	if not os.path.exists(fname):
		print "Could not find the file {}".format(str(fname))
		exit(1)

clingo_in_files = []

for i, fname in enumerate(fnames):
	clingo_in_files.append('Mini Workflow/clingo_input/{}{}.lp4'.format(project_name, ('_' + str(i)) if len(fnames) > 1 else ''))
	subprocess.check_call(['cp', fname, clingo_in_files[-1]])
print "Copied files into the clingo_input folder"

t = ['clingo', '-n {}'.format(args.num_solutions), '-Wnone']
t.extend(clingo_in_files)
#['clingo', '-n {}'.format(args.num_solutions), '-Wnone', str(" ".join(clingo_in_files))]
proc = subprocess.Popen(t, stdout=subprocess.PIPE)
clingo_output = proc.communicate()[0]

#print clingo_output
orig_data = clingo_output.splitlines()

start = 0
for i, line in enumerate(orig_data):
	if line.strip() == 'Solving...':
		start = i+1
		break

temp_data = open('Mini Workflow/clingo_output/{}.txt'.format(project_name), 'w')
temp_data.writelines('\n'.join(orig_data[start:]))
print "Preprocessed clingo output written to clingo_output/{}.txt".format(project_name)

temp_data.close()





