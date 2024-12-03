#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[2]:


x = np.linspace(0,10,100)
y = np.sin(x)
z = np.cos(x)


# In[3]:


print(x)


# In[4]:


print(y)


# In[5]:


# sine wave
plt.plot(x,y)
plt.show()


# In[6]:


# adding titles ,x-axis & y-axis Labels
plt.plot(x,y)
plt.xlabel('angle')
plt.ylabel('sine value')
plt.title('sine wave')
plt.show()


# In[7]:


# parabola
x =np.linspace(-10,10,20)
y =x**2
plt.plot(x,y)
plt.show()


# In[8]:


plt.plot(x,y,'r+')
plt.show()


# In[9]:


plt.plot(x,y,'g.')
plt.show()


# In[10]:


plt.plot(x,y,'rx')
plt.show()


# In[11]:


x = np.linspace(-5,5,50)
plt.plot(x, np.sin(x), 'g-')
plt.plot(x, np.cos(x), 'r--')
plt.show()


# ### Bar plot

# In[12]:


fig = plt.figure()
ax  = fig.add_axes([0,0,1,1])
languages = ['English', 'French', 'Spanish', 'Latin','German']
people = [100, 50, 150, 40, 70]
ax.bar(languages, people)
plt.xlabel('LANGUAGES')
plt.ylabel('PEOPLE')
plt.show()


# ###  Pie chart

# In[13]:


fig1 = plt.figure()
ax = fig1.add_axes([0,0,1,1])
langauges = ["English","French","Spanich", "Latin", "German"]
people = [100,50,150,40,70]
ax.pie(people,labels=languages, autopct='%1.1f')
plt.show()


# ### Scatter Plot

# In[14]:


x = np.linspace(0,10,30)
y = np.sin(x)
z = np.cos(x)
fig2 = plt.figure()
ax = fig2.add_axes([0,0,1,1])
ax.scatter(x,y,color='g')
ax.scatter(x,z,color='b')
plt.show()


# ### 3D Scatter plot
# 

# In[15]:


fig3 = plt.figure()
ax = plt.axes(projection='3d')
z = 20* np.random.random(100)
x = np.sin(z)
y = np.cos(z)
ax.scatter(x,y,z, c=z,cmap='Blues')
plt.show()


# In[ ]:




