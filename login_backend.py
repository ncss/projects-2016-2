import db.login as db

def set_login_cookie(response, user_id):
    response.set_secure_cookie("user_id", user_id) 
    response.redirect("/")

def get_login_cookie(response):
    user_id = response.get_secure_cookie("user_id")
    return user_id

def login(response,user_id,password):
    '''
    -Check if logged in
    -Call db function
    -Cookies
    '''
    user_id = get_login_cookie()
    if user_id is not None:
        user = db.User
        user.user_id = user_id
        return user.load()
    else:
        user = db.User.login(user_id, password)
        if user is None:
            return None
        set_login_cookie(user.user_id)
        return user






