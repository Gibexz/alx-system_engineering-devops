#!/usr/bin/python3
"""
0-gather_data_from_an_API.py module
"""
import requests


def getEmployeeData(id):
    """
    script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
    """
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    user_url = "https://jsonplaceholder.typicode.com/users"

    todos = requests.get(todos_url).json()
    users = requests.get(user_url).json()

    tasks_completed = []
    nos_tasks = 0
    nos_tasks_completed = 0

    for todo in todos:
        if id == todo['userId']:
            nos_tasks += 1

    for todo in todos:
        if id == todo['userId'] and todo['completed'] is True:
            tasks_completed.append(todo['title'])
            nos_tasks_completed += 1

    for user in users:
        if id == user['id']:
            name = user['name']
            break

    print("Employee {} is done with task({}/{}):"
          .format(name, nos_tasks_completed, nos_tasks))
    for task in tasks_completed:
        print(f"\t{task}")


if __name__ == "__main__":
    """Main Function"""
    import sys
    employeId = int(sys.argv[1])
    getEmployeeData(employeId)
