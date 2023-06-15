#https://www.codewars.com/kata/57ee4a67108d3fd9eb0000e7

#original solution
#I think in this case nested loops are a necessary evil, resulting in this problem being quadtratic. I am aware quadratic is a problem for me, apparently. 
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    birb = []
    
    for i in birds:
        if i not in geese:
            birb.append(i)
    
    return birb