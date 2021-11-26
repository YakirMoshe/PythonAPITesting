import requests
import json
import jsonpath

def test_Add_new_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    file = open('C:/TASK_API/RequestJson.json', 'r')
    json_request = json.loads(file.read())
    response = requests.post(API_URL, json_request)
    print(response.text)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

    tech_api_url = "http://thetestingworldapi.com/api/technicalskills"
    file = open('C:/TASK_API/TechDetails.json', 'r')
    requests_json = json.loads(file.read())
    #Update in the File id
    requests_json['id'] = int(id[0])
    requests_json['st_id'] = id[0]
    response = requests.post(tech_api_url, requests_json)
    print(response.text)

    addresses_api_url = "http://thetestingworld.com/api/addresses"
    file = open('C:/TASK_API/Address.json', 'r')
    requests_json = json.loads(file.read())
    #Update in the File stId
    requests_json['stId'] = id[0]
    response = requests.post(addresses_api_url, requests_json)

    final_details = "http://thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])
    response = requests.get(final_details)
    print(response.text)