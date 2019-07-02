
# coding: utf-8

# In[9]:


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


x1,  mod=  list(map(float, input().split(' ')))
dif = bezout(x1, mod)[1]


# In[8]:


get_ipython().system('jupyter nbconvert --to script euclid.ipynb')

