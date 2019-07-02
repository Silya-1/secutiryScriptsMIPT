
# coding: utf-8

# In[39]:


import numpy as np


# In[40]:


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


# In[41]:


print("Введите коэффициенты эллиптической кривой y= x^3 +a*x + b и генератор G точку Q сообщениz размер группы случайный параметр а также модуль")
print("a b G_x G_y Q_x Q_y m size n")
a, b, G_x, G_y, Q_x, Q_y, m, size,k,n=  list(map(int, input().split(' ')))


# In[14]:


def sum_same(G_x, G_y, a, n):
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
    return G_x_1, G_y_1


# In[37]:


def sum_diff(G_x, G_y, Q_x, Q_y,n):
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
    return x_2, y_2


# In[38]:


d = 1
G_x_1, G_y_1 = sum_same(G_x, G_y, a, n)
d += 1
while((G_x_1, G_y_1) != (Q_x, Q_y)):
    G_x_1, G_y_1 = sum_diff(G_x, G_y,G_x_1,G_y_1, n)
    d += 1


# In[47]:


step = k
G_x_1, G_y_1 = sum_same(G_x, G_y, a, n)
step -=1
while (step > 1):
    G_x_1, G_y_1 = sum_diff(G_x, G_y,G_x_1,G_y_1, n)
    step -=1
C_x = G_x_1


# In[51]:


print("𝑟 = 𝐶 mod 𝑞")
r = C_x % size
print("𝑟 = %d" %(r))
print("𝑒 = 𝑚 mod 𝑞")
e = m % size
print("𝑒 = %d" %(e))
print("𝑠 = (𝑟𝑑 + 𝑘𝑒) mod 𝑞")
s = (𝑟*𝑑 + 𝑘*𝑒) % size
print("s = %d" %(s))


# In[53]:


print("Ответ (𝑥_𝑐, 𝑠) = (%d, %d)" %(C_x, s))


# In[ ]:


# -3 -8 0 5 10 4 5 16 11

