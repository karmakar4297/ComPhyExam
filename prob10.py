import numpy as np
import matplotlib.pyplot as plt
#np.set_printoptions(precision=3, suppress=True)

def f(x):
    if(x<1 and x>-1):
        return 1
    else:
        return 0

xmin =-5
xmax=5
n=1024
dx=(xmax-xmin)/(n-1)

sample=np.zeros(n)
xarr=np.zeros(n)

for i in range(n):
    sample[i]=f(xmin+i*dx)
    xarr[i]=xmin+i*dx
dft=np.fft.fft(sample, norm='ortho')
karr=np.fft.fftfreq(n, d=dx)
karr=2*np.pi*karr
factor=np.exp(-1j*karr*xmin)
aft=dx*np.sqrt(n/(2.0*np.pi))*factor*dft

sort=np.argsort(karr)
karr=karr[sort]
aft=aft[sort]
plt.subplot(4,1,1)
plt.plot(xarr, sample, 'g--', label='The box function')
plt.legend(loc='upper right')
plt.xlabel('x')


plt.subplot(4,1,2)
plt.plot(karr,aft, 'b', label='FT with 1024 sample points')
plt.legend(loc='upper right')
plt.xlabel('k')
###############
n=128
dx=(xmax-xmin)/(n-1)

sample=np.zeros(n)
xarr=np.zeros(n)

for i in range(n):
    sample[i]=f(xmin+i*dx)
    xarr[i]=xmin+i*dx
dft=np.fft.fft(sample, norm='ortho')
karr=np.fft.fftfreq(n, d=dx)
karr=2*np.pi*karr
factor=np.exp(-1j*karr*xmin)
aft=dx*np.sqrt(n/(2.0*np.pi))*factor*dft

sort=np.argsort(karr)
karr=karr[sort]
aft=aft[sort]
plt.subplot(4,1,3)
plt.plot(karr,aft, color='black', label='FT with 128 sample points')
plt.legend(loc='upper right')
plt.xlabel('k')
##############################
n=32
dx=(xmax-xmin)/(n-1)

sample=np.zeros(n)
xarr=np.zeros(n)

for i in range(n):
    sample[i]=f(xmin+i*dx)
    xarr[i]=xmin+i*dx
dft=np.fft.fft(sample, norm='ortho')
karr=np.fft.fftfreq(n, d=dx)
karr=2*np.pi*karr
factor=np.exp(-1j*karr*xmin)
aft=dx*np.sqrt(n/(2.0*np.pi))*factor*dft

sort=np.argsort(karr)
karr=karr[sort]
aft=aft[sort]
plt.subplot(4,1,4)
plt.plot(karr,aft, color='grey', label='FT with 32 sample points')
plt.legend(loc='upper right')
plt.xlabel('k')
plt.show()
