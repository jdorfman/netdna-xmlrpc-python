#!/usr/bin/python

from xmlrpclib import ServerProxy
from hashlib import sha256
from datetime import datetime, timedelta

api_key = 'jdorfmantgm01qv10sk58rtarv4vfyk3mn5g5'
user_id = '0000'

def cache_purge(url):
    # Make sure pytz is installed: easy_install --upgrade pytz
    from pytz import timezone
    date = datetime.now(timezone('America/Los_Angeles')).replace(microsecond=0).isoformat() # Must be 'America/Los_Angeles' always!
    authString = sha256(date + ":" + api_key + ":purge").hexdigest()
    print authString
    sp = ServerProxy('http://api.netdna.com/xmlrpc/cache')
    return sp.cache.purge(user_id, authString, date, url)

print cache_purge('http://cdn.86400.io/beta03/app/images/maxcdn-logo-small.png')
