#!/usr/bin/python

from xmlrpclib import ServerProxy
from hashlib import sha256
from datetime import datetime, timedelta
from pytz import timezone

api_key = 'jdorfmanasdsadb6kwnhgb34pjx99'
user_id = '0000'

def cache_purgeallcache(zone):
    date = datetime.now(timezone('America/Los_Angeles')).replace(microsecond=0).isoformat()
    authString = sha256(date + ":" + api_key + ":purgeAllCache").hexdigest()
    print authString
    sp = ServerProxy('http://api.netdna.com/xmlrpc/cache')
    return sp.cache.purgeAllCache(user_id, authString, date, zone)
    
print cache_purgeallcache('static') #static represents my pull zone name
