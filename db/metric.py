import sqlite3
import datetime

conn = sqlite3.connect("ncssbook.db")
conn.row_factory = sqlite3.Row

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
        INSERT INTO metrics(user, activity, timestamp, metric_type, value, submit_timestamp)
            VALUES (?, ?, ?, ? ,?, ?)
        ''', (self.user, self.activity, self.timestamp, self.metric_type, self.value, submit_timestamp))
        conn.commit()
        
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
		
    @staticmethod	
    def get_aggregate_value(activity, metric_type):
        cur = conn.execute('''
		SELECT SUM(value) AS value
		FROM metrics
		WHERE activity = ? AND metric_type = ?
        ''', (activity, metric_type))
        row = cur.fetchone()
	
        return row["value"]
	
	
	
		
