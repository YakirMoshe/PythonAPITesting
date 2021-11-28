import json
import requests
import jsonpath
import openpyxl
from Data_Driven_Testing import Library


def test_add_multiple_student():
    # API
    API_URL = "https://reqres.in/api/users"
    file = open('C:/TASK_API/AddNewStudent.json')
    json_request = json.loads(file.read())

    #Send to contractor 2 params: FileNamePath,SheetName
    obj = Library.Common("C:/TASK_API/TestData.xlsx", "Sheet1")
    col = obj.fetch_column_count()
    row = obj.fetch_row_count()
    keyList = obj.fetch_key_names()

    for i in range(2, row+1):
         update_json_request = obj.update_request_with_data(i, json_request,keyList)
         response = requests.post(API_URL, update_json_request)
         print(response.text)
         assert response.status_code == 201