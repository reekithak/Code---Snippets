#!/usr/bin/env python
# coding: utf-8

# In[23]:


n  = int(input())


# In[24]:


if n==1:
    print(1)
    print(1)
    quit()
W=n                   
prices = []
for i in range(1,n):
    if W>2*i:                                  #since multiple of 2 is the minimum we can look into
        prices.append(i)
        W-=i
    else:
        prices.append(W)
        break
print(len(prices))
print(' '.join([str(i) for i in prices]))


# In[ ]:




