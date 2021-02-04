#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    r = requests.get(url, headers={'user-agent': 'projectapi 0.1'},
                     params={'limit': 10})
    if r.status_code == 200:
        r = r.json()
        hot = r.get('data').get('children')
        for child in hot:
            print(child.get('data').get('title'))
    else:
        print(None)
