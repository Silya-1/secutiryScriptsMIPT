
# coding: utf-8

# In[4]:


import numpy as np
from fractions import Fraction


# In[10]:


def H1(p1, p2):
    return -p1 * np.log2(p1) - p2 * np.log2(p2)

print('px1 px2 pz1 pz2')
px1, px2, pz1, pz2 =  list(map(float,list(map(Fraction, input().split(' ')))))
print("p(y1) =  p(x1) * p(z1) + p(x2) * p(z2) = %f" %(px1 * pz1 + px2 * pz2))
print("p(y2) = 1 - p(y1) = %f" % (1 - px1 * pz1 - px2 * pz2))
Ix1 = - np.log2(float(px1))
Ix2 = -np.log2(float(px2))
print('a) Ix1 = ', Ix1, 'Ix2 = ', Ix2)
Hx = H1(px1, px2)
Hz = H1(pz1, pz2)
py1 = px1 * pz1 + px2 * pz2
py2 = 1 - py1
Hy = H1(py1, py2)
print('b) Hx = ', Hx, 'Hz = ', Hz, 'Hy = ', Hy)
print('c) I(x, z) = 0 (I(X;Y)=H(X)-H(X|Y)=H(X)-H(X)=0)')
print('d) I(x, y) = H(Y) - H(Z) = ', Hy - Hz)
print('e) I(y, z) = H(Y) - H(X) = ', Hy - Hx)
print('f) P(x1 | y1) = P(y1|x1) * P(x1) / P(y1) = P(z1) * P(x1) / P(y1) = ', pz1 * px1 / py1, 'P(x1 | y2) = P(y2|x1) * P(x1) / P(y2) = P(z2) * P(x1) / P(y2) =  ', pz2 * px1 / py2)
print('g) P(x2 | y1) = P(y1|x2) * P(x2) / P(y1) = P(z2) * P(x2) / P(y1) = ', pz2 * px2 / py1, 'P(x2 | y2) = P(y2|x2) * P(x2) / P(y2) = P(z1) * P(x2) / P(y2) =  ', pz1 * px2 / py2)

print("система не надежна тк апостериорные вероятности не равны")
print("неоходимо сделать одинаковые вероятности для ключа(z)")
print("Считаем теперь p(z1) = p(z2) = 1/2, пересчитаем вероятности")
print("p(y1) =  p(x1) * p(z1) + p(x2) * p(z2) = %f" %(px1 * 1/2 + px2 * 1/2))
print("p(y2) = 1 - p(y1) = %f" % (1 - px1 * 1/2 - px2 * 1/2))
py1 = px1 * 1/2 + px2 * 1/2
py2 = 1 - py1
pz1 = pz2 = 1/2
print('f) P(x1 | y1) = P(y1|x1) * P(x1) / P(y1) = P(z1) * P(x1) / P(y1) = ', pz1 * px1 / py1, 'P(x1 | y2) = P(y2|x1) * P(x1) / P(y2) = P(z2) * P(x1) / P(y2) =  ', pz2 * px1 / py2)
print('g) P(x2 | y1) = P(y1|x2) * P(x2) / P(y1) = P(z2) * P(x2) / P(y1) = ', pz2 * px2 / py1, 'P(x2 | y2) = P(y2|x2) * P(x2) / P(y2) = P(z1) * P(x2) / P(y2) =  ', pz1 * px2 / py2)


