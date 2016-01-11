import db.login as db
from urllib.parse import urlencode
import functools
import time

def set_login_cookie(response, user_id):
    response.set_secure_cookie("user_id", str(user_id), expires=time.time() + 24 * 3600) 

def get_login_cookie(response):
    user_id = response.get_secure_cookie("user_id")
    if user_id is not None:
        return int(user_id)
    return None

def requires_login(fn):
    @functools.wraps(fn)
    def wrapper(response, *args, **kwargs):
        if get_login_cookie(response) is not None:
            return fn(response, get_login_cookie(response), *args, **kwargs)
        else:
            print(response.request.uri)
            response.redirect('/login/')
    return wrapper

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

def register(response, email, password, name):
    """
    1. register
    2. register
    3. say yay
    """
    if not db.User.check_email_free(email):
        response.redirect('/register/?error=email')
    else:
        name += ' '
        user = db.User(email=email, fname=name.split()[0], lname=' '.join(name.split()[1:]), password=password)
        user.save()
        login(response, email, password)
        response.redirect('/')
        


def logout(response):
    response.clear_cookie("user_id")
