import os
import json
import pandas as pd


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
            table.iloc[i,p]=np.log(table.iloc[i+1,p]/table.iloc[i,p])
    table.drop(table.tail(1).index, inplace=True)
    return table

# def value_at_risk(data, alpha=0.95):
#     sorted_df = data.sort_values(ascending=True)
#     value = sorted_df.quantile(q=alpha, interpolation='higher')
#     return value

# can be overwritten with the next def when it is approved
# def expected_shortfall(data_column, alpha=0.95):
#     sorted_df = data_column.sort_values(ascending=True)
#     var = value_at_risk(sorted_df, alpha=alpha)
#     multiplier = 1/(len(sorted_df)*(1-alpha))
#     es = multiplier * (var * (sorted_df.searchsorted(var)[0] + 1) - len(sorted_df) * alpha
#                        + sum(sorted_df[sorted_df > var]))
#     return es

def expected_shortfall(data, alpha):
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










def main():
    # load data
    data = load_data()

    # preprocess data
    table = preprocess_data(data)

    currency_quote_list = table.columns.values[1:]
    quote_variance = table[currency_quote_list].var()
    quote_std = table[currency_quote_list].std()


if __name__ == "__main__":
    main()
