import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

NUTRITIONIX_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_ENDPOINT = os.environ.get('SHEETY_ENDPOINT')

today = datetime.now()
hour = today.strftime('%H:%M:%S')
today = today.strftime('%d/%m/%Y')

headers = {
    'x-app-id': os.environ.get('NUTRITIONIX_ID'),
    'x-app-key': os.environ.get('NUTRITIONIX_API_KEY'),
    'Content-Type': 'application/json',
}

exercise_params = {
    'query': input('What exercise did you do and for how many minutes? '),
    'gender': input('Male or Female ').lower(),
    'weight_kg': int(input('Weight in lbs? ')) / 2.2046226,
    'height_cm': int(input('Height in cm? ')),
    'age': int(input('Age? '))
}

nutri_response = requests.post(url=NUTRITIONIX_ENDPOINT, json=exercise_params, headers=headers)
nutri_response.raise_for_status()
data = nutri_response.json()
exercise_data = data['exercises'][0]

sheety_params = {
    'workout': {
        'date': today,
        'time': hour,
        'exercise': exercise_data['name'],
        'duration': exercise_data['duration_min'],
        'calories': round(exercise_data['nf_calories'], 0)

    }
}


sheety_post = requests.post(url=SHEETY_ENDPOINT, json=sheety_params)
sheety_post.raise_for_status()

