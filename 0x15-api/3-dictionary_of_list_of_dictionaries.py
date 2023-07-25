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


def exportEmployeeData():
    """
     script to export an employee data in the JSON format
    """
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    user_url = "https://jsonplaceholder.typicode.com/users"

    todos = requests.get(todos_url).json()
    users = requests.get(user_url).json()

    employeeDataDict = {}

    for id in range(1, len(users) + 1):
        userId = id

        employeeList = []

        username = ""
        for user in users:
            if user['id'] == userId:
                username = user['username']

        for todo in todos:
            if todo['userId'] == userId:
                temp_list = {'task': todo['title'],
                             'completed': todo['completed'],
                             'username': username}
                employeeList.append(temp_list)

        for user in users:
            if user['id'] == userId:
                username = user['username']

        temp_dic = {userId: employeeList}
        employeeDataDict.update(temp_dic)

    fileName = "todo_all_employees.json"
    write2JSON(fileName, employeeDataDict)


if __name__ == "__main__":
    """Main Function"""
    exportEmployeeData()
