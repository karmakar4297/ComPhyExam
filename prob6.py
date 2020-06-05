import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import odeint
def fun(y, x):
    y1, y2 = y
    temp1=32*y1+66*y2+(2/3)*x+(2/3)
    temp2=-66*y1-133*y2-(1/3)*x-(1/3)
    dydx=[temp1, temp2]
    return dydx
y0=[(1/3), (1/3)]
x=np.linspace(0,0.5,100)
sol=odeint(fun, y0, x)
plt.plot(x,sol[:,0],color='blue', label='y1')
plt.plot(x,sol[:,1],color='red', label='y2')
plt.xlabel('x')
plt.legend()
plt.show()




######################Below I did the same with RK4.
######################The ODE is stiff (Not in the given range though)
###################### That is why I used the library functions above.
'''
def f(r,t):
    u1=r[0]
    u2=r[1]
    #u3=r[2]
    f1=32*u1+66*u2+(2/3)*t+(2/3)
    f2=-66*u1-133*u2-(1/3)*t-(1/3)
   # f3=u1+2*u2+np.exp(-t)
    return np.array([f1, f2])

h=float(input('Enter step size: '))
n=int(1/h+1)
t=np.linspace(0,0.5,n)
r=np.array([(1/3),(1/3)]) # r array with the intitial values for u1, u2 and u3   
u1=np.array([1/3])
u2=np.array([1/3])
#u3=np.array([1])
for i in range(0,n-1):
    k1 = h*f(r,t[i])
    k2 = h*f(r+k1/2.0,t[i]+h/2.0)
    k3 = h*f(r+k2/2.0,t[i]+h/2.0)
    k4 = h*f(r+k3,t[i]+h)
    r=r+(k1+2*k2+2*k3+k4)/6
    u1=np.append(u1,r[0])
    u2=np.append(u2,r[1])
   # u3=np.append(u3,r[2])
plt.plot(t,u1,color='blue', label='y1')
plt.plot(t,u2,color='red', label='y2')
#plt.plot(t,u3,color='black', label='u3')
plt.xlabel('x')
plt.legend()
plt.show()
'''
