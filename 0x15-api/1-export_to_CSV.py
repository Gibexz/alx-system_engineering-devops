#!/usr/bin/python3
"""
1-export_to_CSV.py module
"""
import requests
import csv


def write2CSV(filename, data):
    """Write datas in to a given csv filename"""
    """with open(filename, mode='w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        for row in data:
            writer.writerow('"{}"'.format(val) for val in row)
"""
    with open(filename, mode='w', newline='') as file:
        for row in data:
            formatted_row = ','.join(['"{}"'.format(val) for val in row])
            file.write(formatted_row + '\n')


def exportEmployeeData(id):
    """
     script to export an employee data in the CSV format
    """
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    user_url = "https://jsonplaceholder.typicode.com/users"

    todos = requests.get(todos_url).json()
    users = requests.get(user_url).json()

    employeeData = []

    for user in users:
        if id == user['id']:
            username = user['username']

    for todo in todos:
        if id == todo['userId']:
            taskStatus = todo['completed']
            taskTitle = todo['title']
            """ print test
            print('"{}","{}","{}","{}"'
                  .format(id, username, taskStatus, taskTitle))
            """
            employeeData.append([id, username, taskStatus, taskTitle])

    fileName = f"{id}.csv"
    write2CSV(fileName, employeeData)


if __name__ == "__main__":
    """Main Function"""
    import sys
    employeId = int(sys.argv[1])
    exportEmployeeData(employeId)
