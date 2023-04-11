#!/usr/bin/env python
# coding: utf-8

# In[32]:


import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from env import user, password, host
import warnings
warnings.filterwarnings('ignore')

def acquire_zillow():
    if os.path.exists('zillow_2017.csv'):
        return pd.read_csv('zillow_2017.csv', index_col=0)
    else:
        ''' Acquire data from Zillow using env imports and rename columns'''

        url = f"mysql+pymysql://{user}:{password}@{host}/zillow"

        query = """
        SELECT bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, taxamount, fips
        FROM properties_2017
        LEFT JOIN propertylandusetype USING(propertylandusetypeid)
        WHERE propertylandusedesc IN ("Single Family Residential",                       
                                      "Inferred Single Family Residential")"""

        df = pd.read_sql(query, url)


        df = df.rename(columns = {'bedroomcnt':'bedrooms', 
                                  'bathroomcnt':'bathrooms', 
                                  'calculatedfinishedsquarefeet':'area',
                                  'taxvaluedollarcnt':'tax_value', 
                                  'yearbuilt':'year_built',})
        return df


# In[42]:


zillow = acquire_zillow().reset_index()


# In[43]:


zillow


# In[44]:


type(zillow)


# In[45]:


zillow.shape


# In[46]:


zillow.describe()


# In[57]:


def remove_columns(df, cols_to_remove):  
    df = df.drop(columns=cols_to_remove)
    return df


# In[70]:


def handle_missing_values(df, prop_required_column = .5, prop_required_row = .75):
    threshold = int(round(prop_required_column*len(df.index),0))
    df.dropna(axis=1, thresh=threshold, inplace=True)
    threshold = int(round(prop_required_row*len(df.columns),0))
    df.dropna(axis=0, thresh=threshold, inplace=True)
    return df


# In[71]:


handle_missing_values(zillow)


# In[72]:


def data_prep(df, cols_to_remove=[], prop_required_column=.5, prop_required_row=.75):
    df = remove_columns(df, cols_to_remove)
    df = handle_missing_values(df, prop_required_column, prop_required_row)
    return df


# In[79]:


data_prep(df)


# In[ ]:





# In[ ]:





# In[ ]:




