from db.login import User

from collections import defaultdict

def line_chart_activity(user):
    activity_sum = defaultdict(int)
    metrics = user.get_all_metrics()
    activities_list = []
    for metric in metrics:
        print(metric.activity, metric.value, metric.metric_type, metric.timestamp) #reference
        activities_list.append({"name": metric.activity , "data": metric.value})
    for activity_dict in activities_list:
        activity_sum[activity_dict["name"]] += activity_dict["data"]#in minutes
    return activity_sum