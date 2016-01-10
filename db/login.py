import sqlite3

conn = sqlite3.connect('ncssbook.db')


class User:
    
    def __init__(self, user_id=None, username="", password="", fname="", lname="", email="", dob="", postcode="", country_code="", user_permissions="", signup_timestamp="", image=""):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.fname = fname
        self.lname = lname
        self.email = email
        self.dob = dob
        self.postcode = postcode
        self.country_code = country_code
        self.user_permissions = user_permissions
        self.signup_timestamp = signup_timestamp
        self.image = image

    def load(self):
	cur = conn.execute('''
        SELECT *
        FROM users
        WHERE user_id = ?
        ''', (user_id,))
        row = cur.fetchone()
        self.username = row["username"]
        self.password = row["password"]
        self.fname = row["fname"]
        self.lname = row["lname"]
        self.email = row["email"]
        self.dob = row["dob"]
        self.postcode = row["postcode"]
        self.country_code = row["country_code"]
        self.user_permissions = row["user_permissions"]
        self.signup_timestamp = row["signup_timestamp"]
        self.image = row["image"]

    def save():
        cur = conn.execute('''
        INSERT into users (username, password, fname, lname, email, dob, postcode, country_code, signup_timestamp, image)
	VALUES(?,?,?,?,?,?,?,?,?,?)
	''', (self.username, self.password, self.fname, self.lname, self.email, self.dob, self.postcode, self.country_code, self.signup_timestamp, self.image))

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
    def get_user():
        return User()

    @staticmethod
    def register(username="", password="", fname="", lname="", email="", dob="", postcode="", country_code="", user_permissions="", signup_timestamp="", image=""):
        cur = conn.execute('''
        INSERT into users (username, password, fname, lname, email, dob, postcode, country_code, signup_timestamp, image)
	VALUES(?,?,?,?,?,?,?,?,?,?)
	''', (username, password, fname, lname, email, dob, postcode, country_code, signup_timestamp, image))

    @staticmethod
    def delete(username):
        cur = conn.execute('''
        DELETE FROM users WHERE username = ?''', (username))
