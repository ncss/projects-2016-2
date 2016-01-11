import db.login as db

def set_login_cookie(response, user_id):
    response.set_secure_cookie("user_id", str(user_id)) 

def get_login_cookie(response):
    user_id = int(response.get_secure_cookie("user_id"))
    return user_id

def login(response,email,password):
    '''
    -Check if logged in
    -Call db function
    -Cookies
    '''
    cookie_user_id = get_login_cookie(response)
    if cookie_user_id is not None:
        user = db.User()
        user.user_id = cookie_user_id
        return user.load()
    else:
        user = db.User.login(email, password)
        if user is None:
            return None
        set_login_cookie(response, user.user_id)
        return user






