import re
#https://www.codewars.com/kata/52fba66badcd10859f00097e/solutions/python

#original solution
def disemvowel(string_):
    vow = ["a", "e", "i", "o", "u"]
    chars = []

    for i in string_:
        if i.lower() not in vow:
            chars.append(i)

    return "".join(chars)

#new solution
#I think it should be about linear if I'm interpretting documentation correctly, vs the previous being quadratic for the nested linear operations
def disemvowel_redux(string_):
    return re.sub("[aeiouAEIOU]", "", string_.lower())