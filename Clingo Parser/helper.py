import errno
import inspect
import sys
from sys import argv
import string
import os


###################################################################

#to help debug
def lineno():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno

###################################################################

###################################################################

#helper funcs

def isfloat(value):
  """returns true if a value can be typecasted as a float, else false"""
  try:
    float(value)
    return True
  except ValueError:
    return False

def mkdir_p(path):
    """make a directory if it doesn't already exist"""
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

###################################################################

###################################################################

#Class to store details and solution relating to every possible world

class PossibleWorld:
    n_pws = 1
    def __init__(self, num_relations):
        self.rls = [[] for i in range(num_relations)]
        self.pw_id = PossibleWorld.n_pws
        PossibleWorld.n_pws += 1
        self.pw_soln = 0


    def add_relation(self, relation_id, relation_data):
        if relation_id >= len(self.rls):
            self.rls.append([])
        self.rls[relation_id].append(relation_data)

###################################################################

###################################################################

#Class to store description of each relation found in the clingo output

class Relation:
    def __init__(self, relation_name):
        self.relation_name = relation_name
        self.arrity = 0
        self.r_id = 0

###################################################################