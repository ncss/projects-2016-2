from db.login import User
from db.metric import Metric

tim = User(username = "tim", password = "abc123", fname = "Tim", lname = "Dawborn", email = "tim@ncss.edu.au", dob = "2016-01-10", postcode = "1234", country_code = "555", image = "")
james = User(username = "james", password = "123abc", fname = "James", lname = "Curran", email = "jdog@ncss.edu.au", dob = "2016-01-09", postcode = "1000", country_code = "522", image = "")
nicky = User(username = "nicky", password = "nickydabest", fname = "Nicky", lname = "Ringland", email = "nicky@ncss.edu.au", dob = "2016-01-08", postcode = "1337", country_code = "54", image = "")
simon = User(username = "simon", password = "hihihihi", fname = "Simon", lname = "Shields", email = "simon@ncss.edu.au", dob = "2016-01-04", postcode = "999", country_code = "2", image = "")
will = User(username = "will", password = "password123", fname = "Will", lname = "Cannings", email = "will@ncss.edu.au", dob = "2015-12-25", postcode = "000", country_code = "752", image = "")

tim.save()
james.save()
nicky.save()
simon.save()
will.save()

run_minutes = Metric(user = 0, activity = "Running", timestamp = 1452473361, metric_type = "minutes", value = 10)
run_metres = Metric(user = 0, activity = "Running", timestamp = 1452473361, metric_type = "metres", value = 1200)
walk_minutes = Metric(user = 1, activity = "Walking", timestamp = 1452474361, metric_type = "minutes", value = 39)
walk_metres = Metric(user = 1, activity = "Walking", timestamp = 1452474361, metric_type = "metres", value = 1640)
cycling_minutes = Metric(user = 1, activity = "Cycling", timestamp = 1452475652, metric_type = "minutes", value = 40)
cycling_metres = Metric(user = 1, activity = "Cycling", timestamp = 1452475652, metric_type = "metres", value = 40)
swimming_minutes = Metric(user = 2, activity = "Swimming", timestamp = 1452575652, metric_type = "minutes", value = 20)
swimming_metres = Metric(user = 2, activity = "Swimming", timestamp = 1452575652, metric_type = "metres", value = 200)

run_minutes.save()
run_metres.save()
walk_minutes.save()
walk_metres.save()
cycling_minutes.save()
cycling_metres.save()
swimming_minutes.save()
swimming_metres.save()