
# coding: utf-8

# In[4]:


#перевод из 10 в 2 систему исчисления (без поворота bin = bin[::-1]) т.к. схема справа налево)
def DecToBin(a):
    t = a
    bin = []
    print('Перведем число',a,'в двоичный вид:')
    while a != 0:
        if a % 2 == 0:
            bin.append(0)
            print(a, '0')
            a /= 2
        if a % 2 == 1:
            print(a, '1')
            bin.append(1)
            a //= 2
    bin = bin[::-1]
    print(t,'(x10) = (x2) ',bin)
    bin = bin[::-1]
    return bin

#быстрое возведение в степень методом справа налево
def FastExponentiation(msg, fi, key):
    bin = DecToBin(fi)
    i = 0
    d = 1
    print('Используем схему справа налево:')
    while i < len(bin):
        print('Шаг:', i + 1)
        if bin[i] == 1:
            print('d ={}*{}mod{}='.format(d, msg, key), end=' ')
            d *= msg
            d %= key
            print(d)
        print('t ={}^2 mod{}='.format(msg, key), end = ' ')
        msg *= msg
        msg %= key
        print(msg)
        i += 1
    return d


# In[7]:


print('является ли число а (введите):')
a = int(input())
print('свидетелем простоты n (введите) по миллеру:')
n = int(input())

print('-------------------------------------------\nРешение:')
print('Вычислим степени, в которые нужно будет возводить потенциальные свидетели простоты:')
print('Формула для нахождения: (n-1)/ 2^t')
i = 0
l = []
while float(((n - 1)/ 2 ** i) % 2) != 1.0:
    l.append(int((((n - 1)/ 2 ** i))))
    i += 1
l.append(int((((n - 1)/ 2 ** i))))
l = l[::-1]
for i in l:
    print(i, sep='', end=' ')

print('\nВоспользуемся быстрым возведением в степень {}^{} mod {}'.format(a, l[0], n))
FastExponentiation(a, l[0], n)

i = 0
PS = []
temp = pow(a, l[0] , n)

for i,item in enumerate(l):
    print('{}^{} mod {} = {}'.format(a, item, n, pow(a, item, n)), end = '')
    if i == 0:
        print('')
    if i > 0:
        print(' = {} ^2 mod {}'.format(temp, n))
    temp = pow(a, item, n)
    PS.append(temp)
    i += 1

MillerTrigger = False
NotOne = True

for i,item in enumerate(PS):
    if item == n - 1 and PS[i + 1] == 1 and PS[len(PS) - 1]:
        MillerTrigger = True
        print('Т.к. n - 1 элемент находится перед первой единицей, и последний элемент 1, то', a, 'является свидетелем', n, 'по Миллеру')
    if item != 1:
        NotOne = False

if NotOne == True:
    MillerTrigger = True
    print('Т.к. все элементы 1, то {} является свидетелем {} по Миллеру'.format(a, n))
if MillerTrigger == False:
    print('Условия простоты по Миллеру не выполнены')


# In[ ]:


get_ipython().system('jupyter nbconvert --to script M.ipynb')

