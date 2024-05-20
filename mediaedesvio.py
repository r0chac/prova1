#print('hello world')


import math
x=input('x?').split()
xt=(0)
for i in range(len(x)):
    x[i]= float(x[i])
    xt= xt+x[i]
xm=xt/len(x)
print(xm) 
xdv=(0)
for i in range(len(x)):
    x[i]= (x[i]-xm)**2 
    #print(x[i])
    xdv = xdv + x[i]
    #print(xdv) *xdesvio padrão
dp= math.sqrt(xdv/len(x))
print(dp)



    