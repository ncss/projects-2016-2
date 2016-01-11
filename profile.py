from db.login import User
import json, databasetocharts

class ProfileHandler:
    def __init__(self, user_id):
        self.user = User(user_id)
        self.user.load()
    
    def display_profile(self):
        aggregate_activity_data = databasetocharts.pie_chart_activity(self.user)
        real_chart_data = []
        for activity, sum in aggregate_activity_data.items():
            real_chart_data.append({
            "name": activity,
            "y": sum})            
        user_data = {
            "email": self.user.email,
            "full_name": (self.user.fname + ' ' + self.user.lname),
            "chart_data_json": json.dumps(real_chart_data)
        }
        return user_data