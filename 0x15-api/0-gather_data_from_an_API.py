#!/usr/bin/python3
""" A script to gather data from an API(REST API) """

from sys import argv
import requests



emp_id = argv[1]

emp_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
emp_response = requests.get(emp_url)
emp_data = emp_response.json()
emp_name = emp_data.get("name")

todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"
todos_response = requests.get(todos_url)
todos_data = todos_response.json()

total_tasks = len(todos_data)
completed_tasks = [task for task in todos_data if task.get("completed")]
number_of_completed_tasks = len(completed_tasks)

print(f"Employee {emp_name} is done with tasks\
      ({number_of_completed_tasks}/{total_tasks}):")

for task in completed_tasks:
    print("\t" + task.get("title"))
