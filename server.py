from tornado.ncss import Server, ncssbook_log

from engine.template import render

def index_handler(response):
  with open("templates/index.html") as file:
    response.write(file.read())

def home_handler(response):
  with open("templates/index.html") as file:
    response.write(file.read())

def profile_handler(response, user_id):
    with open("templates/profile.html") as file:
      response.write("Profile ID: " + user_id + file.read())

def template_demo(response):
    response.write(render("test.html", {}))

server = Server()
server.register(r"/", index_handler)
server.register(r"/profile/(\d+)/", profile_handler)
server.register(r"/template", template_demo)
server.run()
