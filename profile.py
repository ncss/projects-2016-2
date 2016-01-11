from db.login import User

class ProfileHandler:
    def __init__(self, user_id):
        self.user = User(user_id)
        self.user.load()
    
    def display_profile(self):
        user_data = {"email": self.user.email, "full_name": (self.user.fname + ' ' + self.user.lname)
        "total_km_run": (self.user.total_m_run/1000),
        "total_km_cycled": (self.user.total_m_cycled/1000),
        "total_km_swum": (self.user.total_m_swum/1000),
        "total_km_walked": (self.user.total_m_walked/1000),
        "total_pushups": (self.user.total_pushups),
        "total_situps": (self.user.total_situps),}
        }
        return user_data