#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D
plt.rcParams.update({"font.size": 15})
x = np.arange(-1,1,0.001)
h11 = 1/(1+np.exp(-(500*x+30))) 
h12 = 1/(1+np.exp(-(500*x-30))) 
h21 = h11 - h12

plt.figure(figsize = (10,10))

plt.subplot(311)
plt.ylabel("$h_{11}(x)$")
plt.title("Part (a)")
plt.plot(x,h11)

plt.subplot(312)
plt.ylabel("$h_{12}(x)$")
plt.plot(x,h12,"g-")

plt.subplot(313) 
plt.ylabel("$h_{21}(x)$")
plt.xlabel("$x$") 
plt.plot(x,h21,"r-")
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




