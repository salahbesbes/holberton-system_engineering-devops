#!/usr/bin/python3
""" requests module """
import json
from sys import argv

import requests

if __name__ == "__main__":
    if len(argv) != 2:
        exit(1)

    emp_id = argv[1]
    with open('todo_all_employees.json', mode='w') as employee_file:
        response = requests.request(
            'get',
            'https://jsonplaceholder.typicode.com/users/{}/todos'.format(emp_id))
        res = requests.request('get',
                               'https://jsonplaceholder.typicode.com/users/{}'
                               .format(emp_id))  # list of dicts
        todo_list = json.loads(response.text)
        employee_name = json.loads(res.text).get('name')
        employee_username = json.loads(res.text).get('username')

        array_todo = []
        for todo in todo_list:
            tmp = {'task': todo.get('title'),
                   'completed': todo.get('completed'),
                   'username': employee_username}
            array_todo.append(tmp)

        obj_to_dump = {emp_id: array_todo}
        json.dump(obj_to_dump, employee_file, indent=2)
