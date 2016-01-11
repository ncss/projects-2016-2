from tornado.ncss import Server, ncssbook_log
from activities import ActivityInputHandler
from engine.template import render
from profile import ProfileHandler
from login_backend import login, requires_login, logout, register


def landing_handler(response):
    response.write(render("landing.html", {'a': 'B'}))

@requires_login
def home_handler(response, user_id):
    response.write(render("feed.html", {'a': 'B'}))

def register_handler(response):
    response.write(render("register.html", {'a': 'B'}))

@requires_login
def profile_handler(response, user_id, profile_number=None):
    display_profile = user_id
    if profile_number is not None:
        display_profile = profile_number
    poh = ProfileHandler(display_profile)
    response.write(render("profile.html", poh.display_profile()))

@requires_login
def input_handler_get(response, user_id):
    aih = ActivityInputHandler()
    response.write(render("input_activity.html", aih.get_template_data()))
    
@requires_login
def input_handler_post(response, user_id):
    aih = ActivityInputHandler()
    aih.load_activity_data(response)

@requires_login
def updateprofile_handler(response, user_id):
    response.write(render("update_profile.html", {'a': 'B'}))

@requires_login
def template_demo(response, user_id):
    response.write(render("test.html", {'a': 'B', 'user_id': user_id, 'hello': 'hello'}))

def search_handler(response):
    response.write(render("search_results.html", {'a': 'B'}))

def login_handler(response):
    response.write(render("login.html", {'a': 'B'}))

def page404_handler(response):
  response.write(render("404.html", {}))

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
server.register(r"/.*", page404_handler)

server.run()
