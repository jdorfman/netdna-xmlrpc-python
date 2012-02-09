#! /usr/bin/python

# easy_install or pip install: xmlrpclib hashlib datetime pytz

from xmlrpclib import ServerProxy
from hashlib import sha256
from datetime import datetime, timedelta
from pytz import timezone

# get your key and id here: NetDNA: https://login.netdna.com/account/api | MaxCDN: https://login.maxcdn.com/account/api
apiKey = 'jdorfmantgm01qv10sk58rtarv4vfyk3mn5g5'
apiUserId = '0000'

def pullzoneCreate(zoneName, originUrl, vanityUrl):
    global apiKey, apiUserId
    date = datetime.now(timezone('America/Los_Angeles')).replace(microsecond=0).isoformat() # Must be 'America/Los_Angeles' always!
    authString = sha256(date + ":" + apiKey + ":create").hexdigest()
    zoneInfo = {'name': zoneName, 'origin': originUrl, 'vanity_domain': vanityUrl}
    sp = ServerProxy('http://api.netdna.com/xmlrpc/pullzone')
    return sp.pullzone.create(apiUserId, authString, date, zoneInfo)

# Add your values below:
print pullzoneCreate('pythonzone',
                     'http://www.yourdomain.com',
                     'cdn.yourdomain.com')

# Should see something like:
# {'cdn_url': 'pythonzone.companyalias.netdna-cdn.com', 'id': '34995', 'vanity_ip': '69.174.57.101'}

