
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[127]:


def bezout(a, b):
    print('EUCLID')
    x, xx, y, yy = 1, 0, 0, 1
    print("a = %d, b = %d" %(a, b))
    print("y_-2 = %d  y_-1 = %d" %(xx,  x))
    print("")
    i = -1
    r_prev = a
    while b:
        q = a // b
        a, b = b, a % b
        #print("a = b, b = a - b * q")
        print("r_%d = q_%d*r_%d + r_%d"%(i-1, i+1, i, i+1))
        print("%d = %d * %d + %d" %(r_prev,q, a, b))
        x, xx = xx, x - xx*q
        y, yy = yy, y - yy*q
        print("y_%d = %d" %(i, y))
        i+=1
        print("")
        r_prev = a
    print("EUCLID END")
    return (x, y, a)


# In[ ]:


print('X_1 X_2 X_3 mod')
x1, x2, x3, mod=  list(map(float, input().split(' ')))
print("%d = a * %d + m" %(x2, x1))
print("%d = a * %d + m" %(x3, x2))

dif_2 = (x3-x2) % mod
dif_1 = (x2-x1) % mod
print("X_2 - X_1 = %d" %(dif_1))
print("%d = a*%d" %(x3-x2, x2-x1))
print("%d ^-1 = " % (dif_1))
dif = bezout(mod, dif_1)[1]
print("%d ^-1 = %d" %(dif_1, dif))
a = dif *dif_2
print("a = %d" %(a))
a =  a % mod
print("a = %d" %(a))
m = (x3 - a * x2) % mod
print("m = %d" %(m))

print("X_4= X_3 * %d + %d" %(a, m))
x4 = (x3 * a + m) % mod
print("X_4 = %d" %(x4))


print("X_5= X_4 * %d + %d" %(a, m))
x5 = (x4 * a + m) % mod
print("X_5 = %d" %(x5))

