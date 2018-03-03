from sys import argv

script, folder_loc = argv
n_PWs = int(folder_loc[folder_loc.rfind('_')+1:folder_loc.rfind('/')-2])


def getStats(f):
    for i, l in enumerate(f):
        k = l.find("overlaps (inferred)")
        if (k) != -1:
            print ("Overlaps (inferred):" ,l[k+35:l.find("<", k+35)])

        k = l.find("overlaps (input)")
        if (k) != -1:
            print ("Overlaps (input):", l[k+32:l.find("<", k+32)])

        k = l.find("is_a (input)")
        if (k) != -1:
            print ("is_a (input):", l[k+28:l.find("<", k+28)])
        
        k = l.find("is_a (inferred)")
        if (k) != -1:
            print ("is_a (inferred):", l[k+31:l.find("<", k+31)])
        
        k = l.find("congruent")
        if k != -1:
            print ("Congruent:" ,f[i+1][5:f[i+1].find("<",5)])

for i in range(n_PWs):
    f = open("{}/CEN-NDC-regions_{}_mnpw.gv".format(folder_loc, i)).readlines()
    print ("PW {}:".format(i+1))
    getStats(f)
    print ()