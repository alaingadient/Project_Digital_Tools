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


# def value_at_risk(data, alpha=0.95):
#     sorted_df = data.sort_values(ascending=True)
#     value = sorted_df.quantile(q=alpha, interpolation='higher')
#     return value


# def expected_shortfall(data_column, alpha=0.95):
#     sorted_df = data_column.sort_values(ascending=True)
#     var = value_at_risk(sorted_df, alpha=alpha)
#     multiplier = 1/(len(sorted_df)*(1-alpha))
#     es = multiplier * (var * (sorted_df.searchsorted(var)[0] + 1) - len(sorted_df) * alpha
#                        + sum(sorted_df[sorted_df > var]))
#     return es


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