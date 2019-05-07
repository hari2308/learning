#input list with dictionaries
x = [{"b":1},{"d":2},{"a":3},{"c":4}]

#list for sorting the keys 
b = []
for i in range(0,len(x)):
    for i in x[i]:
        b.append(i)
b=sorted(b)

#list for appending the sorted keys

c =[]
for y in b:
    for j in range(0,len(x)):
        if y in x[j].keys():
            c.append(x[j][y])
            
#list for creating required output
e = []
#for tupling the sorted keys with values 
d = zip(b,c)
#iterating the tuples to add them in dictonary
for x,y in d:
    #dictonary for creating and appending in output list
    u = {}
    #adding new key and value to dictnoary
    u[x] = y
    #appending values to dictonary
    e.append(u)
    # deleting dictonary in order to removed the added keys and values to output list
    del u
#printing output list    
print(e)

#output:
# [{'a': 3}, {'b': 1}, {'c': 4}, {'d': 2}]
