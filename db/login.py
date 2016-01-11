import sqlite3
import time

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

    @staticmethod
    def login(username, password):
        cur = conn.execute('''
        SELECT *
        FROM users
        WHERE username=? AND password=?
        ''', (username, password))
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
