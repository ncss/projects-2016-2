import random
from db.login import User
from db.metric import Metric

tim = User(username = "tim", password = "abc123", fname = "Tim", lname = "Dawborn", email = "tim@ncss.edu.au", dob = "2016-01-10", postcode = "1234", country_code = "555", image = "")
james = User(username = "james", password = "123abc", fname = "James", lname = "Curran", email = "jdog@ncss.edu.au", dob = "2016-01-09", postcode = "1000", country_code = "522", image = "")
nicky = User(username = "nicky", password = "nickykneecapper", fname = "Nicky", lname = "Ringland", email = "nicky@ncss.edu.au", dob = "2016-01-08", postcode = "1337", country_code = "54", image = "")
simon = User(username = "simon", password = "yay", fname = "Simon", lname = "Shields", email = "simon@ncss.edu.au", dob = "2016-01-04", postcode = "999", country_code = "2", image = "")
will = User(username = "will", password = "password123", fname = "Will", lname = "Cannings", email = "will@ncss.edu.au", dob = "2015-12-25", postcode = "000", country_code = "752", image = "")
lochie = User(username = "chokstar", password = "yay", fname = "Lochie", lname = "Chok", email = "chokstar@chokstarproductions.com", dob = "1999-02-24", postcode = "2153", country_code = "2", image = "")
belle = User(username = "belle", password = "yay", fname = "Belle", lname = "Spizick", email = "belle@ncss.edu.au", dob = "1999-12-01", postcode = "7004", country_code = "2", image = "")
jessica = User(username = "jessica", password ="yay", fname = "Jessica", lname = "D'Ali", email = "jess@ncss.edu.au", dob = "1999-12-01", postcode = "7004", country_code = "2", image = "")
renee = User(username = "renee", password ="yay", fname = "Renee", lname = "Noble", email = "renee@ncss.edu.au", dob = "1999-12-01", postcode = "7004", country_code = "2", image = "")
luke = User(username = "luke", password ="yay", fname = "Luke", lname = "Anderson", email = "luke@ncss.edu.au", dob = "1999-12-01", postcode = "7004", country_code = "2", image = "")
callan = User(username = "callan", password ="yay", fname = "Callan", lname = "McNamara", email = "callan@ncss.edu.au", dob = "1999-12-01", postcode = "7004", country_code = "2", image = "")
nick = User(username = "nick", password ="yay", fname = "Nick", lname = "Armstrong", email = "nick@ncss.edu.au", dob = "1999-12-01", postcode = "7004", country_code = "2", image = "")
elizabeth = User(usernamen = "liz", password ="yay", fname = "Elizabeth", lname = "C", email = "elizabeth@ncss.edu.au", dob = "1999-12-01", postcode = "7004", country_code = "2", image = "")
sandra = User(username = "sadra", password ="yay", fname = "Sanda", lname = "Brand", email = "sandra@ncss.edu.au", dob = "1999-12-01", postcode = "7004", country_code = "2", image = "")
sid = User(username = "sid", password ="yay", fname = "Sid", lname = "Pham", email = "sid@ncss.edu.au", dob = "1999-12-01", postcode = "7004", country_code = "2", image = "")
tom = User(username = "tom", password ="yay", fname = "Tom", lname = "Unknown", email = "tom@ncss.edu.au", dob = "1999-12-01", postcode = "7004", country_code = "2", image = "")
kass = User(username = "kass", password ="yay", fname = "Kass", lname = "di Bona", email = "kass@ncss.edu.au", dob = "1999-12-01", postcode = "7004", country_code = "2", image = "")
connie = User(username = "connie", password ="yay", fname = "Connie", lname = "Zhang", email = "connie@ncss.edu.au", dob = "1999-12-01", postcode = "7004", country_code = "2", image = "")
lindsey = User(username = "lindsey", password ="yay", fname = "Lindsey", lname = "Dale", email = "lindsey@ncss.edu.au", dob = "1999-12-01", postcode = "7004", country_code = "2", image = "")
boran = User(username = "boran", password ="yay", fname = "Boran", lname = "Wang", email = "boran@ncss.edu.au", dob = "1999-12-01", postcode = "7004", country_code = "2", image = "")
sarah = User(username = "sarah", password ="yay", fname = "Sarah", lname = "Hercock", email = "sarah@ncss.edu.au", dob = "1999-12-01", postcode = "7004", country_code = "2", image = "")
alex = User(username = "alex", password ="yay", fname = "Alex", lname = "McCLung", email = "alex@ncss.edu.au", dob = "1999-12-01", postcode = "7004", country_code = "2", image = "")
ben = User(username = "ben", password ="yay", fname = "Ben", lname = "Coates", email = "ben@ncss.edu.au", dob = "1999-12-01", postcode = "7004", country_code = "2", image = "")
ryan = User(username = "ryan", password ="yay", fname = "Ryan", lname = "Smith", email = "callan@ncss.edu.au", dob = "1999-12-01", postcode = "7004", country_code = "2", image = "")

tim.save()
james.save()
nicky.save()
simon.save()
will.save()
lochie.save()
belle.save()
jessica.save()
renee.save()
luke.save()
callan.save()
nick.save()
elizabeth.save()
sandra.save()
sid.save()
tom.save()
kass.save()
connie.save()
lindsey.save()
boran.save()
sarah.save()
alex.save()
ben.save()
ryan.save()

run_minutes = Metric(user = 0, activity = "Running", timestamp = 1452473361, metric_type = "minutes", value = 10)
run_minutes2 = Metric(user = 1, activity = "Running", timestamp = 1452473361, metric_type = "minutes", value = 20)
run_minutes3 = Metric(user = 2, activity = "Running", timestamp = 1452473361, metric_type = "minutes", value = 30)
run_minutes4 = Metric(user = 3, activity = "Running", timestamp = 1452473361, metric_type = "minutes", value = 40)
run_minutes5 = Metric(user = 4, activity = "Running", timestamp = 1452473361, metric_type = "minutes", value = 10)
run_minutes6 = Metric(user = 5, activity = "Running", timestamp = 1452473361, metric_type = "minutes", value = 20)
run_minutes7 = Metric(user = 6, activity = "Running", timestamp = 1452473361, metric_type = "minutes", value = 30)
run_minutes8 = Metric(user = 7, activity = "Running", timestamp = 1452473361, metric_type = "minutes", value = 40)
run_metres = Metric(user = 0, activity = "Running", timestamp = 1452473361, metric_type = "metres", value = 1200)
walk_minutes = Metric(user = 1, activity = "Walking", timestamp = 1452474361, metric_type = "minutes", value = 39)
walk_minutes2 = Metric(user = 1, activity = "Walking", timestamp = 1452474461, metric_type = "minutes", value = 39)
walk_minutes3 = Metric(user = 2, activity = "Walking", timestamp = 1452474561, metric_type = "minutes", value = 39)
walk_minutes4 = Metric(user = 4, activity = "Walking", timestamp = 1452474761, metric_type = "minutes", value = 39)
walk_minutes5 = Metric(user = 9, activity = "Walking", timestamp = 1452474361, metric_type = "minutes", value = 39)
walk_minutes6 = Metric(user = 10, activity = "Walking", timestamp = 1452474461, metric_type = "minutes", value = 39)
walk_minutes7 = Metric(user = 15, activity = "Walking", timestamp = 1452474561, metric_type = "minutes", value = 39)
walk_minutes8 = Metric(user = 16 activity = "Walking", timestamp = 1452474761, metric_type = "minutes", value = 39)
walk_metres = Metric(user = 1, activity = "Walking", timestamp = 1452474361, metric_type = "metres", value = 1640)
cycling_minutes = Metric(user = 1, activity = "Cycling", timestamp = 1452475652, metric_type = "minutes", value = 40)
cycling_metres = Metric(user = 1, activity = "Cycling", timestamp = 1452475652, metric_type = "metres", value = 40)
cycling_metres2 = Metric(user = 2, activity = "Cycling", timestamp = 1452475652, metric_type = "metres", value = 500)
cycling_metres3 = Metric(user = 3, activity = "Cycling", timestamp = 1452475652, metric_type = "metres", value = 46)
cycling_minutes = Metric(user = 5, activity = "Cycling", timestamp = 1452475652, metric_type = "minutes", value = 40)
cycling_metres4 = Metric(user = 11, activity = "Cycling", timestamp = 1452475652, metric_type = "metres", value = 40)
cycling_metres5 = Metric(user = 12, activity = "Cycling", timestamp = 1452475652, metric_type = "metres", value = 500)
cycling_metres6 = Metric(user = 13, activity = "Cycling", timestamp = 1452475652, metric_type = "metres", value = 46)
cycling_metres7 = Metric(user = 14, activity = "Cycling", timestamp = 1452475652, metric_type = "metres", value = 40)
cycling_metres8 = Metric(user = 15, activity = "Cycling", timestamp = 1452475652, metric_type = "metres", value = 500)
cycling_metres9 = Metric(user = 16, activity = "Cycling", timestamp = 1452475652, metric_type = "metres", value = 46)
swimming_minutes = Metric(user = 2, activity = "Swimming", timestamp = 1452575652, metric_type = "minutes", value = 20)
swimming_metres = Metric(user = 2, activity = "Swimming", timestamp = 1452575652, metric_type = "metres", value = 200)

run_minutes.save()
run_minutes2.save()
run_minutes3.save()
run_minutes4.save()
run_minutes5.save()
run_minutes6.save()
run_minutes7.save()
run_minutes8.save()
run_metres.save()
walk_minutes.save()
walk_minutes2.save()
walk_minutes3.save()
walk_minutes4.save()
walk_minutes5.save()
walk_minutes6.save()
walk_minutes7.save()
walk_minutes8.save()
walk_metres.save()
cycling_minutes.save()
cycling_metres.save()
cycling_metres2.save()
cycling_metres3.save()
cycling_metres4.save()
cycling_metres5.save()
cycling_metres6.save()
cycling_metres7.save()
cycling_metres8.save()
cycling_metres9.save()
swimming_metres.save()