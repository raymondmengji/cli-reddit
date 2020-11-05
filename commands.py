import requests

import app


def search(param):
    response = requests.get(app.API_URL + '/subreddits/search', headers=app.HEADER, params=param)
    # print('Status Code: ', response.status_code)
    values = response.json()

    for i in range(len(values['data']['children'])):
        print(values['data']['children'][i]['data']['display_name'])