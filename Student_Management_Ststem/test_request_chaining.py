import requests
import json
import jsonpath

def test_add_sudent_data():
    global id
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    #Read file
    file = open("C:/TASK_API/RequestJson.json", "r")
    json_request = json.loads(file.read())
    response = requests.post(API_URL, json_request)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

def test_get_details():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/"+str(id[0])
    response = requests.get(API_URL)
    print(response.text)