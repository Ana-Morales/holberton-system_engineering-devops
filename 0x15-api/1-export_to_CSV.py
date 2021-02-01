#!/usr/bin/python3
"""This module is TO gather data from an API"""

if __name__ == "__main__":

    import csv
    import requests
    import sys

    r = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1]))
    r = r.json()
    name = r.get("username")
    todo_ls = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    with open('{}.csv'.format(sys.argv[1]), 'w', newline='') as f:
        csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todo_ls:
            if task.get("userId") == int(sys.argv[1]):
                row = [sys.argv[1], name, task.get("completed"),
                       task.get("title")]
                csv_writer.writerow(row)
