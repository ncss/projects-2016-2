import sqlite3

conn = sqlite3.connect('ncssbook.db')


class User:
    userCount = 0
    
    def __init__(self, username, password, *, user_id=None, fname="", lname="", email="", dob="", postcode="", country_code="", user_permissions="", signup_timestamp="", image=""):
       self.username = username
       self.password = password
       self.user_id = user_id
       self.fname = fname
       self.lname = lname
       self.email = email
       self.dob = dob
       self.postcode = postcode
       self.country_code = country_code
       self.user_permissions = user_permissions
       self.signup_timestamp = signup_timestamp
       self.image = image

    def login(self):
        cur = conn.execute('''
        SELECT *
        FROM users
        WHERE username=? AND password=?
        ''', (self.username, self.password))
        row = cur.fetchone()
        conn.commit()
        return row
        conn.commit()


    def register(self):
        cur = conn.execute('''
        INSERT into users VALUES(?,?,?,?,?,?,?,?,?,?)''', (username, password, fname, lname, email, dob, postcode, country_code, user_permissions, signup_timestamp, image))
        
        return cur.lastrowid

   
    def delete(self):
        cur = conn.execute('''
        DELETE FROM users WHERE username = ?''', (self.username))
        return user_id
