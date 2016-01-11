import sqlite3
import time
from db.metric import Metric

conn = sqlite3.connect('ncssbook.db')
conn.row_factory = sqlite3.Row

pics = {'Whale Shark: 'https://en.gravatar.com/userimage/99536151/1476b93b8ba85972473813b424831e12.jpg?size=200', 'Ryan': 'https://en.gravatar.com/userimage/99536151/b385ab26a1b12bfda017c9afa4bdf9cd.jpg?size=200', 'Leonard': 'https://en.gravatar.com/userimage/99536151/0503f8e3cfab0f1026c87b4f7399b980.jpg?size=200','Nicky': "/static/img/nicky.jpg", 'James': '/static/img/james.jpeg', 'Will': '/static/img/will.jpg', 'Renee': 'https://en.gravatar.com/userimage/99536151/56db2b8980a14007ae5b8219c3a44285.jpg?size=200', 'Sarah': 'https://en.gravatar.com/userimage/99536151/649c9279cc45d6b259350feb0fb71770.jpg?size=200', 'Simon': 'https://en.gravatar.com/userimage/99536151/66a2b732ba550aca5e255054b9d2a4ba.jpg?size=200', 'Alex': 'https://en.gravatar.com/userimage/99536151/a2da14e006d508e8512993f3647a32a0.jpg?size=200', 'Boran': 'https://en.gravatar.com/userimage/99536151/9657b7fb05d7b5239f30ecb8b50b9e79.jpg?size=200', 'Kassie': 'https://en.gravatar.com/userimage/99536151/72c52ffb6aef95cacd46f35e9872f91d.jpg?size=200', 'Jess': 'https://en.gravatar.com/userimage/99536151/25e16dd9d4f585b60fb1e272c154f7a8.jpg?size=200', 'Ben': 'https://en.gravatar.com/userimage/99536151/9bd1d0dbe694579807f64c168032d55f.jpg?size=200', 'Belle': 'https://en.gravatar.com/userimage/99536151/11d5b7bf40bcd605b147721559b171f3.jpg?size=200', 'Sandra': 'https://en.gravatar.com/userimage/99536151/ac6f0a63d2824676384e8642cf2683f7.jpg?size=200', 'Leonard': 'https://en.gravatar.com/userimage/99536151/3e35f5ea2b7fe99c9963993d8c08cf7f.jpg?size=200', 'Nick': 'https://en.gravatar.com/userimage/99536151/d3812dcd7e238e4885f1f92511fb77f9.jpg?size=200', 'Lindsey': 'https://en.gravatar.com/userimage/99536151/7bb9afe31fcb8c53a946346b2f9d6b1e.jpg?size=200', 'Sid': 'https://en.gravatar.com/userimage/99536151/56c321df945f2b4c81c2230c1073ac47.jpg?size=200', 'Ryan': 'https://en.gravatar.com/userimage/99536151/1476b93b8ba85972473813b424831e12.jpg?size=200', 'Connie': 'https://en.gravatar.com/userimage/99536151/97c3fbf82ef10fcb9c2b0891c2aa47db.jpg?size=200', 'Luke': 'https://en.gravatar.com/userimage/99536151/8fc18881a1731a4d14c4f4b594ff828a.jpg?size=200', 'Lachie': 'https://en.gravatar.com/userimage/99536151/134641ade908ad9e9a9e7027ca49db8a.jpg?size=200', 'Callan': 'https://en.gravatar.com/userimage/99536151/5c9e7c8770bf91ef0e3e78de494ee1a1.jpg?size=200', 'Tom': 'https://en.gravatar.com/userimage/99536151/42c690d1e469882e301a4c2ce20df19c.jpg?size=200', 'Elizabeth': 'https://en.gravatar.com/userimage/99536151/84770c8a088bbf4e826bef3239163613.jpg?size=200'}

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
        if self.fname in pics:
            self.pic = pics[self.fname]
        else:
            self.pic = "/static/img/profile_pic.jpg"

    def save(self):
        # This needs to update the user object with the returned ID
        cur = conn.execute('''
        INSERT into users (username, password, fname, lname, email, dob, postcode, country_code, signup_timestamp, image)
    VALUES(?,?,?,?,?,?,?,?,?,?)
    ''', (self.username, self.password, self.fname, self.lname, self.email, self.dob, self.postcode, self.country_code, int(time.time()), self.image))
        conn.commit()

    def follow(self, followee_user_id):
        if self.user_id is None:
            raise Exception("No user ID defined. Cannot add followers!")
        curr = conn.execute('''
        INSERT INTO following (follower, followee, timestamp)
        VALUES (?, ?, ?)
        ''', (self.user_id, followee_user_id, int(time.time())))
        conn.commit()
    
    #Returns a list of User objects of each person that is following the user
    def get_followers(self):
        if self.user_id is None:
            raise Exception("No user ID defined. Cannot get followers!")
        curr = conn.execute('''
        SELECT u.*
        FROM following f
        JOIN users u ON f.follower = u.id 
        WHERE f.followee = ?
        ''', (self.user_id,))
        
        followers = []
        for row in curr:
            followers.append(User(row["id"], row["username"], row["password"], row["fname"], row["lname"], row["email"], row["dob"], row["postcode"], row["country_code"], row["image"]))
        return followers
        
    #Returns a list of User objects of each person the user is following
    def get_followees(self):
        if self.user_id is None:
            raise Exception("No user ID defined. Cannot get followees!")
        curr = conn.execute('''
        SELECT u.*
        FROM following f
        JOIN users u ON f.followee = u.id 
        WHERE f.follower = ?
        ''', (self.user_id,))
    
        followees = []
        for row in curr:
            followees.append(User(row["id"], row["username"], row["password"], row["fname"], row["lname"], row["email"], row["dob"], row["postcode"], row["country_code"], row["image"])) 
        return followees

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
    def check_email_free(email):
        cur = conn.execute('''
        SELECT *
        FROM users
        WHERE email=?
        ''', (email,))
        row = cur.fetchone()
        if row is None:
            return True
        else:
            return False
    
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
		
    def get_user_aggregate_value(self, activity, metric_type):
        cur = conn.execute('''
        SELECT SUM(value) AS value
        FROM metrics
        WHERE user = ? AND activity = ? AND metric_type = ?
        ''', (self.user_id, activity, metric_type))
        row = cur.fetchone()
		
        return row["value"]
        
    def get_all_user_aggregate_values(self):
        cur = conn.execute('''
        SELECT activity, metric_type, SUM(value) AS value
        FROM metrics
        WHERE user = ?
        GROUP BY activity, metric_type
        ''', (self.user_id, ))
        return cur.fetchall()
        
    @staticmethod
    def find_user_by_fullname(search):
        cur = conn.execute('''
        SELECT *
        FROM users 
        WHERE fname || ' ' || lname LIKE ?
        ''', ('%'+search+'%', ))
        results = []
        for row in cur:
            u = User(row["id"], row["username"], row["password"], row["email"], row["fname"], row["lname"], row["dob"], row["postcode"], row["country_code"], row["image"])
            if u.fname in pics:
                u.pic = pics[u.fname]
            else:
                u.pic = "/static/img/profile_pic.jpg"
            results.append(u)
        return results
