#!/usr/bin/python3
""" handle Reddit API recursively """
import requests


def get_title(obj, hot_list):
    if type(obj) is list:
        for el in obj:
            if type(el) is dict:
                get_title(el, hot_list)
    elif type(obj) is dict:
        for key, val in obj.items():
            if key == 'title':
                hot_list.append(obj.get(key))
            elif type(val) is dict:
                get_title(val, hot_list)
            elif type(val) is list:
                get_title(val, hot_list)
    return hot_list


def recurse(subreddit, hot_list=[]):
    url = "https://www.reddit.com/r/{}/{post_type}.json".format(
        subreddit, post_type='hot')

    response = requests.get(url,
                            headers={"User-agent": "Any thing"},
                            allow_redirects=False)

    try:
        data = response.json()

        return get_title(data, hot_list)

    except Exception:
        print(None)
