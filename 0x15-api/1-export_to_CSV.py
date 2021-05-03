#!/usr/bin/python3
""" requests module """
import csv
import json
from sys import argv
import requests

if __name__ == "__main__":
    if len(argv) != 2:
        exit()
    emp_id = argv[1]
    with open('{}.csv'.format(emp_id), mode='w') as employee_file:
        employee_writer = csv.writer(employee_file,
                                     delimiter=',',
                                     quotechar='"',
                                     quoting=csv.QUOTE_ALL)
        response = requests.request(
                'get',
                'https://jsonplaceholder.typicode.com/users/{}/todos'
                .format(emp_id))
        res = requests.request('get',
                               'https://jsonplaceholder.typicode.com/users/{}'
                               .format(emp_id))  # list of dicts
        todo_list = json.loads(response.text)
        employee_name = json.loads(res.text).get('name')

        for todo in todo_list:
            row_to_write = [emp_id, employee_name,
                            todo.get('completed'),
                            todo.get('title')]
            employee_writer.writerow(row_to_write)
