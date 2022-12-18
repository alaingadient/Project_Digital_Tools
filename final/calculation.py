#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import json
import pandas as pd
import numpy as np

def value_at_risk(data, alpha):
    sorted_df = data.sort_values(ascending=True)
    value = sorted_df.quantile(q=alpha, interpolation='higher')
    return value

def expected_shortfall(table, alpha):
    es_table=pd.DataFrame()
    for i in table.columns:
        if i=="date":
            continue
        data_column=table[i]
        sorted_df = data_column.sort_values(ascending=True)
        var = value_at_risk(sorted_df, alpha=alpha)
        p=sum(k<var for k in data_column)
        es = 1/p * sum(sorted_df[sorted_df < var])
        es_table[i]=[es]
    return es_table

def variance(table):
 
    quote_variance = table.var()
    return quote_variance

