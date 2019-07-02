
# coding: utf-8

# In[20]:


import numpy as np


# In[29]:


x1,  n=  list(map(int, input().split(' ')))


# In[30]:


if (int((x1 ** n) % n) == x1):
    print("YES")
else:
    print("NO")


# In[32]:


get_ipython().system('jupyter nbconvert --to script ferma.ipynb')

