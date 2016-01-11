import db.login as db

def login(username,password):
    '''
    -Check if logged in
    -Call db function
    -Cookies
    '''
    return db.User.login(username, password)


