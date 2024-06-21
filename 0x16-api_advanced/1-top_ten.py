#!/usr/bin/python3
"""
A function that prints the titles of the first 10 hot posts
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json().get("data").get("children")
    for post in data[:10]:
        print(post.get("data").get("title"))
