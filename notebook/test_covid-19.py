import requests

url = 'https://covid-19.adapay.tech/api/v1/'
token = '497115d0c2ff9586bf0fe03088cfdbe2'

payload = {
    'country': 'China',
    'stime': '2020-02-01',
    'etime': '2020-03-22'
}

headers = {
            'token': token
        }

r = requests.get(url+'infection/country', params=payload, headers=headers)

data = r.json()

print(data)

for key, value in data['data'].items():
    print(key, value)

