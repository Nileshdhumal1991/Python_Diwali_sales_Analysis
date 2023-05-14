# -*- coding: utf-8 -*-
"""Data Analytics with Python Project

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U3Q0my-j7xQ1fB7Srq8TyT9iObwNZKVL
"""

import numpy as np
 import pandas as pd
 import matplotlib.pyplot as plt
 import seaborn as sns

df = pd.read_csv("/content/drive/MyDrive/Analytics with Python Project/Diwali Sales Data.csv", encoding="latin-1")
df

df.shape

df.head()

df.info()

df.drop(['Status','unnamed1'],axis=1,inplace=True)

df.info()

#Check null values
pd.isnull(df)

pd.isnull(df).sum()

df.shape

df.dropna(inplace = True)

pd.isnull(df).sum()

df.info()

df['Amount']=df['Amount'].astype('int')

df['Amount'].dtypes

df.columns

df.rename(columns = {'Marital_Status':'shadi'})

df.describe()

"""**Exploratory Data Analysis**"""

df.columns

# plotting a bar chart for Gender and it's count
x=sns.countplot(x='Gender', data=df)

for bars in x.containers:
  x.bar_label(bars)

df.groupby(['Gender'])['Amount'].sum().sort_values(ascending=False)

# plotting a bar chart for gender vs total amount

sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)

"""*From above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than men*

**#AGE**
"""

ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)

df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

# Total Amount vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

ax=sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age)

"""From above graphs we can see that most of the buyers are of age group between 26-35 yrs female

**State**
"""

df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

# total number of orders from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(12)
                                                                                                                   

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Orders')

# total amount/sales from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(12)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Amount')

"""*From above graphs we can see that most of the orders & total sales/amount are from Uttar Pradesh, Maharashtra and Karnataka respectively*

**Marital Status**
"""

ax=sns.countplot(data = df, x = 'Marital_Status')

sns.set(rc={'figure.figsize':(3,3)})
for bars in ax.containers:
    ax.bar_label(bars)

sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')

"""*From above graphs we can see that most of the buyers are married (women) and they have high purchasing power*

Occupation
"""

sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)

sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')

"""From above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation sector

Product Category
"""

sns.set(rc={'figure.figsize':(25,7)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)

sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')

df.groupby(['Product_Category'])['Amount'].sum().sort_values(ascending=False).head(10)

sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')

"""From above graphs we can see that most of the sold products are from Food, Clothing and Electronics category

**Conclusion:-**
Married women age group 26-35 yrs from UP, Maharastra and Karnataka working 
in IT, Healthcare and Aviation are more likely to buy 
products from Food, Clothing and Electronics category
"""