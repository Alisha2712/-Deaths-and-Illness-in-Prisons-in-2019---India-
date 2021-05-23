#!/usr/bin/env python
# coding: utf-8

# In[1]:


#As the data is in PDF format, so converting it to csv using CAMELOT or TABULA-PY library.

# Camelot is a Python library and a command-line tool that makes it easy for 
# anyone to extract data tables trapped inside PDF files.

#Whereas Tabula-py is a simple Python wrapper of tabula-java, which can read tables in a PDF. 
#It enables you to convert a PDF file into a CSV, TSV, JSON or even a pandas DataFrame.

# Extracting PDF Tables using Camelot

# installing Camelot
#conda install -c conda-forge camelot-py

# importing
import camelot


# In[15]:


data = camelot.read_pdf(r'C:\Users\Jayant Gera\Desktop\datascience\Deaths\total deaths.pdf', flavor='stream', pages='all')
data

# we will get a TableList object called as data, which is a list of Table object. 
#We can fetch everything we need from this object.
# From the output below, we can see that the tables object has only one table, since n=1.


# In[16]:


# we can access the shape of the object using the index = 0. 
# By default, it uses LATTICE technique. 
data[0]


# In[17]:


# printing the parsing report
print(data[0].parsing_report)


# In[68]:


# Woah! The accuracy is splendid and there is little whitespace, meaning the table was most likely extracted correctly.


# In[69]:


# importing pandas and numpy
import pandas as pd
import numpy as np


# In[100]:


total_data = data[0].df
total_data.head(8)


# In[101]:


heading = total_data.iloc[0]+' ' + total_data.iloc[1]+' ' + total_data.iloc[2]+' ' + total_data.iloc[3]
total_data = total_data.rename(columns=heading).drop(total_data.index[0] )
total_data.head()


# In[102]:


total_data = total_data.drop(labels=[1,2,3,4,5,35,43,44,45], axis=0)
total_data =total_data.drop(columns=total_data.columns[0])
total_data.head()


# In[95]:


total_data.columns


# In[103]:


total_data = total_data.rename(columns={'Total Deaths  (Col.3 + Col.4 + ': 'Total Deaths'})
total_data.head()


# In[97]:


total_data.replace(to_replace ='-', value ='0')
total_data.head()


# In[104]:


total_data.shape


# In[105]:


total_data


# In[108]:


total_data.to_csv('total_data.csv')


# In[109]:


pd.read_csv('total_data.csv')


# In[ ]:





# In[ ]:




