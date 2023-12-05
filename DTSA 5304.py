#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
data= pd.read_csv("Recalls_Data_Cleaned.csv")
data.head()


# In[34]:


import altair as alt
alt.Chart(data).mark_bar().encode(x="Component", y="Potentially Affected")


# In[27]:


alt.Chart(data).mark_circle().encode(x="Component", y="Potentially Affected")


# In[32]:


alt.Chart(data).mark_circle().encode(
    x = "Component",
    y = "Potentially Affected",
    color="Manufacturer"
)


# In[65]:


import pandas as pd
datav1= pd.read_csv("Recalls_Data_v1.csv")
datav1.head()


# In[49]:


alt.Chart(datav1).mark_circle().encode(
    x = "Component",
    y = "Potentially Affected",
    color="Report Year"
)


# In[54]:


alt.Chart(datav1).mark_circle().encode(
    x = "Component",
    y = "Completion Rate % (Blank - Not Reported)",
    color=alt.Color('Recall Type', scale=alt.Scale(scheme='spectral')),
    size="Potentially Affected",
    tooltip=["Manufacturer", "Potentially Affected", "Recall Type"]
)


# In[61]:


alt.Chart(datav1).mark_circle().encode(
    x = "Component",
    y = "Completion Rate % (Blank - Not Reported)",
    color=alt.Color('Manufacturer', scale=alt.Scale(scheme='spectral', 
                                                    domain=['Ford Motor Company', 
                                                            'Takata (TK Global, LLC)',
                                                            'General Motors, LLC',
                                                            'Chrysler (FCA US, LLC)',
                                                            'Honda (American Honda Motor Co.)',
                                                            'Toyota Motor Engineering & Manufacturing',
                                                            'Nissan North America, Inc.',
                                                            'Subaru of America, Inc.',
                                                            'Kiekert USA',
                                                            'Hyundai Motor America'])),
    size="Potentially Affected",
    tooltip=["Manufacturer", "Potentially Affected", "Completion Rate % (Blank - Not Reported)", "Recall Type"]
)


# In[66]:


alt.Chart(datav1).mark_circle().encode(
    x = "Component", 
    y = "Completion Rate % (Blank - Not Reported)", 
    color=alt.Color('Manufacturer', scale=alt.Scale(scheme='spectral', 
                                                    domain=['Ford Motor Company', 
                                                            'General Motors, LLC', 
                                                            'Chrysler (FCA US, LLC)', 
                                                            'Kiekert USA', 'Honda (American Honda Motor Co.)', 
                                                            'Takata (TK Global, LLC)',
                                                            'Toyota Motor Engineering & Manufacturing', 
                                                            'Nissan North America, Inc.', 
                                                            'Hyundai Motor America', 
                                                            'Subaru of America, Inc.'])), 
    size="Potentially Affected", 
    tooltip=["Manufacturer", "Potentially Affected", "Completion Rate % (Blank - Not Reported)", "Recall Type"] )


# In[116]:


alt.Chart(datav1).mark_circle().encode(
    x = "Completion Rate % (Blank - Not Reported)",
    y = "Recall Type",
    color=alt.Color('Recall Type'),
    size = "Potentially Affected",
    tooltip=["Manufacturer", "Potentially Affected", "Recall Type", "Completion Rate % (Blank - Not Reported)"])


# In[98]:


datav4= pd.read_csv("Recalls_Data_v4.csv")
datav4.head()


# In[99]:


alt.Chart(datav4).mark_circle().encode(
    x = "Component",
    y = "Completion Rate % (Blank - Not Reported)",
    color=alt.Color('Parent Company Region', scale=alt.Scale(scheme='spectral')),
    size="Potentially Affected",
    tooltip=["Manufacturer", "Potentially Affected", "Completion Rate % (Blank - Not Reported)", "Recall Type"]
)

