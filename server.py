from tornado.ncss import Server, ncssbook_log
from activities import ActivityInputHandler, activity_dict
from engine.template import render
from profile import ProfileHandler
from login_backend import login


def landing_handler(response):
    response.write(render("landing.html", {'a': 'B'}))

def home_handler(response):
    response.write(render("feed.html", {'a': 'B'}))

def register_handler(response):
    response.write(render("register.html", {'a': 'B'}))

def profile_handler(response, user_id):
    poh = ProfileHandler(user_id)
    response.write(render("profile.html", poh.display_profile()))

def input_handler(response):
    aih = ActivityInputHandler(activity_dict)
    response.write(render("input_activity.html", aih.get_template_data()))

def updateprofile_handler(response):
    response.write(render("update_profile.html", {'a': 'B'}))

def template_demo(response):
    response.write(render("test.html", {'a': 'B'}))

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
server.register(r"/.*", page404_handler)

server.run()
