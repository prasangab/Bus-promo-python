import sqlite3 as lite
import sys


con = lite.connect('bpclient.db')
with con:
    
    cur = con.cursor()    
    
    cur.execute("DROP TABLE IF EXISTS ad_details")
    cur.execute("CREATE TABLE ad_details(ad_id VARCHAR, start_date DATE, end_time DATE, link VARCHAR)")
    cur.execute("INSERT INTO ad_details VALUES(1,'2015-06-02','2015-08-20', 'https://youtu.be/zHdoczkqEPA')")
    cur.execute("INSERT INTO ad_details VALUES(2,'2015-07-02','2015-09-20', 'https://youtu.be/Xv9dDiGRwVI')")
    
    
    cur.execute("DROP TABLE IF EXISTS played_details")
    cur.execute("CREATE TABLE played_details(ad_id VARCHAR, date DATE, round INT)")
    cur.execute("INSERT INTO played_details VALUES(1,'2015-08-02', 5)")
    cur.execute("INSERT INTO played_details VALUES(2,'2015-08-02', 9)")

    cur.execute("DROP TABLE IF EXISTS ad_data")
    cur.execute("CREATE TABLE ad_data(data VARCHAR, content VARCHAR)")
    cur.execute("INSERT INTO ad_data VALUES('lastget', '2015-07-15')")
    cur.execute("INSERT INTO ad_data VALUES('lastput', '2015-08-03')")
    cur.execute("INSERT INTO ad_data VALUES('root', '02')")
    cur.execute("INSERT INTO ad_data VALUES('lisenno', '63-2233')")


    cur.execute("SELECT * FROM ad_details")
    while True:
      
        row = cur.fetchone()
        
        if row == None:
            break
            
        print row[0], row[1], row[2], row[3]

    cur.execute("SELECT * FROM played_details")
    while True:
      
        row = cur.fetchone()
        
        if row == None:
            break
            
        print row[0], row[1], row[2]

    cur.execute("SELECT * FROM ad_data")
    while True:
      
        row = cur.fetchone()
        
        if row == None:
            break
            
        print row[0], row[1]

        if row[0]== 'root':
            rootid = row[1]
            #print "root id ="+rootid
