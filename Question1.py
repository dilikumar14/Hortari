l=['Phil','Alan','Phil','Alan','Alan','Phil','Alan','Phil','Phil']
n1=l.count('Alan')
n2=l.count('Phil')
if(n1==n2):
    l.sort()
    print('Winner is %s'%(l[-1]))
elif(n1>n2):
    print('Winner is Alan')
else:
    print('Winner is Phil')