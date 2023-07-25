#!/usr/bin/python3
"""
2-export_to_JSON.py module
"""
import json
import requests


def write2JSON(filename, data):
    """converts a dictionary to JSON format and saves to a json file"""
    with open(filename, mode='w') as file:
        json.dump(data, file)


def exportEmployeeData(id):
    """
     script to export an employee data in the JSON format
    """
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    user_url = "https://jsonplaceholder.typicode.com/users"

    todos = requests.get(todos_url).json()
    users = requests.get(user_url).json()
    
    userIdList = []
    employeeDataDict = {}
    employeeDataList = []

    for user in users:
        userIdList.append[user['id']]
    """for user in users:
        if id == user['id']:
            username = user['username']"""

    for todo in todos:
        if id == todo['userId']:
            taskStatus = todo['completed']
            taskTitle = todo['title']
            employeeDataList.append({"task": taskTitle,
                                     "completed": taskStatus,
                                     "username": username})
            employeeDataDict.update({id: employeeDataList})
    """for key, value in employeeDataDict.items():
        print(f"{key}: {value}")
    print(employeeDataDict)

    fileName = f"{id}.json"
    write2JSON(fileName, employeeDataDict)"""


if __name__ == "__main__":
    """Main Function"""
    import sys
    employeId = int(sys.argv[1])
    exportEmployeeData(employeId)
