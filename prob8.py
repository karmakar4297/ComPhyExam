import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp
import math


#############Fisrt Equation
def fun(t,y):
    return np.vstack((y[1],4*(y[0]-t)))
def bc(ya,yb):
    return np.array([ya[0],yb[0]-2])
    
x=np.linspace(0,1,10)
n=x.size
y1=np.zeros((2,n),dtype=float)
y1[0]=0 
sol1=solve_bvp(fun,bc,x,y1)


ytr1=np.zeros(n, dtype=float)
err=np.zeros(n)
coeff=math.exp(2)/(math.exp(4)-1)
for i in range(0,n):
    ytr1[i]=coeff*(math.exp(2*x[i])-math.exp(-2*x[i]))+x[i]
    err[i]=(ytr1[i]-sol1.sol(x)[0][i])/(sol1.sol(x)[0][i])

print('\n The rel. errs in percentage:\n')
for i in range(err.size):
    if(i==0):
        print(abs(err[i]),'The error is comparable to the value as both are very small for this case\n')
    else:    
        print(abs(err[i]),'\n')
plt.figure()
plt.plot(x,sol1.sol(x)[0],'.-',label='Numerical')
plt.plot(x,ytr1,'r--',label='Analytical')
#plt.title(r'$y=log(x)$')
plt.legend()
plt.show()
