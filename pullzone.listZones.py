#! /usr/bin/python

from xmlrpclib import ServerProxy
from hashlib import sha256
from datetime import datetime, timedelta
from pytz import timezone

apiKey = 'asdasdasdsadkd6wb6kwnhgb34pjx99'
apiUserId = '0000'

def pullzoneListZones():
    global apiKey, apiUserId
    date = datetime.now(timezone('America/Los_Angeles')).replace(microsecond=0).isoformat() # Must be 'America/Los_Angeles' always!
    authString = sha256(date + ":" + apiKey + ":listZones").hexdigest()
    sp = ServerProxy('http://api.netdna.com/xmlrpc/pullzone')
    return sp.pullzone.listZones(apiUserId, authString, date)

print pullzoneListZones()
