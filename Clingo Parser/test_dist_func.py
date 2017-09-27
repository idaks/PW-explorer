import numpy as np
import pandas as pd
from helper import lineno, isfloat, mkdir_p, PossibleWorld, Relation

def dist(pw_id_1, pw_id_2, dfs = None, pws = None, relations = None, conn = None):
	return (pw_id_1 - pw_id_2)

