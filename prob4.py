import numpy as np
import matplotlib.pyplot as plt
n=1024
arr=np.random.rand(n)

#(a)
plt.figure()
plt.plot(arr, label='Sample')
plt.legend()



#(b)
dft=np.fft.fft(arr)
karr=np.fft.fftfreq(n,d=1)
karr=2*np.pi*karr
sort=np.argsort(karr)
skarr=karr[sort]
sdft=dft[sort]
spectra=abs(sdft)*abs(sdft)/n
plt.figure()
plt.plot(skarr,spectra, label='Spectra')
plt.legend()
#print(spectra)

#(c)
kmax=np.amax(skarr)
kmin=np.amin(skarr)
print('Minimum k =',kmin,'\nMaximum k =',kmax)
plt.legend()
plt.show()
#(d)




