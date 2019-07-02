
# coding: utf-8

# In[48]:


import numpy as np


# In[33]:


def bezout(a, b):
    x, xx, y, yy = 1, 0, 0, 1
    i = -1
    r_prev = a
    while b:
        q = a // b
        a, b = b, a % b
        #print("a = b, b = a - b * q")
        x, xx = xx, x - xx*q
        y, yy = yy, y - yy*q
        i+=1
        r_prev = a
    return (x, y, a)


# In[34]:


def sum_same(G_x, G_y, a, n):
    if G_x == Q_x and G_y == (-G_y % n):
        return float("inf"), float("inf") 
    if G_x == float("inf") and G_y == float("inf"):
        return float("inf"), float("inf") 
    print("Правило сложения для одинаковых точек c одинаковой координатой (G и G)")
    print("m = (3*G_x * G_x + a) / (2 * G_y)")
    step =  2*G_y %n
    step = bezout(n , step)[1]
    step %= n
    print("(2 * G_y)^(-1) = %d" %(step))
    var = (3 * G_x * G_x + a) %n
    print("(3*G_x * G_x + a) = %d" %(var))
    var *= step
    m = var %n
    print("m = %d" %(var %n))
    print("G_x_2 = m^2 - 2*G_x")
    G_x_1 = (m *m - 2 * G_x) %n
    print("G_x_2 = %d" %(G_x_1))
    print("G_y_2 = -G_y + m *(-G_x_2 + G_x)")
    G_y_1 = (-G_y + m *(-(G_x_1 - G_x)%n)) %n
    print("G_y_2 = %d" %(G_y_1))
    return G_x_1 % n, G_y_1 % n


# In[35]:


def sum_diff(G_x, G_y, Q_x, Q_y,n, a):
    if G_x == Q_x and G_y == (-Q_y % n):
        return float("inf"), float("inf") 
    if G_x == float("inf") and G_y == float("inf"):
        return Q_x, Q_y 
    if Q_x == float("inf") and Q_Y == float("inf"):
        return G_x, G_y
    if G_x == Q_x and Q_y == G_y:
        return(sum_same(G_x, G_y,a,n))
    print("Правило сложения для  точек c разной координатой (G и Q)")
    print("m = (G_x - Q_x) / (G_x - x_A)")
    step =  (G_x - Q_x) %n
    step = bezout(n , step)[1]
    print("(G_x - Q_x)^-1 = %d" %(step))
    step %= n
    var = (G_y - Q_y) %n
    print("(G_y - Q_y)^-1 = %d" %(var))
    var *= step
    m = var %n
    print("m = %d" %(var %n))
    print("G_x_1 = m^2 - G_x - Q_x")
    x_2 = (m *m - G_x - Q_x) %n
    print("G_x_1 = %d" %(x_2))
    print("G_y_1 = -G_y + m *(-G_x_1 + G_x)")
    y_2 = (-G_y + m *(-(x_2 - G_x)%n)) %n
    print("G_y_1 = %d" %(y_2))
    return x_2 % n, y_2 %n


# In[42]:


print("Введите коэффициенты эллиптической кривой y= x^3 +a*x + b и генератор G а также модуль")
print("a b G_x G_y n")
a, b, G_x, G_y, n=  list(map(int, input().split(' ')))


# In[46]:


Q_x = G_x
Q_y = G_y
res = [(G_x, G_y)]
while(Q_x != float("inf") and Q_y  != float("inf")):
    Q_x, Q_y = sum_diff(G_x, G_y, Q_x, Q_y,n, a)
    res.append((Q_x, Q_y))
print("Ответ")
print("Длина подгруппы = %d" %(len(res)))
print("Точки"  + str(res))


# In[49]:


get_ipython().system('jupyter nbconvert --to script 7.3ipynb')

