#!/usr/bin/python3
"""
module: 1-top_ten.py
"""

import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    try:
        response = requests.get(url, headers={"User-Agent": "Gibexz"})

        if response.status_code != 200:
            print(response.status_code)
            print("None")
            return

        data = response.json()
        if "data" in data and "children" in data["data"]:
            posts_dict = data["data"]["children"]

            for post in posts_dict:
                print(post["data"]["title"])

            else:
                print("None")
                return

    except Exception as e:
        print("None")
        return
