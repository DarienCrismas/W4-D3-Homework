#https://www.codewars.com/kata/55908aad6620c066bc00002a/solutions/python

#orig solution
def xo(s):
    xamount = 0
    oamount = 0
    for letter in s:
        if letter.lower() == "x":
            xamount += 1
        if letter.lower() == "o":
            oamount += 1
    return oamount == xamount
            
#new solution
def xo_redux(s):
    #should be linear for .count()
    #previous quadtratic, nested linear operations
    #.upper is just for something new, I know .lower is standard
    return s.upper().count("x") == s.upper().count("o")