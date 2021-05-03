#!/usr/bin/python3
""" requests module """
import json
from sys import argv

import requests

if __name__ == "__main__":
    if len(argv) != 2:
        exit()
    emp_id = argv[1]
    response = requests.request(
        'get',
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(emp_id))
    res = requests.request('get',
                           'https://jsonplaceholder.typicode.com/users/{}'
                           .format(emp_id))  # list of dicts
    todo_list = json.loads(response.text)
    employee_name = json.loads(res.text).get('name')
    total_todos = len(todo_list)
    list_completed_todos = [el for el in todo_list if el.get('completed')]
    completed_todos = len(list_completed_todos)
    print('Employee {} is done with tasks({}/{}):'.format(employee_name,
                                                          completed_todos,
                                                          total_todos))

    for todo in list_completed_todos:
        print('\t {}'.format(todo.get('title')))
