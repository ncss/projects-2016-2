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
	
activities = {
    "running": Activity("Running","Walking quickly","child", [
		{"title": "Duration", "units": "minutes"},
		{"title": "Distance", "units": "metres"},
	]),
	"walking": Activity("Walking","Running slowly","male"), [
		{"title": "Duration", "units": "minutes"},
		{"title": "Distance", "units": "metres"},
	]),
	"cycling": Activity("Cycling","Using a bicycle","bicycle"),[
		{"title": "Duration", "units": "minutes"},
		{"title": "Distance", "units": "metres"},
	]),
	"swimming": Activity("Swimming","Running in water","tint"),[
		{"title": "Duration", "units": "minutes"},
		{"title": "Distance", "units": "metres"},
	]),
	"soccer": Activity("Soccer","Kicking a ball","futbol-o"),[
		{"title": "Duration", "units": "minutes"},
		{"title": "Distance", "units": "metres"},
	]),
	"push ups": Activity("Push ups","Pushing up","arrows-v"),[
		{"title": "Duration", "units": "minutes"},
		{"title": "Distance", "units": "metres"},
	]),
	"sit ups": Activity("Sit ups","Sitting up","arrow-h"),[
		{"title": "Duration", "units": "minutes"},
		{"title": "Distance", "units": "metres"},
	]),
	"other": Activity("Other","Enter own one","question")[
		{"title": "Duration", "units": "minutes"},
		{"title": "Distance", "units": "metres"},
	]),
	}