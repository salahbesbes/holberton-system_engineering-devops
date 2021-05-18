#!/usr/bin/python3
""" handle Reddit API recursively """
import requests


def get_title(subreddit, hot_list, after=True):
    url = "https://www.reddit.com/r/{}/{post_type}.json".format(
        subreddit, post_type='hot')
    params = {'after': after,
              'limit': 100}
    response = requests.get(url,
                            headers={"User-agent": "Any thing"},
                            allow_redirects=False,
                            params=params)

    try:
        data = response.json()
        list_items = data['data']['children']
        after = data.get('data').get('after')

        if after:
            for item in list_items:
                hot_list.append(item.get('title'))
            get_title(subreddit, hot_list, after)

        return hot_list
    except Exception:
        print(None)


def recurse(subreddit, hot_list=[]):
    return get_title(subreddit, hot_list)
