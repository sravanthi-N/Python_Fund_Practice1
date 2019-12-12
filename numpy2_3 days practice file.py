#!/usr/bin/env python
# coding: utf-8

# In[1]:


# creating empty array

import numpy as np

array_empty=np.empty((2,3))
array_empty


# In[3]:


# Creating idetity array

array_eye=np.eye(4)
array_eye


# In[13]:


# using arange 
array_of_events1= np.arange(2,20,2)    # for even numbers
#print(array_of_events1)
array_of_events1

array_of_events2=np.arange(3,20,2)    # for odd numbers
#print(array_of_events2)
array_of_events2


# In[14]:


# creating 2-Dimensional array

array_2d=np.array([(1,2,3),(4,5,6)])
array_2d


# In[15]:


array_2d.shape   # to know the shape of array


# In[18]:


array_nd=np.arange(6)
array_nd


# In[21]:


array_nd.shape


# In[22]:


# want to change the shape of array_nd
array_nd=np.arange(6).reshape(2,3)
array_nd
                            


# In[23]:


# trying another possible shape of array_nd

array_nd=np.arange(6).reshape(3,2)
array_nd


# In[24]:


# creating ones array with the same as array_nd using 'like' attribute
array_ones=np.ones_like(array_nd)
array_ones


# In[25]:


#Printing the array

print(array_nd)


# In[26]:


# Basic arthmetic operations
a=np.array([10,10,10])
b=np.array([20,20,20])
print(a+b)


# In[27]:


print(a-b)


# In[28]:


print(a*b)


# In[29]:


print(b/a)


# In[30]:


# comparision operators

a>35


# In[31]:


b<20


# In[32]:


a.shape


# In[34]:


c=np.array([5,5])
print(c)


# In[36]:


# Universal functions in numpy

angles= np.array([0,30,45,60,90])

#converting angles into radiance using formula

radiance=angles*np.pi/180
radiance


# In[37]:


# converting angles to radiances using inbuild formula
radiance=np.radians(angles)
radiance


# In[ ]:




