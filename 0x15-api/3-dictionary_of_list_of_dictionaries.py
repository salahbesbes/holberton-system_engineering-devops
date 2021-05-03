#!/usr/bin/python3
""" requests module """
import json
import requests

if __name__ == "__main__":

    with open('todo_all_employees.json', mode='w') as employee_file:
        all_employee = requests.get(
            'https://jsonplaceholder.typicode.com/users/').json()

        object_to_dump = {}
        for user in all_employee:
            user_id = user.get('id')
            todo_list = requests.request(
                'get',
                'https://jsonplaceholder.typicode.com/users/{}/todos'
                .format(user_id)).json()

            array_todo = []
            for todo in todo_list:
                tmp = {'task': todo.get('title'),
                       'completed': todo.get('completed'),
                       'username': user.get('username')}
                array_todo.append(tmp)
            object_to_dump.update({user_id: array_todo})

        json.dump(object_to_dump, employee_file, indent=2)
