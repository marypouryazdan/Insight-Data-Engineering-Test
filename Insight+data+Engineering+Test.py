
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
data = pd.read_csv('de_cc_data.txt')


# In[2]:

data.head()


# In[6]:

data.tail(30)


# In[ ]:




# In[ ]:


 


# In[18]:

data.id.value_counts()


# In[20]:

data.drug_name.value_counts()


# In[21]:

data.shape


# In[22]:

data.dtypes


# In[25]:

data['drug_cost'].describe()


# In[26]:

data['id'].describe()


# In[27]:

data.describe()


# In[28]:

data.sort_values(by='drug_name', ascending=False)


# In[29]:

data.head()


# # Groupby
# 

# In[19]:


res=data.groupby(['drug_name'])['id','drug_cost'].agg({'id':pd.Series.nunique,'drug_cost':sum})


# In[20]:

res.sort_values(by=['drug_cost'],ascending=False).head()


# In[21]:

res1=res.reset_index()
res1.head()


# # Output Preparation

# In[26]:

res1.rename(columns={'drug_name':'drug_name','id':'num_prescriber','drug_cost':'total_cost'},inplace=True)
res1.head()


# # Sorting the list based on Drug cost and name in a descending order

# In[30]:

res1=res1.sort_values(by=['total_cost','drug_name'],ascending=[False,False])
res1.head()


# In[33]:

res1.to_csv("Output.csv")


# In[ ]:



