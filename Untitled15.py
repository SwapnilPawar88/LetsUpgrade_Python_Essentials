#!/usr/bin/env python
# coding: utf-8

# # Email - SwapnilsPawar330@gmail.com
# # Name - Swapnil Pawar
# 

# In[2]:


#find occurrance of the substring in the give String 
#What we Think we become ; we are python programmer


# In[26]:


str1 = "What we Think we become ; we are python programmer"
list1 =str1.split()
d = dict()
ind = dict()
for demo_str in list1:
    if demo_str in d:
        d[demo_str] = d[demo_str] + 1
        
    else:
        d[demo_str] = 1
        
print("Occurrance of words is")
for key in list(d.keys()):
    print(key , ":", d[key] )


# In[30]:


str1 = "Hi I Am Swapnil Pawar"
print(str1.islower())
print(str1.isupper())


# In[32]:


str2 = "hi i am swapnil pawar"
print(str2.islower())
print(str2.isupper())


# In[33]:


str3 = "THIS IS THE LETSUPGRADE PORTAL"
print(str3.islower())
print(str3.isupper())


# In[ ]:




