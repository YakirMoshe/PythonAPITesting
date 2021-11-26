import requests
import json
import jsonpath

def test_add_sudent_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    #Read file
    file = open("C:/TASK_API/RequestJson.json", "r")
    json_request = json.loads(file.read())
    response = requests.post(API_URL, json_request)
    print(response.text)

def test_get_student_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/529135"
    response = requests.get(API_URL)
    json_response = response.json()
    #json_response = json.loads(response.text)
    # valid id data
    id = jsonpath.jsonpath(json_response, 'data.id')
    print(id)
    assert id[0] == 529135

def test_update_sudent_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/529135"
    #Read file
    file = open("C:/TASK_API/UpdateRequestJson.json", "r")
    json_request = json.loads(file.read())
    response = requests.put(API_URL, json_request)
    print(response.text)

# After Update print GET REQUEST FOR VALID
def test_get_student_AfterUpdateData():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/529135"
    response = requests.get(API_URL)
    json_response = response.json()
    #json_response = json.loads(response.text)
    # valid id data
    print(json_response)
    id = jsonpath.jsonpath(json_response, 'data.id')
    print(id)
    assert id[0] == 529135

def test_delete_student():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/529135"
    response = requests.delete(API_URL)
    print(response.text)

# After Update print GET REQUEST FOR VALID
def test_get_student_ValidDeleteStudent():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/529135"
    response = requests.get(API_URL)
    json_response = response.json()
    #json_response = json.loads(response.text)
    # valid id data
    print(json_response)
    id = jsonpath.jsonpath(json_response, 'data.id')
    print(id)
    assert id[0] == 529135