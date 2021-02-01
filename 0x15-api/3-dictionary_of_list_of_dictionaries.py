#!/usr/bin/python3
"""This module is TO gather data from an API"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    r = requests.get('https://jsonplaceholder.typicode.com/users/')
    r = r.json()
    ids_usernames = {}
    for user in r:
        ids_usernames[user.get("id")] = user.get("username")

    todo_ls = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    task_dic = {}
    for task in todo_ls:
        user_id = task.get("userId")
        username = ids_usernames[user_id]
        tsk = task.get("title")
        completed = task.get("completed")
        d = {"username": username, "task": tsk, "completed": completed}
        if task_dic.get(user_id):
            task_dic.get(user_id).append(d)
        else:
            task_dic[user_id] = [d]

    with open('todo_all_employees.json', 'w', newline='') as f:
        json.dump(task_dic, f)
