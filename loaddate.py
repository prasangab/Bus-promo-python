import sqlite3 as lite
import sys
import json
import httplib


con = lite.connect('bpclient.db')
with con:
    
    cur = con.cursor()
    
    
    cur.execute("DROP TABLE IF EXISTS played_details")
    cur.execute("CREATE TABLE played_details(ad_id VARCHAR, date DATE, round INT)")
    cur.execute("INSERT INTO played_details VALUES(1,'2015-08-02', 5)")
    cur.execute("INSERT INTO played_details VALUES(2,'2015-08-02', 9)")

    y=[]

       
    cur.execute("SELECT * FROM played_details")
    while True:
      
        row = cur.fetchone()
        
        if row == None:
            break
            
        #print row[0], row[1], row[2]

        all_data = {"id": row[0], "licno": row[1], "time": row[2]}
        y.append(all_data)
        #print all_data
        #print y
    z = {"data":y}
    #print z

    d = (z)
    jsonarray = json.dumps(d, ensure_ascii=False)
    #print jsonarray

    host = 'localhost:8000'
    h = httplib.HTTP(host)


    h.putrequest('GET','/loadDatato?dayreport='+jsonarray)

    h.endheaders()
    returncode, returnmsg, headers = h.getreply()
    xx='';
    if returncode == 200:  #Connection successfull
        f = h.getfile()
        xx=xx+ f.read()
    try:
        #print h.getreply()
        y=json.loads(xx)
    except:
        print "done"

    
    
