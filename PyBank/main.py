#!/usr/bin/env python
# coding: utf-8

# In[65]:


import pandas as pd


# In[66]:


csv_path = "Resources/budget_data.csv"


# In[67]:


pybank_df = pd.read_csv(csv_path, encoding="utf-8")

#pybank_df.head()


# In[68]:


print("Financial Analysis")


# In[69]:


print("------------------")


# In[70]:


months = pybank_df["Profit/Losses"].count()
#months


# In[71]:


print("Total Months: " + str(months))


# In[72]:


total = pybank_df["Profit/Losses"].sum()
#total


# In[73]:


print("Total:  $"+str(total))


# In[74]:


#average = pybank_df["Profit/Losses"].mean()


# In[75]:


#first_day = pybank_df[1:2]


# In[76]:


#first_day2 = pybank_df.iloc[0:2]
#first_day2 = pybank_df.loc[0:2]


# In[77]:


best_df = pybank_df.sort_values("Profit/Losses",ascending=False)
#best_df


# In[78]:


best_df = best_df.reset_index(drop=True)
#best_df


# In[79]:


best_day = best_df.loc[0,:]
#best_day


# In[80]:


print("Greatest Increase in Profits" + str(best_day))


# In[81]:


worst_day = best_df.loc[len(best_df)-1,:]
#worst_day


# In[82]:


print("Greaest Decrease in Profits" + str(worst_day))


# In[83]:


with open('readme.txt', 'w') as f:
    f.write('readme')


# In[ ]:




