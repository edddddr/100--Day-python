import os
from http.client import responses

import requests
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv('API_ID')
API_KEY = os.getenv('API_KEY')

workout_URL = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheety_URL =  'https://api.sheety.co/4b3fc0aebd1f3a0f1ea4db7b17f029ec/myWorkouts/workouts'
num = 3
workout_headers = {
    'x-app-id': API_ID,
    'x-app-key': API_KEY
}

# user_input = input("Tell me what exercise you did")

sheety_headers = {
    'Authorization' :  'Basic Og=='
}

parameters = {
    'query' : "ran 3 miles and did 20 push-ups",
    'gender' : "male",
    'weight_kg' : 55,
    'height_cm' : 1.57,
    'age': 80
}

workout_res = requests.post(
    url=workout_URL,
    json=parameters,
    headers = workout_headers
)





workout = workout_res.json()['exercises']
exercise = workout[0]['user_input']
duration = workout[0]['duration_min']
calories = workout[0]['nf_calories']


def count(num):
    return num + 1

workout_params = {
    'workout' : {
             'date': '30/09/2025',
             'time': '15:00:00',
             'exercise': exercise,
             'duration': duration,
             'calories': calories,
             'id': count(num)
                 }
}

response = requests.post(url=sheety_URL, json=workout_params, headers=sheety_headers)


print(response.json())