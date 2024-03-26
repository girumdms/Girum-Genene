#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


txt_data = pd.read_table('MSdos_R_E.txt', usecols=['Date','Budgeted Cost of Revenue',
                                                   'Budgeted Cost of Expenditure'], parse_dates=['Date'])


# In[4]:


df_w = pd.DataFrame({'Date_Pay_w': pd.to_datetime(['2017-05-01', '2017-05-07', '2017-05-14','2017-05-21',
                                                   '2017-05-27', '2017-06-02']),
                     'Type':['20% Advance Payment', '1st Pay', '2nd Pay', '3rd pay', '4th pay', '5th pay'],
                                               
                     'payment_w':[792702, 762508, 603925, 402240, 420424, 981711]})


# In[5]:


# this will call any row value data using the indentation number
txt_data.iloc[32]


# In[6]:


df_w


# In[7]:


df_w['payment_w'].sum()


# df is a data Frame used for plotting of the disbursement graph and it is a cummulative value

# In[8]:


df = pd.DataFrame({'Date_pay': pd.to_datetime(['2017-05-01', '2017-05-07', '2017-05-14',
                                               '2017-05-21', '2017-05-27', '2017-06-02']),
                'payment_Cu':[792702,  1555210, 2159135, 2561375, 2981799, 3963511]})


# In[9]:


from bokeh.plotting import figure, output_file, show
from bokeh.io import output_notebook

output_notebook()


# In[11]:


p1 = figure(x_axis_type='datetime', title='Revenue vs Expenditure Graph', width =800, plot_height= 400)

p1.grid.grid_line_alpha=1
p1.xaxis.axis_label = 'Date'
p1.yaxis.axis_label = 'Budgeted Cost'


p1.line(txt_data['Date'], txt_data['Budgeted Cost of Revenue'], color='#f2a900', legend = 'Rev.')
p1.line(txt_data['Date'], txt_data['Budgeted Cost of Expenditure'], color='green', legend = 'Exp.')

p1.line(df['Date_pay'], df['payment_Cu'],color='red', legend = 'Pay. Disb. Schedule')


p1.legend.location ='top_left'
show(p1)


# In[ ]:




