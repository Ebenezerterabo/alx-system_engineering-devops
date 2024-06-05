#!/usr/bin/python3
"""
A script to gather data from an API(REST API) and export to CSV
"""

import json
import requests
from sys import argv


def main():
    """main function"""
    # get employee id
    emp_id = int(argv[1])
    # Fetch employee data
    emp_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    emp_response = requests.get(emp_url)
    emp_data = emp_response.json()
    # Fetch employee tasks(todo)
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    # prepare data for JSON
    task_data = {
        emp_id: []
    }
    for task in todos_data:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": emp_data.get("username")
        }
        task_data[emp_id].append(task_dict)
    # write to JSON
    with open(f"{emp_id}.json", mode="w") as json_file:
        json.dump(task_data, json_file)


if __name__ == "__main__":
    main()
