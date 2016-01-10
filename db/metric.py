import sqlite3
import datetime

conn = sqlite3.
class Metric:
    id = None
    user = None
    activity = None
    timestamp = None
    metric_type = None
    value = None
    
    def __init__(self, id="", user="", activity="", timestamp="", metric_type="", value=""):
        self.user = user
        self.activity = activity
        self.timestamp = timestamp
        self.metric_type = metric_type
        self.id = id
        self.value = value
    
    #SUBMIT_TIMESTAMP NEEEDED!!
    def save(self):
        submit_timestamp = datetime.datetime.now()
        
        curs = conn.cursor()
        curs.execute('''
        INSERT INTO metrics(id, user, activity, timestamp, metric_type, value, submit_timestamp)
            VALUES (?, ?, ?, ?, ? ,?, ?)
        ''', ())
        
    def load(self):
        pass
    
    