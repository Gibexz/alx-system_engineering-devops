#!/usr/bin/python3
"""
module: 0-subs.py
"""

import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns
    the number of subscribers
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    try:
        response = requests.get(url, headers={"User-Agent": "Gibexz"})
        if response.status_code != 200:
            return 0
        data = response.json()
        if "data" in data and "subscribers" in data["data"]:
            return data["data"]["subscribers"]
        else:
            return 0

    except Exception as e:
        return 0
