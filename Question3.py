l=[2,2,4,5,6,7,2,8,5,8]
m=[]
n=[]
for value in l:
    occurence=l.count(value)
    l.sort()
    if(occurence>1):
        m.append(value)
    else:
        n.append(value)
print(n,m)