import sqlite3
import time

conn = sqlite3.connect('ncssbook.db')
conn.row_factory = sqlite3.Row


class User:
    
    def __init__(self, user_id=None, username="", password="", fname="", lname="", email="", dob="", postcode="", country_code="", image=""):
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
        
    @staticmethod
    def login(username, password):
        cur = conn.execute('''
        SELECT *
        FROM users
        WHERE username=? AND password=?
        ''', (username, password))
        row = cur.fetchone()
        if row is not None:
             return User(**row)
        else:
             return None

    @staticmethod
    def delete(username):
        cur = conn.execute('''
        DELETE FROM users WHERE username = ?''', (username))
        conn.commit()
