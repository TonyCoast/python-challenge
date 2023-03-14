#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os
import csv

pybank_csv = 'C:/Users/ANTHONY/Desktop/PythonActivities/budget_data.csv'
    
total_months = []
net_pl = []
changes_pl = []
greatest_increase = []
greatest_decrease = []


# In[5]:


with open(pybank_csv) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    print(csvreader)
    for row in csvreader:
        print(row)


# In[6]:


print(len(csvreader))


# In[ ]:




