#!/usr/bin/python3
""" requests module """
import csv
import requests
from sys import argv

if __name__ == "__main__":

    emp_id = argv[1]
    with open('{}.csv'.format(emp_id), mode='w') as employee_file:
        employee_writer = csv.writer(employee_file,
                                     delimiter=',',
                                     quotechar='"',
                                     quoting=csv.QUOTE_ALL)
        todo_list = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                                 .format(emp_id)).json()
        employee = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                                .format(emp_id)).json()  # list of dicts
        employee_name = employee.get('name')

        for todo in todo_list:
            row_to_write = [emp_id, employee_name,
                            todo.get('completed'),
                            todo.get('title')]
            employee_writer.writerow(row_to_write)
