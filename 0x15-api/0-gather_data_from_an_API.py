#!/usr/bin/python3
""" requests module """
import requests
from sys import argv

if __name__ == "__main__":

    emp_id = argv[1]
    todo_list = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                             .format(emp_id)).json()
    employee = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(emp_id)).json()
    employee_name = employee.get('name')
    total_todos = len(todo_list)
    list_completed_todos = [el for el in todo_list if el.get('completed')]
    completed_todos = len(list_completed_todos)
    print('Employee {} is done with tasks({}/{}):'.format(employee_name,
                                                          completed_todos,
                                                          total_todos))

    for todo in list_completed_todos:
        print('\t {}'.format(todo.get('title')))
