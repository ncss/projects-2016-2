import sqlite3

conn = sqlite3.connect('ncssbook.db')

def login(username, password):
    cur = conn.execute('''
    SELECT id
    FROM users
    WHERE user=? AND pass=?
    ''', (username, password))
    row = cur.fetchone()
    user_id = None if row is None else row['id']
    conn.commit()
    return user_id
