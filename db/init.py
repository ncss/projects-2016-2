import sqlite3

DATABASE_NAME = 'ncssbook.db'

conn = sqlite3.connect(DATABASE_NAME)

cur = conn.cursor()

cur.execute('''
CREATE TABLE users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        email TEXT NOT NULL,
        fname TEXT NOT NULL,
        lname TEXT NOT NULL,
        dob TEXT,
        postcode TEXT NOT NULL,
        country_code TEXT NOT NULL,
        signup_timestamp INTEGER NOT NULL,
        image BLOB
        );
''')


cur.execute('''
CREATE TABLE following(
        follower INTEGER references users(id),
        followee INTEGER references users(id),
        timestamp INTEGER NOT NULL,
        PRIMARY KEY (follower, followee)
        );
''')

cur.execute('''
CREATE TABLE metrics(
        id INTEGER PRIMARY KEY,
        user INTEGER references users(id),
        activity INTEGER references activities(id),
        metric_type INTEGER references metric_types(id),
        value REAL NOT NULL,
        timestamp INTEGER NOT NULL,
        submit_timestamp INTEGER NOT NULL
        );
''')
