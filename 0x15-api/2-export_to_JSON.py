#!/usr/bin/python3
""" requests module """
import json
import requests
from sys import argv

if __name__ == "__main__":

    emp_id = argv[1]
    with open('{}.json'.format(emp_id), mode='w') as employee_file:
        todo_list = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}/todos'
            .format(emp_id)).json()
        employee = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'
            .format(emp_id)).json()

        employee_name = employee.get('name')
        employee_username = employee.get('username')

        array_todo = []
        for todo in todo_list:
            tmp = {'task': todo.get('title'),
                   'completed': todo.get('completed'),
                   'username': employee_username}
            array_todo.append(tmp)

        obj_to_dump = {emp_id: array_todo}
        json.dump(obj_to_dump, employee_file, indent=2)
