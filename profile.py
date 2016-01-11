from db.login import User
import json, databasetocharts
from collections import defaultdict
import time
import datetime
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

        metrics = self.user.get_all_metrics()
            
        activity_dict = defaultdict(list)
        activity_list = []
        metrics_list = []
        for metric in metrics:
            metric_list = []
            metric_list.append(metric.activity)
            metric_list.append(metric.timestamp)
            metric_list.append(str(metric.value)+ " " + str(metric.metric_type))
            activity_dict[metric.activity].append(metric_list)
        print(activity_dict)
                
        activities_list = []
        for activity_list in activity_dict:
            activities_list.append(sorted(activity_dict[activity_list], key=lambda x:x[1]))
            for item in activities_list[-1]:
                item[1] = datetime.datetime.fromtimestamp(item[1]).strftime("%H:%M %p - %d/%m/%Y")
        print(activities_list)    
        print()
        activities_list.sort(key=lambda x:x[0][0].casefold())
                
        user_data = {
            "email": self.user.email,
            "full_name": (self.user.fname + ' ' + self.user.lname),
            "chart_data_json": json.dumps(real_chart_data),
            "activities":activities_list,
            "pic_url": self.user.pic
        }
        return user_data