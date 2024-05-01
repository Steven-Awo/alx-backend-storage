#!/usr/bin/env python3
"""
Using a web cache and also a tracker
"""

import requests

import redis

from functools import wraps

store = redis.Redis()


def count_url_access(method):
    """ Decorator thats for counting the nuber of
    times that a URL has been accessed """
    @wraps(method)
    def wrapper(url):
        cached_key = "cached:" + url
        cached_data = store.get(cached_key)
        if cached_data:
            return cached_data.decode("utf-8")

        count_key = "count:" + url
        html = method(url)

        store.incr(count_key)
        store.set(cached_key, html)
        store.expire(cached_key, 10)
        return html
    return wrapper


@count_url_access
def get_page(url: str) -> str:
    """ Returning the HTML's content of the specific url """
    res = requests.get(url)
    return res.text

