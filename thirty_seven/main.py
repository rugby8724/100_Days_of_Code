import requests
import os
from dotenv import load_dotenv
from datetime import datetime
from urllib.error import HTTPError

load_dotenv()

pixela_endpoint = 'https://pixe.la/v1/users'

PIXELA_TOKEN = os.environ.get('PIXELA_TOKEN')
PIXELA_USER_NAME = os.environ.get('PIXELA_USER')
PIXELA_GRAPH_ID = 'graph1'

pixela_input_endpoint = f'{pixela_endpoint}/{PIXELA_USER_NAME}/graphs/{PIXELA_GRAPH_ID}'

headers = {
    'X-USER-TOKEN': PIXELA_TOKEN
}


# ------------- enter daily data into pixela ---------------
def programming_min_today():
    today = datetime.now()
    today = today.strftime('%Y%m%d')

    pixela_input_config = {
        'date': today,
        'quantity': input('How many minutes did you code today: ')
    }

    response = requests.post(url=pixela_input_endpoint, json=pixela_input_config, headers=headers)
    print(response.text)


# ------------- edit daily data in pixela ---------------


def edit_pixela():
    day = input('What day would you like to edit please format as yyyyMMdd: ')
    try:
        update_endpoint = f'{pixela_input_endpoint}/{day}'
    except HTTPError as e:
        if e.code == 404:
            edit_pixela()

    update_config = {
        'quantity': input(f'How man minutes did you code on {day}: ')
    }

    response = requests.put(url=update_endpoint, json=update_config, headers=headers)
    print(response.text)


# ------------- edit daily data in pixela ---------------


def delete_pixela():
    day = input('What day would you like to delete please format as yyyyMMdd: ')
    try:
        delete_endpoint = f'{pixela_input_endpoint}/{day}'
    except HTTPError as e:
        if e == 404:
            delete_pixela()

    response = requests.delete(url=delete_endpoint, headers=headers)
    print(response.text)

# ---------- call function ----------


def run_pixela():
    user_request = input('To enter today\'s min press:"m" \n '
                         'To edit a day press:"e" \n '
                         'To delete a day type: "DELETE":  ')

    if user_request.lower() == 'm':
        programming_min_today()
    elif user_request.lower() == 'e':
        edit_pixela()
    elif user_request == 'DELETE':
        delete_pixela()
    else:
        run_pixela()

run_pixela()

# ---------- used to create user on used on first run ----------
# user_params = {
#     'token': PIXELA_TOKEN ,
#     'username': PIXELA_USER_NAME,
#     'agreeTermsOfService': 'yes',
#     'notMinor': 'yes',
# }

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# ------------- used to create user on used on first run ---------------
# graph_endpoint = f'{pixela_endpoint}/{PIXELA_USER_NAME}/graphs'
#
# graph_config = {
#     'id': 'graph1',
#     'name': 'Programming Graph',
#     'unit': 'Minutes',
#     'type': 'int',
#     'color': 'shibafu',
#
# }
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
