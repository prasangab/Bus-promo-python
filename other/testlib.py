import httplib
import json
import sqlite3

host = 'localhost:8000'
h = httplib.HTTP(host)
h.putrequest('GET', '/getnewData?rootid=02&myflagdate=2015-07-15')
h.endheaders()
returncode, returnmsg, headers = h.getreply()
x='';
if returncode == 200:  #OK
    f = h.getfile()
    x=x+ f.read()
y=json.loads(x)

print y 

if y['error']== 'ok':
    print y['results'][0]['storage_location']
    conn = sqlite3.connect('test.db')
    print "Opened database successfully";

else:
    print "error occured..."

