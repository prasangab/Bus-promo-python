import httplib
import json
import sqlite3
import pafy


#sqlite database connection..........

con = sqlite3.connect('bpclient.db')

with con:
    
    cur = con.cursor()

    cur.execute("SELECT * FROM ad_data")
    while True:
      
        row = cur.fetchone()
        
        if row == None:
            break
            
        #print row[0], row[1]

        if row[0] == 'root':
            rootid = row[1]
            #print "root id ="+rootid
        if row[0] == 'lastget':
            flagdate = row[1]
            #print "flagdate ="+flagdate

            

#send GET request to server....
            
host = 'localhost:8000'
h = httplib.HTTP(host)


h.putrequest('GET','/getUpdateFlag?rootid='+rootid)

h.endheaders()
returncode, returnmsg, headers = h.getreply()
x='';
if returncode == 200:  #Connection successfull
    f = h.getfile()
    x=x+ f.read()
y=json.loads(x)

last_modified = y['lastupdate']

if last_modified > flagdate:

    h.putrequest('GET', '/getnewData?rootid='+rootid+'&myflagdate='+flagdate)

    h.endheaders()
    returncode, returnmsg, headers = h.getreply()
    x='';
    if returncode == 200:  #Connection successfull
        f = h.getfile()
        x=x+ f.read()
    y=json.loads(x)

    #print y


    if y['error']== 'ok':

        result = y['results']

        for i in range(0, len(result)):
            #print result[i]
            

       #video downloader.........
            
            url = y['results'][i]['storage_location']
            video = pafy.new(url)
            streams = video.streams

            #for s in streams:
            #   print(s.resolution, s.extension, s.get_filesize(), s.url)

            best = video.getbest()

            best = video.getbest(preftype="webm")

            #filename = best.download(quiet=False)
            filename = best.download(filepath = "F:" )

            result = y['results'][i]
            #print result

            start_date = y['results'][i]['added']
            end_date = y['results'][i]['removed']
            link = y['results'][i]['storage_location']
            ad_id = y['results'][i]['advert_id']
            today = y['date']
    

            cur.execute("INSERT INTO ad_details (ad_id, start_date, end_time, link) VALUES (?, ?, ?, ?)",(ad_id, start_date, end_date, link))
            """
            cur.execute("SELECT * FROM ad_details")
            while True:
      
                row = cur.fetchone()
        
                if row == None:
                    break
            
                print row[0], row[1], row[2], row[3]"""

        cur.execute("DELETE FROM ad_data WHERE data = 'lastget'")
        cur.execute("INSERT INTO ad_data (data, content) VALUES (?, ?)",('lastget', today))
        """cur.execute("SELECT * FROM ad_data")
        while True:
      
            row = cur.fetchone()
        
            if row == None:
                break
            
            print row[0], row[1]"""
    

    else:
        print "error occured..."


def update_played_details(played_ad_id):
    con = lite.connect('bpclient.db')
    with con:
    
        cur = con.cursor()

        cur.execute("SELECT round FROM played_details WHERE ad_id=:id",{"id":played_ad_id})
        con.commit()
        while True:
      
            row = cur.fetchone()
        
            if row == None:
                break
            
            last_round = row[0]
            print last_round
            new_round = int(last_round) + 1
            print str(new_round)

        cur.execute("UPDATE played_details SET round=? WHERE ad_id=?", (str(new_round), played_ad_id))        
        con.commit()
