#!/usr/bin/python3
"""Returns the number of subscribers (not active users, total subscribers) for
a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    r = requests.get(url, headers={'user-agent': 'projectapi 0.1'})
    if r.status_code == 200:
        r = r.json()
        subscribers = r.get('data').get('subscribers')
        return subscribers
    return 0
