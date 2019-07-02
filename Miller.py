
# coding: utf-8

# In[49]:


def Miller(n, a):  
    res = []
    power = n-1
    print('Powers')
    while power % 2 == 0:
        print(power)
        res.append((a ** power) % n)
        power = power // 2
    print(power)
    res.append((a ** power) % n)
    return res


# In[50]:


print("n, a")
n, a=  list(map(int, input().split(' ')))
res = Miller(n, a)
print(res)
print(res[0] == 1 and res[-1] != -1 % n and -1 % n in res)

