import sqlite3 as lite
import sys

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

        


update_played_details("1")
        
    
