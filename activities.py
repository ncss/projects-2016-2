import tornado.ncss as tornado
from engine.template import render

class Activity:
    title = None
    description = None
    icon = None
    metric_list = None
    
    def __init__(self, title="", description="", icon="", metric_list=[]):
        self.title = title
        self.description = description
        self.icon = icon    
        self.metric_list = metric_list


    
class ActivityInputHandler:
    activities = {
        "running": Activity("Running","Walking quickly","child", [
            {"title": "Duration", "units": "minutes"},
            {"title": "Distance", "units": "metres"},
        ]),
        "walking": Activity("Walking","Running slowly","male", [
            {"title": "Duration", "units": "minutes"},
            {"title": "Distance", "units": "metres"},
        ]),
        "cycling": Activity("Cycling","Using a bicycle","bicycle",[
            {"title": "Duration", "units": "minutes"},
            {"title": "Distance", "units": "metres"},
        ]),
        "swimming": Activity("Swimming","Running in water","tint",[
            {"title": "Duration", "units": "minutes"},
            {"title": "Distance", "units": "metres"},
        ]),
        "soccer": Activity("Soccer","Kicking a ball","futbol-o",[
            {"title": "Duration", "units": "minutes"},
        ]),
        "push_ups": Activity("Push ups","Pushing up","arrows-v",[
            {"title": "Count", "units": "amount"},
        ]),
        "sit_ups": Activity("Sit ups","Sitting up","arrow-h",[
            {"title": "Count", "units": "amount"},
        ]),
        "other": Activity("Other","Enter own one","question",[
            {"title": "Duration", "units": "minutes"}
        ]),
        }
    
    def get_template_data(self):
        return {"activities": self.activities}
        
    def load_activity_data(self, request):
        print(request.get_field("swimming_Duration"))
        for activity_name, activity in self.activities.items():
            for metric in activity.metric_list:
                field_name = activity_name + "_" + metric["title"]
                print(field_name)
                print(request.get_field(field_name))
            
            
            
            
            
            
            
            
            
            
            
    
    
    
    
