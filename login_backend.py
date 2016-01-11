import db.login as db

def set_login_cookie(response, email):
    response.set_secure_cookie("email", email) 

def get_login_cookie(response):
    email = response.get_secure_cookie("email")
    return email

def login(response,email,password):
    '''
    -Check if logged in
    -Call db function
    -Cookies
    '''
    cookie_email = get_login_cookie(response)
    if cookie_email is not None:
        user = db.User
        user.email = cookie_email
        return user.load()
    else:
        user = db.User.login(email, password)
        if user is None:
            return None
        set_login_cookie(response, user.email)
        return user






