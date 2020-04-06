import requests
import pandas as pd

url = 'https://covid-19.adapay.tech/api/v1/'
token = '497115d0c2ff9586bf0fe03088cfdbe2'
region = 'US'

headers = {
    'token': token
}

payload = {
    'region': region,

    'start_date': '2020-03-26',
    'end_date': '2020-04-04'
}

# interface: region

r = requests.get(url+'infection/region', params=payload, headers=headers)

data = r.json()

print('---')
# json raw data
print(data)

print('---')
# filter data
for key, value in data['data']['region'][region].items():
    print(key, value)

print('---')
# load to dataframe
df = pd.DataFrame.from_dict(data['data']['region'][region])
print(df)

print('---')
# rotate dataframe
df = df.T
print(df)

# interface: region detail

payload = {
    'region': region,
    'start_date': '2020-03-26',
    'end_date': '2020-03-27'
}

r = requests.get(url+'infection/region/detail', params=payload, headers=headers)

data = r.json()

print('---')
# json raw data
print(data)

print('---')
# filter data
for key, value in data['data']['area'].items():
    print(key, value)

print('---')
# load to dataframe
df = pd.DataFrame.from_dict(data['data'])
df = pd.DataFrame(df, index=['a', 'b'])
print(df)

print('---')
df = pd.DataFrame.from_dict(data['data']['area']['New York'])
print(df)

print('---')
# rotate dataframe
df = df.T
print(df)

print('---')
df1 = df['a']
print(df1)


