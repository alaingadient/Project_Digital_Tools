# upstream.py
import os
import json
import requests

start_date = "2020-01-01"
end_date = "2021-01-01"

# get the data
url = "{root_url}/{endpoint}?source={base}&api_key={api_key}&currencies={symbols}&start_date={observation_start}&end_date={observation_end}" \
    .format(root_url="https://api.apilayer.com",
            endpoint="currency_data/timeframe",
            base="CHF",
            api_key="X3hyUw4lUbU4HCmrjfLXqe026xGmlQ6L",
            symbols="USD,EUR,GBP,JPY,AUD,NZD,CAD,NOK,SEK",
            observation_start=start_date,
            observation_end=end_date
           )

payload = {}
headers= {
  "apikey": "X3hyUw4lUbU4HCmrjfLXqe026xGmlQ6L"
}
response = requests.request("GET", url, headers=headers, data=payload)
status_code = response.status_code
result = response.text
result = json.loads(result)

save_path = os.getcwd() + "/data"
save_name = "G10_currency_quote_from_{start_date}_to_{end_date}.json".format(start_date=start_date, end_date=end_date)

# overwrite if exists.
save_file = save_path + "/" + save_name
with open(save_file, "w+") as f:
    try:
        data = json.load(f)
    except json.JSONDecodeError:
        data = {}
    json.dump(result, f, indent = 4)
