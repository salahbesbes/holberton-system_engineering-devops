#!/usr/bin/python3
""" limit the queries  Reddit API """
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(
        subreddit)
    params = {'limit': 10}

    response = requests.get(url,
                            headers={"User-agent": "Any thing"},
                            allow_redirects=False,
                            params=params)

    try:
        response = response.json()
        list_items_got = response['data']['children']
        for item in list_items_got:
            print(item['data']['title'])
    except Exception:
        print(None)
