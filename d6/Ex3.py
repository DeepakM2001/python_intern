
d1=['A','S','D','f','E','O']
d2=[7,8,9,5,4,3]
res = {}
for key in d1:
    for value in d2:
        res[key] = value
        d2.remove(value)
        break  
print("Dictionary is ",str(res))

