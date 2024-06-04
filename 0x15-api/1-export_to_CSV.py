#!/usr/bin/python3
"""
A script to gather data from an API(REST API)
"""

import csv
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
    # prepare data for CSV
    task_data = []
    for task in todos_data:
        task_dict = {
            "USER_ID": emp_id,
            "USERNAME": emp_data.get("username"),
            "TASK_COMPLETED_STATUS": task.get("completed"),
            "TASK_TITLE": task.get("title")
        }
        task_data.append(task_dict)
    # write to CSV
    with open(f"{emp_id}.csv", mode="w") as csv_file:
        fieldnames = ["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        for task in task_data:
            writer.writerow(task)


if __name__ == "__main__":
    main()
