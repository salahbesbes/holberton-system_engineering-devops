#!/usr/bin/python3
""" handle Reddit API recursively """
import requests
import re


def search_occurence(title, occurrence):
    list_words = title.split()
    # todo: try to delete this line
    list_words = [w.lower() for w in list_words]

    # count occurence
    for word in list_words:
        if word in occurrence.keys():
            occurrence[word] += 1

    return occurrence


def search_in_titles(subreddit, word_list, occurrence, after=True):
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
        # after is an ttribut that tell us that we can found more data
        after = data.get('data').get('after')
        for item in list_items:
            result = search_occurence(item['data']['title'], occurrence)

        if after:
            result = search_in_titles(
                subreddit, word_list, result, after)
        else:
            # delete any item have  val == 0
            result = {key: val for key,
                      val in result.items() if val != 0}

            for key, val in sorted(result.items(), key=lambda el: el[1], reverse=True):
                print('{}: {}'.format(key, val))

    except Exception:
        print()


def count_words(subreddit, word_list):

    search = [re.sub(r'[^a-z]', '', w.lower()) for w in word_list]
    search = set(search)
    occurrence = {key: 0 for key in search}
    return search_in_titles(subreddit, search, occurrence)
