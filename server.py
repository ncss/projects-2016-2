from tornado.ncss import Server, ncssbook_log

from engine.template import render


def landing_handler(response):
  response.write(render("landing.html", {'a': 'B'}))

def home_handler(response):
    response.write(render("feed.html", {'a': 'B'}))
	
def register_handler(response):
  response.write(render("register.html", {'a': 'B'}))

def profile_handler(response, user_id):
    response.write(render("profile.html", {'user_id': 51}))
      
def input_handler(response):
  response.write(render("input.html", {'a': 'B'}))
	
def updateprofile_handler(response):
  response.write(render("update_profile.html", {'a': 'B'}))

def template_demo(response):
    response.write(render("test.html", {'a': 'B'}))

def search_handler(response):
  response.write(render("search.html", {'a': 'B'}))
	
server = Server()
server.register(r"/", landing_handler)
server.register(r"/home/", home_handler)
server.register(r"/register/", register_handler)
server.register(r"/profile/(\d+)/", profile_handler)
server.register(r"/input/", input_handler)
server.register(r"/updateprofile/", updateprofile_handler)
server.register(r"/search/", search_handler)
server.register(r"/template/", template_demo)

server.run()
