
# coding: utf-8

# In[25]:


def pow_h(base, degree, module):
    binary = "{0:b}".format(degree)
#     print("Возводим число %d в %d степень по модулю %d"%(base,degree,module))

    if len(binary) != 8:
        binary = '0' * (8 - len(binary)) + binary

#     print("Двоичное представление степени - " + binary)
    s = 1

    counter = 1
    for i in binary:
        temp = (s ** 2) * (base ** int(i)) % module
#         print("S%d = (%d)^2 * %d^%d  = %d" % (counter, s, base, int(i), temp))
        counter += 1
        s = temp
#     print("Ответ - %d"%s)
    return s


# In[26]:


def Miller(n, a):  
    res = []
    power = n-1
    print('n - 1 = %d' %(power))
    print('Пока n - 1 делится на 2^i мы считаем a ^((n-1)/2^i) где i=1..')
    i = 0
    while power % 2 == 0:
        print("(n - 1)/ 2^%d =  %d" %(i, power))
        print("Найдем a ^ (n - 1)/ 2^%d" %(i))
        var = pow_h(a, power, n)
        print("a ^ (n - 1)/ 2^%d = %d" %(i, var))
        res.append(var)
        i += 1
        power = power // 2
    print("(n - 1)/ 2^%d =  %d" %(i, power))
    print("Найдем a ^ (n - 1)/ 2^%d" %(i))
    var = pow_h(a, power, n)
    print("a ^ (n - 1)/ 2^%d = %d" %(i, var))
    res.append(var)
    return res


# In[27]:


print("Введите свидетель и проверяемое число")
print("x1 , n")
a , n=  list(map(int, input().split(' ')))
res = Miller(n, a)
print("-1 mod n = %d" %(-1 %n))
print("Если первое найденное число равно 1 и последнее найденное не равно %d и %d есть среди найденных чисел то a свидетель простоты n" % (-1%n , -1%n))
print("Наши результаты")
print(res)
print(res[0] == 1 and res[-1] != -1 % n and -1 % n in res)

