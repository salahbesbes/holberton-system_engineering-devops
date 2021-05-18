#!/usr/bin/python3
""" a function that queries the Reddit API """
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url,
                            headers={"User-agent": "Any thing"},
                            allow_redirects=False).json()
    try:
        return response["data"]["subscribers"]
    except Exception:
        return 0
