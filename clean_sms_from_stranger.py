'''
author: winsweet@gmail.com
'''

import android

droid = android.Android()

data = droid.queryContent( 'content://com.android.contacts/data/phones' )
allphonenumber = set( [ i['data1'].replace(' ','')[-8:] for i in data[1] ] )

sms=droid.smsGetMessages(False)
for i in sms[1]:
  if i['address'][-8:] not in allphonenumber:
    droid.smsDeleteMessage( i['_id'] )
