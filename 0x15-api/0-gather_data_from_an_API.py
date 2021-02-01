#!/usr/bin/python3
"""This module is TO gather data from an API"""

if __name__ == "__main__":

    import requests
    import sys

    r = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1]))
    r = r.json()
    name = r.get("name")

    todo_ls = requests.get('https://jsonplaceholder.typicode.com/todos')
    todo_ls = todo_ls.json()
    tasks_done = []
    total = 0
    for task in todo_ls:
        if task.get("userId") == int(sys.argv[1]):
            total += 1
            if task.get("completed") is True:
                tasks_done.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(name,
                                                          len(tasks_done),
                                                          total))
    for t in tasks_done:
        print("\t {}".format(t))
