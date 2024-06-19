#!/usr/bin/python3
import requests

"""
A function to get the number of subscribers of a subreddit
"""


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        subscribers = response.json()["data"]["subscribers"]
        return subscribers
    else:
        return 0
