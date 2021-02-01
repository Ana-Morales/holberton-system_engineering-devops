#!/usr/bin/python3
"""This module is TO gather data from an API"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    r = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1]))
    r = r.json()
    name = r.get("username")
    todo_ls = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    task_dic = {str(sys.argv[1]): []}
    for task in todo_ls:
        if task.get("userId") == int(sys.argv[1]):
            d = {}
            d["task"] = task.get("title")
            d["completed"] = task.get("completed")
            d["username"] = name
            task_dic[str(sys.argv[1])].append(d)
    with open('{}.json'.format(sys.argv[1]), 'w', newline='') as f:
        json.dump(task_dic, f)
