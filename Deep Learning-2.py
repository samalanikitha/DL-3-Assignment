#!/usr/bin/env python
# coding: utf-8

# In[15]:


#3
#Plot the following functions: h11(x), h12(x) and h21(x) for x ∈ (−1, 1)
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D
plt.rcParams.update({"font.size": 15})
x = np.arange(-1,1,0.001)
h11 = 1/(1+np.exp(-(500*x+30)))
h12 = 1/(1+np.exp(-(500*x-30)))
h21 = h11 - h12
plt.ylabel("h11(x)")
plt.xlabel("x")
plt.plot(x,h11)

plt.show()


# In[16]:


plt.ylabel("h12(x)")
plt.xlabel("x")
plt.plot(x,h12)
plt.show()


# In[17]:


plt.ylabel("h21(x)")
plt.xlabel("x")
plt.plot(x,h21)
plt.show()


# In[18]:


#3b
#Plot the following functions: h11(x1, x2), h12(x1, x2), h13(x1, x2), h14(x1, x2), h21(x1, x2),
#h22(x1, x2), h31(x1, x2) and f(x1, x2) for x1 ∈ (−5, 5) and x2 ∈ (−5, 5)
def h11(x1,x2):
    return 1/(1 + np.exp(-(x1 + 50*x2 + 100)))

def h12(x1,x2):
    return 1/(1 + np.exp(-(x1 + 50*x2 - 100)))

def h13(x1,x2):
    return 1/(1 + np.exp(-(50*x1 + x2 + 100)))

def h14(x1,x2):
    return 1/(1 + np.exp(-(50*x1 + x2 - 100)))

def h21(x1,x2):
    return h11(x1,x2) - h12(x1,x2)

def h22(x1,x2):
    return h13(x1,x2) - h14(x1,x2)

def h31(x1,x2):
    return h21(x1,x2) + h22(x1,x2)

def f(x1,x2):
    return 1/(1 + np.exp(-(100*h31(x1,x2) - 200)))


# In[19]:


x1 = np.arange(-5,5,0.01)
x2 = np.arange(-5,5,0.01)
X,Y = np.meshgrid(x1, x2)


# In[25]:


Z = h11(X, Y)
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('h11');


# In[21]:


Z = h12(X, Y)
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z)
ax.set_xlabel('x_1')
ax.set_ylabel('x_2')
ax.set_zlabel('h12');


# In[22]:


Z = h13(X, Y)
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('h13');


# In[23]:


Z = h14(X, Y)
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('h14');

Z = h21(X, Y)
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('h21');


# In[24]:


Z = h22(X, Y)
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('h22');

Z = h31(X, Y)
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('h31');


# In[26]:


Z = f(X, Y)
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('f');


# In[ ]:




