from db.login import User
import json, databasetocharts

class ProfileHandler:
    def __init__(self, user_id):
        self.user = User(user_id)
        self.user.load()
    
    def display_profile(self):
<<<<<<< HEAD
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
=======
        chart_data = [{
               "name": 'Sleeping',
               "y": 30
            }, {
               "name": 'Resting',
               "y": 20,
               "sliced": True,
               "selected": True
            }, {
               "name": 'Relaxing',
               "y": 20
            }, {
               "name": 'Snoozing',
               "y": 5
            }, {
               "name": 'Lolling',
               "y": 5
            }]
    
        activities_list = [
                        ["Swimming", "10pm", "5km"],
                        ["Hiking", "3pm", "16km"] ]
    
        user_data = {
            "email": self.user.email,
            "full_name": (self.user.fname + ' ' + self.user.lname),
            "chart_data_json": json.dumps(chart_data),
            "activities": activities_list
>>>>>>> 2626d30c4daffed77e31f819b4784b1a58579e86
        }
        return user_data