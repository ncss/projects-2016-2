import sqlite3
import datetime

conn = sqlite3.
class Metric:  
    def __init__(self, id="", user="", activity="", timestamp="", metric_type="", value=""):
        self.user = user
        self.activity = activity
        self.timestamp = timestamp
        self.metric_type = metric_type
        self.id = id
        self.value = value
    
    def save(self):
        submit_timestamp = datetime.datetime.now()
        
        curs = conn.cursor()
        curs.execute('''
        INSERT INTO metrics(id, user, activity, timestamp, metric_type, value, submit_timestamp)
            VALUES (?, ?, ?, ?, ? ,?, ?)
        ''', ())
        
    def load(self):
        cur = conn.execute('''
        SELECT *
        FROM metrics
        WHERE id = ?
        ''', (self.id,))
        row = cur.fetchone()
        self.user = row["user"]
        self.activity = row["activity"]
        self.timestamp = row["timestamp"]
        self.metric_type = row["metric_type"]
        self.id = row["id"]
        self.value = row["value"]
     
     
     

     
    
    