from tornado.ncss import Server, ncssbook_log

def landing_handler(response):
  with open("templates/landing.html") as file:
    response.write(file.read())

def home_handler(response):
  with open("templates/home.html") as file:
    response.write(file.read())
	
def register_handler(response):
  with open("templates/register.html") as file:
    response.write(file.read())

def profile_handler(response, user_id):
    with open("templates/profile.html") as file:
      response.write("Profile ID: " + user_id + file.read())
	  
def input_handler(response):
  with open("templates/input.html") as file:
    response.write(file.read())
	
def updateprofile_handler(response):
  with open("templates/updateprofile.html") as file:
    response.write(file.read())

def template_demo(response):
    response.write(render("test.html", {'a': 'B'}))

def search_handler(response):
  with open("templates/search.html") as file:
    response.write(file.read())
	
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
