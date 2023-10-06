
"""
Square wave analysis in Python

"""
import matplotlib.pyplot as plt
import numpy as np
from sympy import *
%matplotlib
from scipy import signal

# Ask the user for amplitude and time period
A=eval(input("Enter Amplitude:"))
T=eval(input("Enter time period:"))/2  #2T is the period of wave , so we need to give half value in T

t = np.linspace(0, 10, 1000, endpoint=False)

plt.subplot(2,1,1)
# Multiply the square wave function by the amplitude and adjust the frequency using the time period
plt.plot(t, A * signal.square(2 * np.pi * (1/T) * t/2),'r')
plt.title('Square wave by inbuilt method')
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.grid()
plt.show()

pi=np.pi
x,n,t=symbols('x n t',real=True)


N=eval(input("Enter Number of terms:"))

a0=(1/T)*(integrate((A),(x,0,T)).evalf() + integrate((-A),(x,T,2*T)).evalf())
an_values = [(1/T)*(integrate((A*cos(n*pi*x/T)),(x,0,T)).evalf() + integrate((-A*cos(x*n*pi/T)),(x,T,2*T)).evalf()) for n in range(1,N+1)]
bn_values = [(1/T)*(integrate((A*sin(n*pi*x/T)),(x,0,T)).evalf() + integrate((-A*sin(x*n*pi/T)),(x,T,2*T)).evalf()) for n in range(1,N+1)]

def f(value):
    sum=0
    for n in range(1,N+1):
        sum += an_values[n-1]*cos(n*pi*x/T) + bn_values[n-1]*sin(n*pi*x/T)
    return (sum+a0/2).subs(x,value)

a=np.linspace(0,10,1000)
b=[f(i) for i in a]
plt.subplot(2,1,2)
plt.plot(a,b,'b')
plt.grid()
plt.title('Square wave by fourier series')
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
