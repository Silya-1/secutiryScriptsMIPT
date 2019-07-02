
# coding: utf-8

# In[1]:


def gcd(a, b):
    while b:
        a, b=b, a%b
    return a
def phi(a):
    b=a-1
    c=0
    while b:
        if not gcd(a,b)-1:
            c+=1
        b-=1
    return c


# In[2]:


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


print("n e m")
n, e, m=  list(map(int, input().split(' ')))


# In[ ]:


d = bezout(phi(n), e)[1]
print("d= e^-1 mod phi(n)")
print("Phi(n) = %d" %(phi(n)))
print("d = %d" %(d))
s = m ** d % n
print("s = m ^ d mod n")
print(s)

