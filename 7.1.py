
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


def bezout(a, b):
    print('Алгоритм евклида')
    x, xx, y, yy = 1, 0, 0, 1
    print("\ta = %d, b = %d" %(a, b))
    print("\ty_-2 = %d  y_-1 = %d" %(xx,  x))
    print("")
    i = -1
    r_prev = a
    while b:
        q = a // b
        a, b = b, a % b
        #print("a = b, b = a - b * q")
        print("\tr_%d = q_%d*r_%d + r_%d"%(i-1, i+1, i, i+1))
        print("\t%d = %d * %d + %d" %(r_prev,q, a, b))
        x, xx = xx, x - xx*q
        y, yy = yy, y - yy*q
        print("\ty_%d = %d" %(i, y))
        i+=1
        print("")
        r_prev = a
    print("Алгоритм евклида закончен")
    return (x, y, a)


# In[3]:


print("Введите коэффициенты эллиптической кривой y= x^3 +a*x + b и точку A а также модуль")
print("a b x y n")
a,b,x, y, n=  list(map(int, input().split(' ')))


# In[4]:


print("Правило сложения для одинаковых точек c одинаковой координатой (A и A)")
print("m = (3*x_A * x_A + a) / (2 * y_A)")
step =  2*y %n
print("Найдем (2 * y_A) = %d" %(step))
print("Найдем (2 * y_A)^-1")
step = bezout(n , step)[1]
print("(2 * y_A)^(-1) = %d" %(step))
step %= n
print("(2 * y_A)^(-1) = %d" %(step))
var = (3 * x * x) %n
print("(3*x_A * x_A) = %d" %(var))
var = (3*x * x + a) %n
print("(3x_A * x_A + a) = %d" %(var))
var *= step
m = var %n
print("m = %d" %(var %n))
print("x_2A = m^2 - 2*x_A")
x_1 = (m *m - 2 * x) %n
print("x_2A = %d" %(x_1))
print("y_2A = -y_A + m *(-x_2A + x_a)")
y_1 = (-y + m *(-(x_1 - x)%n)) %n
print("y_2A = %d" %(y_1))


# In[5]:


print("Правило сложения для  точек c одинаковой координатой (A и 2A)")
print("m = (y_2A - y_A) / (x_2A - x_A)")
step =  (x_1 - x) %n
print("Найдем (x_2A - x_A) = %d" %(step))
print("Найдем (x_2A - x_A)^-1")

step = bezout(n , step)[1]
print("(x_2A - x_A)^-1 = %d" %(step))
step %= n
print("(x_2A - x_A)^-1 = %d" %(step))
var = (y_1 - y) %n
print("y_2A - y_A = %d" %(var))
var *= step
m = var %n
print("m = %d" %(var %n))
print("x_3A = m^2 - x_2A - x_A")
x_2 = (m *m - x_1 - x) %n
print("x_3A = %d" %(x_2))
print("y_3A = -y_2A + m *(-x_3A + x_2A)")
y_2 = (-y_1 + m *(-(x_2 - x_1)%n)) %n
print("y_3A = %d" %(y_2))


# In[6]:


print("Ответ")
print("2A(%d,%d)  3A(%d%,d)" %(x_1 y_1, x_2, y_2))

