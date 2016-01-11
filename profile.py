from db.login import User

class ProfileHandler:
    def __init__(self, user_id):
        self.user = User(user_id)
        self.user.load()
    
    def display_profile(self):
        user_data = {"email": self.user.email, "full_name": (self.user.fname + ' ' + self.user.lname)
        
        }
        return user_data