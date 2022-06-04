#!/usr/bin/env python
# coding: utf-8

# In[1]:


from urllib.request import urlretrieve

Top_500_companies = 'https://datahub.io/core/s-and-p-500-companies/r/0.html.csv'


# In[2]:


urlretrieve(Top_500_companies, 'S&P_500_Financials')


# In[3]:


Top_500_financials  = 'https://datahub.io/core/s-and-p-500-companies-financials/r/1.html.csv'

urlretrieve(Top_500_financials, 'Financials')


# In[4]:


import pandas as pd


# In[5]:


df1 = pd.read_csv('Financials')
df1


# In[6]:


df1.drop(columns = ['SEC Filings'],inplace = True)


# In[7]:


df1.rename({'52 Week Low':'Week_52_low',
            '52 Week High':'Week_52_high',
            'Earnings/Share':'Earning_Share',
            'Dividend Yield':'Dividend_Yield',
           'Market Cap':'Market_cap',
           'Price/Sales':'Price_Sales',
           'Price/Book':'Price_Book',
           'Price/Earnings':'Price_Earnings'}
           ,axis = 1, inplace = True)


# In[8]:


df1


# In[9]:


df1.dropna(inplace = True)


# In[10]:


df1.shape


# In[11]:


df1.isnull().sum()


# In[12]:


df1.sort_values('Price_Sales',ascending = False).head(10)


# The Real Estate sector had the highest average Sales out of all the sectors followed by Information Technology, with TeleCommunication Services being the least.

# In[13]:


df1['Sector'].nunique()


# In[14]:


df1['Symbol'].nunique()


# In[15]:


df1_sector = df1.groupby('Sector')[['Price_Earnings', 'Price', 'Market_cap','Price_Sales']].mean()
df1_sector


# In[16]:


df1_pb_value = df1.groupby('Sector')[['Price_Book']].mean().sort_values('Price_Book',ascending = False)
df1_pb_value

Consumer Staples has the highest Price to Book ratio and the Utilities has the lowest. It is clearly indicates that the daily esssentials are the most sought out products in the market. There is a hugh gap between the PB ratio of Consumer Staples(essential items) to Consumer Discretionary(non-essentials but desirable)
# In[17]:


df1_Sales_value = df1.groupby('Sector')[['Price_Sales']].mean().sort_values('Price_Sales',ascending = False)
df1_Sales_value


# The real-estate had the highest average sales and Telecommunications Services the lowest.
# By the above we can conclude that the Real estate prices have gone up the highest and probably will continue to go up in the times to come.

# In[18]:


df1.describe()


# In[19]:


df1[df1.Price > 1000].sort_values('Market_cap',ascending=False)

## There are 4 top 500 companies whose stock price is over 1000 dollars, namely

Priceline.com Inc (PCLN) 
Amazon.com Inc (AMZN)
Alphabet Inc Class A (GOOGL)
Alphabet Inc Class C (GOOG)

All the above belong to either Consumer Discretionary or Information Technology sector.
# In[20]:


df1[df1.Week_52_high> 1000].sort_values('Week_52_high',ascending=False)


# In[21]:


df1[df1.Week_52_low> 1000].sort_values('Week_52_low',ascending=False)


# In[22]:


df1_Sales_value = df1.groupby('Sector')[['Earning_Share']].sum().sort_values('Earning_Share',ascending = False)
df1_Sales_value


# The Consumer Discretionary sector is the most profitable followed by the Industrials sector. 

# In[23]:


df1_Sales_value = df1.groupby('Sector')[['Earning_Share']].mean().sort_values('Earning_Share',ascending = False)
df1_Sales_value

The average earnings for Industrials and Materials go hand in hand as it both of these sectors depend on earch other.
In order for an industry to function properly it needs raw materials so it makes sense for these sectors to be at the top of the chart. 
# In[24]:


df1.info()


# In[25]:


pd.set_option('display.max_rows', None)


# In[26]:


df1[df1['Sector'].str.contains('Consumer Discretionary')].count()


# In[27]:


df1[df1['Sector'].str.contains('Consumer Discretionary')].sort_values('Market_cap',ascending = False)


# Amazon has the highest Market Capital in the Consumer Discretionary sector. It is clear that more people tend to shop online now a days.

# In[28]:


df1[df1['Sector'].str.contains('Industrials')].count()


# In[29]:


df_industry = df1[df1['Sector'].str.contains('Industrials')].sort_values('Market_cap',ascending = False)
df_industry 

By the analysig the market trend ,The Boeing company is at the top of the market in the Industry sector. There is a hugh gap between The Boeing Company which sits at the top of the chart and the 3M Company which is second on the chart.
# In[30]:


df1[df1['Sector'].str.contains('Information Technology')].count()


# In[31]:


Info_tech = df1[df1['Sector'].str.contains('Information Technology')].sort_values('Market_cap',ascending = False)
Info_tech


# Apple, Alphabet Class A, Alphabet Class C and Microsoft Corp are the top 4 IT companies with the highest Market Cap out of the 70 IT companies listed in the TOP 500 fortune companies of the world.

# In[32]:


df_Div_Ear = df1[(df1['Dividend_Yield']>1)&(df1['Earning_Share'] < 10)].sort_values('Market_cap',ascending = False)
df_Div_Ear


# In[33]:


df_Div_Ear.count()


# In[34]:


df1['Symbol'] = df1['Symbol'].astype('category')


# In[35]:


df1['Name'] = df1['Name'].astype('category')


# In[36]:


df1['Sector'] = df1['Sector'].astype('category')


# In[37]:


df1.info()


# In[38]:


import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (9, 5)
matplotlib.rcParams['figure.facecolor'] = '#00000000'


# In[39]:


Sector_df = df1.Sector.value_counts()
Sector_df


# In[40]:


plt.figure(figsize=(16,8))
plt.xticks(rotation=70)
plt.title('Sector')
sns.barplot(x= Sector_df.index, y=Sector_df);


# In[42]:


import numpy as np


# In[43]:


plt.figure(figsize=(12, 6))
plt.title('Week 52 closing')
plt.xlabel('Week_52_low')
plt.ylabel('Symbol')

plt.hist(df1.Week_52_low, bins=np.arange(10,100,5), color='purple');


# In[44]:


plt.figure(figsize=(12, 6))
plt.title('Week 52 Opening')
plt.xlabel('Week_52_High')
plt.ylabel('Symbol')

plt.hist(df1.Week_52_high, bins=np.arange(10,100,5), color='green');


# In[46]:


plt.figure(figsize=(12, 6))
sns.distplot(df1.Price_Sales, kde =False)
plt.show();


# In[47]:


df1.groupby(['Sector'])['Price_Sales'].agg(['mean','std']).plot(kind = 'barh', stacked = True)
plt.xticks(rotation = 0)
plt.show()


# In[48]:


plt.figure(figsize=(18,8))
sns.pairplot(df1,kind = 'reg',vars = ['Market_cap','Price'], hue = 'Sector');


# In[49]:


df1.dtypes


# In[52]:


df1_corr = df1.corr()


# In[54]:


sns.heatmap(df1_corr,annot=True)
plt.figure(figsize=(18,8));


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




