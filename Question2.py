a=[1,2,3,4,5,6,2,5,3,6,4,6,3,8]
b=[]
x=[]
for values in a:
    res=a.count(values)
    a.sort()
    if(res==1):
        x.append(values)
    elif(res>1):
        b.append(values)
a=x+b
print(a)