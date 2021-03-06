# -*- coding: utf-8 -*-
"""SEÑALES.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1D3cpXC_CEZlfTE-F2Qeobvc0-hcW5POk
"""
#SEÑAL TRIANGULAR
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
import scipy.stats as stats
# INGRESO
# Rango en tiempo de la señal y muestras
a=0
b=1
n = 2000
# Frecuencia de la señal en Hz
fs= 5

# PROCEDIMIENTO
# Simetria de la señal triangular diente de sierra
simetria=0.5
t = np.linspace(a, b, n)
senal = signal.sawtooth(2 * np.pi * fs * t, simetria)

# SALIDA
plt.grid('on')
plt.plot(t,senal,'pink')
plt.title('Señal Triangular')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.show()

#SEÑAL EXPONENCIAL
sigma = 10
omega = 0

s = complex(sigma,omega)
senal = np.exp(s*t)

# SALIDA - gráfica
plt.grid('on')
plt.plot(t,np.real(senal),'black')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.margins(0.1)
plt.title('Señal Exponencial')
plt.show()

# Commented out IPython magic to ensure Python compatibility.
#SEÑAL IMPULSO UNITARIO 
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
t=np.arange(-1,10,1)
δ=(t==0)*1.0
plt.stem(t,δ)
plt.grid('on')
plt.title('Señal Impulso Unitario')

#SEÑAL SENOIDAL
import numpy as np
import pylab as pl

#DATOS
t=np.linspace(0,1,100)
f0=5
s=np.cos(2*np.pi*f0*t-np.pi/2)

#GRÁFICA
pl.plot(t,s,'purple')
pl.grid('on')
pl.xlabel('Tiempo')
pl.ylabel('Amplitud')
pl.title('Senoidal')
pl.show()

#SEÑAL DIENTE DE SIERRA
from scipy import signal 
import matplotlib.pyplot as plot 
import numpy as np 
t = np.linspace(0, 1, 1000, endpoint=True) 
plot.plot(t, signal.sawtooth(2 * np.pi * 5 * t),'g') 
plot.grid('on')
plot.xlabel('Tiempo') 
plot.ylabel('Amplitud') 
plot.title('Señal Diente de Sierra') 
plot.show()

# Señal Sinusoidal con Dos Armónicos

import matplotlib.pyplot as plt
import numpy as np
from numpy import pi

n = 2 ** 6 # Número de intervalos
f = 400.0 # Hz
dt = 1 / (f * 16) # Espaciado, 16 puntos por período
t = np.linspace(0, (n - 1) * dt, n) # Intervalo de tiempo en segundos
y = np.sin(2 * pi * f * t) - 0.5 * np.sin(2 * pi * 2 * f * t) # Señal
plt.grid('on')
plt.plot(t, y,'r')
plt.xlabel('Tiempo (s)')
plt.ylabel('y(t)')
plt.title('Señal Sinusoidal con Dos Armónicos')