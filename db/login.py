import sqlite3
import time
from db.metric import Metric

conn = sqlite3.connect('ncssbook.db')
conn.row_factory = sqlite3.Row


class User:
    
    def __init__(self, user_id=None, username="", password="", email="", fname="", lname="", dob="", postcode="", country_code="", signup_timestamp=0, image=""):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.fname = fname
        self.lname = lname
        self.email = email
        self.dob = dob
        self.postcode = postcode
        self.country_code = country_code
        self.image = image

    def load(self):
        cur = conn.execute('''
            SELECT *
            FROM users
            WHERE id = ?
            ''', (self.user_id,))
        row = cur.fetchone()
        self.username = row["username"]
        self.password = row["password"]
        self.fname = row["fname"]
        self.lname = row["lname"]
        self.email = row["email"]
        self.dob = row["dob"]
        self.postcode = row["postcode"]
        self.country_code = row["country_code"]
        self.signup_timestamp = row["signup_timestamp"]
        self.image = row["image"]

    def save(self):
        # This needs to update the user object with the returned ID
        cur = conn.execute('''
        INSERT into users (username, password, fname, lname, email, dob, postcode, country_code, signup_timestamp, image)
    VALUES(?,?,?,?,?,?,?,?,?,?)
    ''', (self.username, self.password, self.fname, self.lname, self.email, self.dob, self.postcode, self.country_code, int(time.time()), self.image))
        conn.commit()

    def get_activities(self):
        if self.user_id is None:
            raise Exception("No user ID defined. Cannot get activities!")
            
        cur = conn.execute('''
            SELECT DISTINCT activity
            FROM metrics
            WHERE ? = user
            ''', (self.user_id,))
        activities = []
            
        for row in cur:
            activities.append(row["activity"])
        
        return activities
    
    #Returns all of the metrics a user has
    def get_all_metrics(self):
        if self.user_id is None:
            raise Exception("No user ID defined. Cannot get metrics!")
        
        cur = conn.execute('''
            SELECT *
            FROM metrics
            WHERE user = ?
        ''', (self.user_id,))
        
        metrics = []
        for row in cur:
            metrics.append(Metric(row["id"], row["user"], row["activity"], row["timestamp"], row['metric_type'], row['value']))
        return metrics
    
    #Returns all of the metrics for a specific metric
    def get_activity_metrics(self, activity):
        if self.user_id is None:
            raise Exception("No user ID defined. Cannot get metrics for activity " +  activity)
       
        cur = conn.execute('''
        SELECT * 
        FROM metrics
        WHERE user = ? AND activity = ?
        ''', (self.user_id, activity))
        
        metrics = []
        for row in cur:
            metrics.append(Metric(row["id"], row["user"], row["activity"], row["timestamp"], row['metric_type'], row['value']))
        return metrics
        
    @staticmethod
    def login(email, password):
        cur = conn.execute('''
        SELECT *
        FROM users
        WHERE email=? AND password=?
        ''', (email, password))
        row = cur.fetchone()
        if row is not None:
            return User(*row)
        else:
             return None

    @staticmethod
    def delete(username):
        cur = conn.execute('''
        DELETE FROM users WHERE username = ?''', (username))
        conn.commit()
