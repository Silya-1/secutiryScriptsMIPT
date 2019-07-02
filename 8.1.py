
# coding: utf-8

# In[1]:


import numpy as np


# In[6]:


print('Введите модуль схемы Блома p:')
p = int(input())
print('Введите идентефикатор Алисы (вектор (a,b)):')
Ax = int(input())
Ay = int(input())
print('Введите закрытый ключ Алисы (вектор (a,b)):')
AxClosed = int(input())
AyClosed = int(input())
print('Введите идентефикатор Боба (вектор (a,b)):')
Bx = int(input())
By = int(input())
print('Введите закрытый ключ Боба (вектор (a,b)):')
BxClosed = int(input())
ByClosed = int(input())

def minusOneMod(exp, fi):
    if fi == 0:
        print('Нельзя брать по модулю 0')
        exit(0)
    if exp == 1:
        return 1
    if exp == 0:
        return 0
    r = 0
    q = 0
    y  = [0, 1]
    mod = fi
    coef_first = 0
    coef_second = 1
    while r != 1:
        q = fi // exp
        r = fi % exp
        y.append(y[coef_first] - y[coef_second]*q)
        fi = exp
        exp = r
        coef_first += 1
        coef_second += 1
    y[coef_second] %= mod
    return y[coef_second]

print('Матрица доверенного центра имеет вид \n(a  b)\n(b  c)\n')
print('YA = ({}) = (a  b)({})\n     ({}) = (b  c)({})'.format(AxClosed, Ax, AyClosed, Ay))
print('YB = ({}) = (a  b)({})\n     ({}) = (b  c)({})'.format(BxClosed, Bx, ByClosed, By))
print('Откуда получаем систему уравнений')
print('{}a + {}b = {}'.format(Ax, Ay, AxClosed))
print('{}b + {}c = {}'.format(Ax, Ay, AyClosed))
print('{}a + {}b = {}'.format(Bx, By, BxClosed))
print('Решив систему уравнений получаем')
arr = [[Ax, Ay, -AxClosed],[Ax, Ay, -AyClosed],[Bx, By, -BxClosed]]
arr[2][1] *=  arr[0][0]
arr[2][2] *=  arr[0][0]
arr[2][1] += arr[2][0]*(-arr[0][1])
arr[2][2] += arr[2][0]*(-arr[0][2])
tChisl = pow(-arr[2][2], 1, p)
tZnam = minusOneMod(pow(arr[2][1], 1, p), p)
b = pow(tChisl*tZnam, 1, p)

arr = [[Ax, Ay, -AxClosed],[Ax, Ay, -AyClosed],[Bx, By, -BxClosed]]
tChisl = pow(-arr[0][2] - arr[0][1]*b, 1, p)
tZnam = minusOneMod(pow(arr[0][0], 1, p), p)
a = pow(tChisl*tZnam, 1, p)

arr = [[Ax, Ay, -AxClosed],[Ax, Ay, -AyClosed],[Bx, By, -BxClosed]]
tChisl = pow(-arr[1][2] - arr[1][0]*b, 1, p)
tZnam = minusOneMod(pow(arr[1][1], 1, p), p)
c = pow(tChisl*tZnam, 1, p)

print('a = {} / {} mod {} = {}*{} mod {} = {}'.format(-arr[0][2] - arr[0][1]*b, arr[0][0], p, tChisl, tZnam, p, a))
print('b = {} / {} mod {} = {}*{} mod {} = {}'.format(-arr[2][2], arr[2][1], p, tChisl,tZnam, p, b))
print('b = {} / {} mod {} = {}*{} mod {} = {}'.format(-arr[1][2] - arr[1][0]*b, arr[1][1], p, tChisl, tZnam, p, c))

print('Откуда получаем матрицу доверительного центра')
print('D = ({}  {})\n    ({}  {})'.format(a, b, b, c))

s = pow(AxClosed*Bx + AyClosed*By, 1, p)
print('Общий сеансовый ключ S = Sa = Sb = (закр А)(откр B) = ({},{})({},{})(<- 2ю вертикально) = {} mod {} = {}'
      .format(AxClosed, AyClosed, Bx, By, AxClosed*Bx + AyClosed*By, p, s))

