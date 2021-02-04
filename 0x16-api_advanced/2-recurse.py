#!/usr/bin/python3
"""Returns a list containing the titles of all hot articles for a
given subreddit"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """List containing the titles of all hot articles for a given subreddit"""

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    r = requests.get(url, headers={'user-agent': 'projectapi 0.1'},
                     params={'after': after})
    after = r.json().get('data').get('after')

    if after is None:
        return hot_list
    if r.status_code == 200:
        r = r.json()
        hot = r.get('data').get('children')
        for child in hot:
            hot_list.append(child.get('data').get('title'))
        return recurse(subreddit, hot_list, after)
    else:
        return (None)
