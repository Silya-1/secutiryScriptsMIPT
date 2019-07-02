
# coding: utf-8

# In[15]:


import numpy as np


# In[20]:


def pow_h(base, degree, module):
    binary = "{0:b}".format(degree)
    print("Возводим число %d в %d степень по модулю %d"%(base,degree,module))

    if len(binary) != 8:
        binary = '0' * (8 - len(binary)) + binary

    print("Двоичное представление степени - " + binary)
    s = 1

    counter = 1
    for i in binary:
        temp = (s ** 2) * (base ** int(i)) % module
        print("S%d = (%d)^2 * %d^%d  = %d" % (counter, s, base, int(i), temp))
        counter += 1
        s = temp
    print("Ответ - %d"%s)
    return s



# In[ ]:


print("Введите 1 кандита и число чью простоту проверяем")
print("x1 n")
x1, n=  list(map(int, input().split(' ')))
print("Проверяем первое число (x1)")
print("Если x1^n mod n = x1 то число свидетель простоты")
var = pow_h(x1, n, n)
print("x1^n mod n = %d" %(var))
if (var == x1):
    print("ДА")
else:
    print("НЕТ")

