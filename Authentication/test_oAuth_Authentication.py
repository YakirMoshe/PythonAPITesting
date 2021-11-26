import json
import requests
import jsonpath

def test_oAuth_api():
    token_url = "https://reqres.in/api/login"
    data = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
    }
    response = requests.post(token_url, data)
    print(response.text)
    token_value = jsonpath.jsonpath(response.json(),'token')
    print(response.text)
    auth = {'Authorization':'Bearer '+ token_value[0]}
    API_URL = 'https://reqres.in/api/users?page=2'
    response = requests.get(API_URL, headers =auth)
    print(response.text)
