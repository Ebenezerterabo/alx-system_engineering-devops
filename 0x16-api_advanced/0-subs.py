#!/usr/bin/python3
"""
module for 0-subs
"""
import requests


def number_of_subscribers(subreddit):
    """
    A function to get the number of subscribers of a subreddit
    returns 0 if the subreddit doesn't exits
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "jeybenz"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        if "data" in data and "subscribers" in data["data"]:
            return data["data"]["subscribers"]
        else:
            return 0
    return 0
