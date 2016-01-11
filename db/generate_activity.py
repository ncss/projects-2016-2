import random
from db.login import User
from db.metric import Metric

tim = User(username = "tim", password = "abc123", fname = "Tim", lname = "Dawborn", email = "tim@ncss.edu.au", dob = "2016-01-10", postcode = "1234", country_code = "555", image = "")
james = User(username = "james", password = "123abc", fname = "James", lname = "Curran", email = "jdog@ncss.edu.au", dob = "2016-01-09", postcode = "1000", country_code = "522", image = "")
nicky = User(username = "nicky", password = "nickydabest", fname = "Nicky", lname = "Ringland", email = "nicky@ncss.edu.au", dob = "2016-01-08", postcode = "1337", country_code = "54", image = "")
simon = User(username = "simon", password = "hihihihi", fname = "Simon", lname = "Shields", email = "simon@ncss.edu.au", dob = "2016-01-04", postcode = "999", country_code = "2", image = "")
will = User(username = "will", password = "password123", fname = "Will", lname = "Cannings", email = "will@ncss.edu.au", dob = "2015-12-25", postcode = "000", country_code = "752", image = "")
lochie = User(username = "chokstar", password = "ch0kstar", fname = "Lochie", lname = "Chok", email = "chokstar@chokstarproductions.com", dob = "1999-02-24", postcode = "2153", country_code = "2", image = "")
belle = User(username = "belle", password = "password", fname = "Belle", lname = "Spizick", email = "belle@ncss.edu.au", dob = "1999-12-01", postcode = "7004", country_code = "2", image = "")

tim.save()
james.save()
nicky.save()
simon.save()
will.save()
lochie.save()
belle.save()

currenttimestamp = 1452473361
for i in range(1000):
    currenttimestamp += 86100
    minutes = random.randint(4, 90)
    checker = random.randint(0, 8)
    if checker == 0:
        activity1 = "running"
    elif checker == 1:
        activity1 = "walking"
    elif checker == 2:
        activity1 = "cycling"
    elif checker == 3:
        activity1 = "swimming"
    elif checker == 4:
        activity1 = "soccer"
    elif checker == 5:
        activity1 = "push_ups"
    elif checker == 6:
        activity1 = "sit_us"
    elif checker == 7:
        activity1 = "other"
    m = Metric(user = 0, activity = activity1, timestamp = currenttimestamp, metric_type = "minutes", value = minutes)
    m.save()
