#! /usr/bin/python

from xmlrpclib import ServerProxy
from hashlib import sha256
from datetime import datetime, timedelta
from pytz import timezone

apiKey = 'asdasdasdasdasdj7bcakd6wb6kwnhgb34pjx99'
apiUserId = '0000'

def pushzoneListZones():
	global apiKey, apiUserId
	date = datetime.now(timezone('America/Los_Angeles')).replace(microsecond=0).isoformat()
	authString = sha256(date + ":" + apiKey + ":listZones").hexdigest()
	sp = ServerProxy('http://api.netdna.com/xmlrpc/pushzone')
	return sp.pushzone.listZones(apiUserId, authString, date)

print pushzoneListZones()
