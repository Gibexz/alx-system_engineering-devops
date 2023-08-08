#!/usr/bin/python3
"""
module: 2-recurse.py
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    function that recursively queries the Reddit API and prints
    the titles of the hot posts listed for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    if after:
        url = url + f"?after={after}"
    header = {"User-Agent": "Gibexz"}
    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code != 200:
        print("None")
        return
    dataa = response.json()
    if "data" in dataa and "children" in dataa["data"]:
        posts_dict = dataa["data"]["children"]

        for post in posts_dict:
            hot_list.append(post["data"]["title"])

        after = dataa["data"]["after"]
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list

    else:
        return None
