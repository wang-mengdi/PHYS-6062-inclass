import numpy as np
from gaussxw import gaussxw


def I(f,a,b,N):
    h = (b-a)/N
    sum = 0.5*(f(a)+f(b))
    for k in range(1,N):
        sum+=f(a+k*h)
    return h*sum

def S(f,a,b,N):
    h = (b-a)/N
    fx = f(np.linspace(a,b,N+1))
    return h/3*( f(a)+f(b) + 4*fx[1:N:2].sum() + 2*fx[2:N-1:2].sum())

def G(f,a,b,N):
    x,w = gaussxw(N)
    x = x*(b-a)/2 + (b+a)/2
    w = w * (b-a)/2
    fx = f(x)
    return np.dot(w,fx)

f = lambda x: x**4-2*x+1
a,b=0,2
#print(I(f,a,b,10))
#print(I(f,a,b,100))
#print(I(f,a,b,1000))
#print(S(f,a,b,10))
print(G(f,a,b,3))
print(G(f,a,b,10))
print(G(f,a,b,100))