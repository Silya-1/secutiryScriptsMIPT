
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


def modifyArr(arr):
    arr[1][0] *= arr[0][1]
    arr[1][2] *= arr[0][1]
    arr[1][0] -= arr[0][0] * arr[1][1]
    arr[1][2] -= arr[0][2] * arr[1][1]
    arr[1][1] = 0
    return arr

#exp^-1 mod fi
def minusOneMod(exp, fi):
    #print('---промежуточный расчет {} ^-1 mod {} ---'.format(exp, fi))
    if fi == 0:
        #print('Нельзя брать по модулю 0')
        exit(0)
    if exp == 1:
        #print('1 mod {} = 1'.format(fi))
        #print('---промежуточный расчет закончен---')
        return 1
    if exp == 0:
        return 0
    r = 0
    g = 0
    y  = [0, 1]
    mod = fi
    expAns = exp
    coef_first = 0
    coef_second = 1

    #print('Распишем в таблице: (Элементы в () можно не писать)')
    #print('(Запишем y в столбце справа:)')
    #print('y[-2] =', y[0])
    #print('y[-1] =', y[1])

    while r != 1:
        g = fi // exp
        r = fi % exp
        y.append(y[coef_first] - y[coef_second]*g)
        #print('{} = (g{}){}*{} + r({}){} ,посчитаем y({}) = y({}){} - y({}){}*g({}){} = {}'
        #      .format(fi, coef_first, g, exp, coef_first, r, coef_first, coef_first - 2,
        #              y[coef_first], coef_second - 2, y[coef_second], coef_first, g, y[coef_second + 1]))
        fi = exp
        exp = r
        coef_first += 1
        coef_second += 1
    y[coef_second] %= mod
    #print('Ответ {}^-1 mod {} = {}'.format(expAns, mod, y[coef_second]))
    return y[coef_second]


# In[4]:


print('Введите модуль p:')
p = int(input())
print('Введите количество следов:')
n = int(input())
print('Введите количество цифр в следе:')
a = int(input())
print('Введите любые {} следа (через enter):'.format(a - 1))

arr = [[0] * a for i in range(a - 1)]
for i in range(0, a - 1):
    for j in range (0, a):
        arr[i][j] = int(input())

print('Берем 2 любые суперплоскости из следов (все вычисления в F{}):'.format(a - 1, p))

for i in range(0, a - 1):
    for j in range (0, a):
        if j != a - 1:
            print('{} * x{} + '.format(arr[i][j], j + 1), end = '')
        if j == a - 1:
            print(arr[i][j], end='')
    print(' = 0')

print('Выразив коэффициенты получаем:')

arr = modifyArr(arr)
t = pow(-arr[1][2], 1, p)
r = minusOneMod(pow(arr[1][0], 1, p), p)
x = pow(t*r, 1, p)
print('M = x = ({}mod {} * {}^-1 mod{}) mod {} = {} * {} mod {} = {}'
      .format(-arr[1][2], p, pow(arr[1][0], 1, p), p, p, t, r, p, x))

e = pow(-(x*arr[0][0] + arr[0][2]), 1, p)
g = minusOneMod(pow(arr[0][1], 1, p), p)
y = pow(e*g, 1, p)

print('y = ({}mod {} * {}^-1 mod{}) mod {} = {} * {} mod {} = {}'
      .format(-(x*arr[0][0] + arr[0][2]), p, pow(arr[0][1], 1, p), p, p, e, g, p, y))

