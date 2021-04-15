import requests

params = {
    'name': 'Tad'
}

response = requests.get('https://api.agify.io', params=params)
data = response.json()
age = data['age']
print(age)