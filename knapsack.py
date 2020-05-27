#!/usr/bin/env python
# coding: utf-8

# In[6]:


#tkaing values
n,W =  [int(x) for x in input().split()]


# In[7]:


#checking max_limits of knapsack
if W==0:http://localhost:8888/notebooks/knapsack.ipynb#
    print(0)
    quit()


# In[8]:


#getting values of value and weight of each item
lst = []
for i in range(n):
    v,w = [int(j) for j in input().split()]
    if v==0:
        continue
    lst.append((v,w))


# In[9]:


#sorting the lst with respect to v/w value
lst.sort(key = lambda x: x[0]/x[1] , reverse=True)


# In[10]:


total_value = 0


# In[11]:



for v,w in lst:
    if W==0:  #checking if the limit has reached
        #print(total_value)
        quit()
    amt = min(w,W)               #taking the minimum of W, i.e Total weight and w,which represent weight of object
    total_value+=amt*v/w         # adding the value to the list///
    W-=amt                       #subtracting the amount !
    


# In[1]:


print(total_value)
    
    


# In[ ]:




