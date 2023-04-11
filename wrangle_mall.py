#!/usr/bin/env python
# coding: utf-8

# In[13]:


import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from env import user, password, host
import warnings
warnings.filterwarnings('ignore')

def acquire_mall():
    if os.path.exists('customers.csv'):
        return pd.read_csv('customers.csv', index_col=0)
    else:
        ''' Acquire data from mall_customers using env imports and rename columns'''

        url = f"mysql+pymysql://{user}:{password}@{host}/mall_customers"

        query = """
        SELECT *
        FROM customers
        """

        df = pd.read_sql(query, url)


        
        return df


# In[15]:


mall = acquire_mall()


# In[18]:


mall.shape


# In[20]:


mall.describe()


# In[21]:


type(mall)

