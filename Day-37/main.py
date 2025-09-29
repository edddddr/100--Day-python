import requests
import datetime

TOKEN = 'oslidjfwio9e00skjd'
USER = 'endaw'
GRAPH_ID = 'atoz'


pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token' : TOKEN,
    'username' : USER,
    'agreeTermsOfService' : 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixela_endpoint, json=user_params)


graph_endpoint = f'{pixela_endpoint}/{USER}/graphs'

graph_params = {
    'id' : GRAPH_ID,
    'name': 'Cycling graph',
    'unit': 'km',
    'type': 'float',
    'color': 'ajisai'
}

headers = {
    'X-USER-TOKEN' : TOKEN
}

date = datetime.datetime(year=2025, month=9, day=28)

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)

pixel_endpoint = f"{pixela_endpoint}/{USER}/graphs/{GRAPH_ID}"


pixel_params = {
    'quantity' : '30.343',

}
# /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
# response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)

response = requests.delete(url= f'{pixela_endpoint}/{USER}/graphs/{GRAPH_ID}/20250828',
                        headers=headers
                        )

print(response.text)