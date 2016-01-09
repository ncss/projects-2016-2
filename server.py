from tornado.ncss import Server, ncssbook_log

def index_handler(response):
  with open("indextest.html") as file:
    response.write(file.read())

def profile_handler(response, user_id):
    with open("indextest.html") as file:
      response.write("Profile ID: " + user_id + file.read())

server = Server()
server.register(r"/", index_handler)
server.register(r"/profile/(\d+)/", profile_handler)
server.run()
