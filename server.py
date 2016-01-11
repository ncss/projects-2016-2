from tornado.ncss import Server, ncssbook_log
from activities import ActivityInputHandler
from engine.template import render
from profile import ProfileHandler
from db.login import User
import json
from login_backend import login, requires_login, logout, register, optional_login

@optional_login
def landing_handler(response, user_id):
    if user_id != None:
        response.redirect('/home/')
    else:
        vars = {'logged_in': user_id is not None,
                'html_class': 'landing'}
        response.write(render("landing.html", vars))

@requires_login
def home_handler(response, user_id):
    response.write(render("feed.html", {'logged_in': True}))

def register_handler(response):
    response.write(render("register.html", {'logged_in': False}))

@requires_login
def profile_handler(response, user_id, profile_number=None):
    display_profile = user_id
    if profile_number is not None:
        display_profile = profile_number
    poh = ProfileHandler(display_profile)
    vars = poh.display_profile()
    vars['logged_in'] = True
    response.write(render("profile.html", vars))

@requires_login
def input_handler_get(response, user_id):
    aih = ActivityInputHandler(user_id)
    vars = aih.get_template_data()
    vars['logged_in'] = True
    response.write(render("input_activity.html", vars))
    
@requires_login
def input_handler_post(response, user_id):
    aih = ActivityInputHandler(user_id)
    aih.load_activity_data(response)
    post = True
    vars = aih.get_template_data(post)
    vars['logged_in'] = True
    response.write(render("input_activity.html", vars))

@requires_login
def updateprofile_handler(response, user_id):
    response.write(render("update_profile.html", {'logged_in': True}))

@requires_login
def template_demo(response, user_id):
    response.write(render("test.html", {'a': 'B', 'user_id': user_id, 'hello': 'hello', 'logged_in': True}))

@optional_login
def search_handler(response, user_id):
    ary = User.find_user_by_fullname(response.get_field('query'))
    response.write(render("search_results.html", {'results': ary, 'logged_in': user_id is not None}))

@optional_login
def login_handler(response, user_id):
    response.write(render("login.html", {'logged_in': user_id is not None}))

@optional_login
def page404_handler(response, user_id):
    response.write(render("404.html", {'logged_in': user_id is not None}))

def auth_handler(response):
    email = response.get_field('email')
    password = response.get_field('password')
    result = login(response, email, password)
    print(result)
    if result is None:
        response.redirect('/?failure=1')
    else:
        response.redirect('/?success=1')

def logout_handler(response):
    logout(response)
    response.redirect('/')

def newuser_handler(response):
    email = response.get_field('email')
    password = response.get_field('password')
    name = response.get_field('name')
    tc = response.get_field('termsconditions')
    if tc != "accept":
        response.redirect('/register/?error=no_tc')
    return register(response, email, password, name)

def search_autocomplete_handler(response):
    ary = User.find_user_by_fullname(response.get_field('query'))
    res = []
    response.set_header("Content-Type", "application/json")
    for el in ary:
        res.append(el.fname + ' ' + el.lname)
    response.write(json.dumps(res))

server = Server()

server.register(r"/", landing_handler)
server.register(r"/home/", home_handler)
server.register(r"/register/", register_handler)
server.register(r"/profile/", profile_handler)
server.register(r"/profile/(\d+)/", profile_handler)
server.register(r"/input/", input_handler_get, post=input_handler_post)
server.register(r"/updateprofile/", updateprofile_handler)
server.register(r"/search/", search_handler)
server.register(r"/template/", template_demo)
server.register(r"/login/", login_handler)
server.register(r"/authenticate/", auth_handler)
server.register(r"/logout/", logout_handler)
server.register(r"/newuser/", newuser_handler)
server.register(r"/api/autocomplete", search_autocomplete_handler)
server.register(r"/.*", page404_handler)

server.run()
