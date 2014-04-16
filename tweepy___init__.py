# Tweepy
# Copyright 2009-2010 Joshua Roesslein
# See LICENSE for details.

"""
Tweepy Twitter API library
"""
__version__ = '2.3'
__author__ = 'Joshua Roesslein'
__license__ = 'MIT'

from tweepy_models import Status, User, DirectMessage, Friendship, SavedSearch, SearchResults, ModelFactory, Category
from tweepy_error import TweepError
from tweepy_api import API
from tweepy_cache import Cache, MemoryCache, FileCache
from tweepy_auth import OAuthHandler
from tweepy_streaming import Stream, StreamListener
from tweepy_cursor import Cursor

# Global, unauthenticated instance of API
api = API()

def debug(enable=True, level=1):

    import httplib
    httplib.HTTPConnection.debuglevel = level

