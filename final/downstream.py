#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import json
import pandas as pd
import numpy 


def load_data():
    # Should be the same as the saved file in the data folder
    start_date = "2020-01-01"
    end_date = "2021-01-01"

    saved_path = os.getcwd() + "/data"
    saved_name = "G10_currency_quote_from_{start_date}_to_{end_date}.json".format(start_date=start_date, end_date=end_date)
    saved_file = saved_path + "/" + saved_name

    with open(saved_file) as f:
        data = f.read()
        data = json.loads(data)
    return data


def preprocess_data(data):
    data = pd.DataFrame(data)
    table = pd.json_normalize(data['quotes'])
    date = list(data.index)
    table.insert(0, "date", date)
    return table


# give the log returns of the data
def preprocess_data_log_returns(data):
    data = pd.DataFrame(data)
    table = pd.json_normalize(data['quotes'])
    date = list(data.index)
    table.insert(0, "date", date)
    length=int(table.shape[0]-1)
    col=int(table.shape[1])
    for p in range(1,col):
        for i in range(0,length):
            table.iloc[i,p]=numpy.log(table.iloc[i+1,p]/table.iloc[i,p])
    table.drop(table.tail(1).index, inplace=True)
    return table

