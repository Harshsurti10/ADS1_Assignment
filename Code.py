#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


df = pd.read_csv('API_19_DS2_en_csv_v2_4700503.csv', header=[2])
print(df)


# In[4]:


df


# In[6]:


print(df.isnull().sum())


# In[7]:


df_yearnew=df.fillna(0)


# In[8]:


df_yearnew


# In[9]:


print(df_yearnew.columns)
print("The size of the data:", df_yearnew.size)
print("The shape of the data:", df_yearnew.shape)
print(df_yearnew.describe())


# In[11]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[13]:


sns.scatterplot(x="Country Name", y = "2018", data = df_yearnew)


# In[14]:


sns.stripplot(x="Country Code", y = "2020", data = df_yearnew)


# In[16]:


df_yearnew.corr()


# In[17]:


sns.heatmap(df_yearnew.corr(),annot=True)


# In[ ]:




