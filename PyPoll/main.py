#!/usr/bin/env python
# coding: utf-8

# In[137]:


import pandas as pd
import os


# In[138]:


csv_path = "Resources/election_data.csv"


# In[139]:


pypoll_df = pd.read_csv(csv_path, encoding="utf-8")

#pypoll_df.head()


# In[104]:


print("Election Results")


# In[105]:


print("----------------")


# In[106]:


total = len(pypoll_df)
print("Total Votes: "+ str(total))


# In[107]:


print("----------------")


# In[108]:


#candidates = pypoll_df.Candidate.unique()
#print(candidates)


# In[109]:


#pypoll_df["Candidate"].value_counts()


# In[110]:


#pypoll_df.sort_values("Candidate").head()


# In[111]:


stockham_df=pd.DataFrame(pypoll_df.loc[pypoll_df["Candidate"]=="Charles Casper Stockham",:])


# In[112]:


#stockham_df.info()


# In[113]:


#stockham_count = stockham_df["Ballot ID"]
#stockham_count.count()


# In[114]:


stock_count = stockham_count.count()


# In[115]:


stockham_perc = stockham_count.count() / total * 100


# In[116]:


#stockham_perc


# In[117]:


stockham_perc2 = round(stockham_perc,3)


# In[118]:


#stockham_perc2


# In[119]:


print("Charles Casper Stockham:  " + str(stockham_perc2) + "%  "  + (str(stock_count)))


# In[120]:


degette_df=pd.DataFrame(pypoll_df.loc[pypoll_df["Candidate"]=="Diana DeGette",:])


# In[121]:


#degette_df.head()


# In[122]:


degette_count = degette_df["Ballot ID"].count()


# In[123]:


#degette_count


# In[124]:


degette_perc = degette_count / total * 100


# In[125]:


degette_perc2 = round(degette_perc,3)


# In[126]:


print("Diana DeGette:  " + str(degette_perc2) + "%  "  + (str(degette_count)))


# In[127]:


doane_df=pd.DataFrame(pypoll_df.loc[pypoll_df["Candidate"]=="Raymon Anthony Doane",:])


# In[128]:


#doane_df.head()


# In[129]:


doane_count = doane_df["Ballot ID"].count()


# In[130]:


#doane_count


# In[131]:


doane_perc = doane_count / total * 100


# In[132]:


doane_perc2 = round(doane_perc,3)


# In[133]:


print("Raymon Anthony Doane:  " + str(doane_perc2) + "%  "  + (str(doane_count)))


# In[134]:


print("----------------")


# In[135]:


if (doane_count > degette_count) & (doane_count > stock_count):
    print("Winner: Raymon Anthony Doane")
elif (stock_count > degette_count) & (stock_count > degette_count):
    print("Winner: Charles Casper Stockham")
else:
    print("Winner: Diane Degette")


# In[136]:


print("----------------")

