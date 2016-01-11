from tornado.ncss import Server, ncssbook_log
from activities import ActivityInputHandler, activity_dict
from engine.template import render
from profile import ProfileHandler
from login_backend import login, requires_login, logout


def landing_handler(response):
    response.write(render("landing.html", {'a': 'B'}))

@requires_login
def home_handler(response, user_id):
    response.write(render("feed.html", {'a': 'B'}))

def register_handler(response):
    response.write(render("register.html", {'a': 'B'}))

@requires_login
def profile_handler(response, user_id):
    poh = ProfileHandler(user_id)
    response.write(render("profile.html", poh.display_profile()))

@requires_login
def input_handler(response, user_id):
    aih = ActivityInputHandler(activity_dict)
    response.write(render("input_activity.html", aih.get_template_data()))

@requires_login
def updateprofile_handler(response):
    response.write(render("update_profile.html", {'a': 'B'}))

def template_demo(response):
    response.write(render("test.html", {'a': 'B'}))

def search_handler(response):
    response.write(render("search_results.html", {'a': 'B'}))

def login_handler(response):
    response.write(render("login.html", {'a': 'B'}))

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

server = Server()

server.register(r"/", landing_handler)
server.register(r"/home/", home_handler)
server.register(r"/register/", register_handler)
server.register(r"/profile/(\d+)/", profile_handler)
server.register(r"/input/", input_handler)
server.register(r"/updateprofile/", updateprofile_handler)
server.register(r"/search/", search_handler)
server.register(r"/template/", template_demo)
server.register(r"/login/", login_handler)
server.register(r"/authenticate/", auth_handler)
server.register(r"/logout/", logout_handler)

server.run()
