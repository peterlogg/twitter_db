#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Daddy Bear's Twitter client."""
import os
import random
import tweepy
from typing import List
import time

API_KEY = os.getenv("API_KEY")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")


def do_retweets() -> None:
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    while 2 > 1:
        ids = list()
        searches = [
            "\"daddy bear\"", "\"bus driver\"", "peckham", "bertie", "pancake",
            "plop"
        ]
        for search_term in searches:
            ids += _return_tweets(search_term, api)
        random.shuffle(ids)
        for id_ in ids:
            try:
                api.retweet(id_)
            except:
                continue
            time.sleep(60)


def _return_tweets(search_term: str, api: tweepy.API) -> List[int]:
    """Get list of tweet IDs"""
    return [
        tweet.id for tweet in api.search(q=search_term, lang="en", count=100)
    ]


if __name__ == "__main__":
    do_retweets()
