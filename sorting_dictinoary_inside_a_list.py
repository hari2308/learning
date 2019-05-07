x = [{"b":1},{"d":2},{"a":3},{"c":4}]
b = []
for i in range(0,len(x)):
    for i in x[i]:
        b.append(i)
b=sorted(b)

c =[]
for y in b:
    for j in range(0,len(x)):
        if y in x[j].keys():
            c.append(x[j][y])
            
e = []            
d = zip(b,c)
r = 0

for x,y in d:
    u = {}
    u[x] = y
    e.append(u)
    del u
    r +=1
   
print(e)

#output:
# [{'a': 3}, {'b': 1}, {'c': 4}, {'d': 2}]
