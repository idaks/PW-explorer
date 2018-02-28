import pandas as pd
import numpy as np
import sys
if __name__ == '__main__':
    df = pd.read_csv(sys.argv[1], names=["left","rel","right","infer"],error_bad_lines=False)
    
    ans = df.loc[ (df["rel"].isin(["<",">"])) & (df["infer"] == "deduced")]
    print ("number of SUBSET from DEDUCED: " + str(len(ans.index)))
    print(ans)
    ans = df.loc[ (df["rel"].isin(["<",">"])) & (df["infer"] == "inferred")] 
    print ("number of SUBSET from INFERRED: " + str( len(ans.index)))
    print(ans)
    ans = df.loc[ (df["rel"] == "><") & (df["infer"] == "inferred")]
    print ("number of OVERLAP from INFERRED: " + str(len(ans.index)))
    print(ans)
    ans = df.loc[ (df["rel"] == "><") & (df["infer"] == "input")]
    print ("number of OVERLAP from INPUT: " + str(len(ans.index)))
    print(ans)
