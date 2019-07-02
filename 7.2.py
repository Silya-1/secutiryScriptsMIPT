
# coding: utf-8

# In[1]:


import numpy


# In[17]:


print("Введите коэффициенты эллиптической кривой y= x^3 +a*x + b и модуль")
print("a b n")
a,b,n =  list(map(int, input().split(' ')))


# In[28]:


x =[i for i in range(n)]
x_2 = [(i * i) % n for i in range(n)]
y_2 = [((i**3)%n + a*i + b) %n for i in range(n)]
res_1 = {}
total_res = {}
count = 0


# In[29]:


for i in range(len(x_2)):
    res_1[i] = "-"
    total_res[i] = "-"
    for j in range(len(x_2)):
        if(x_2[j] == y_2[i]):
            count += 1
            if(res_1[i] == "-"):
                res_1[i] = [x[j]]
                total_res[i] = [([x[i], x[j]])]
            else:
                res_1[i].append(x[j])
                total_res[i].append(([x[i], x[j]]))


# In[50]:


print("x" ,end="\t\t|")
print("x^2" ,end="\t\t|")
print("y^2" ,end="\t\t|")
print("y_1, y_2",end='\t\t')
print("Точки")
for i in range(len(x)):
    print(x[i] ,end="\t\t|")
    print(x_2[i] ,end="\t\t|")
    print(y_2[i] ,end="\t\t|")
    print(res_1[i] ,end="\t\t|")
    print(total_res[i])


# In[85]:


print("Размер группы точек: = %d"%(count + 1))
print("Точки: = " +" O, " + str(list(map(str,list(filter(lambda x:  x != "-",total_res.values()))))))


# In[91]:


string = ''
for x in list(map(str,list(filter(lambda x:  x != "-",total_res.values())))):
    string = string + x + ","

