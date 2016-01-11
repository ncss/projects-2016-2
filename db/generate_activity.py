import random
from db.login import User
from db.metric import Metric

tim = User(username = "GeorgeF", password = "a", fname = "George", lname = "Forman", email = "a", dob = "2016-01-10", postcode = "1234", country_code = "555", image = "")
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
elizabeth = User(username = "liz", password ="yay", fname = "Elizabeth", lname = "C", email = "elizabeth@ncss.edu.au", dob = "1999-12-01", postcode = "7004", country_code = "2", image = "")
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

for user_number in range(0, 23):
    currenttimestamp = 1452473361
    for i in range(20):
        currenttimestamp += 86100
        minutes = random.randint(4, 90)
        checker = random.randint(0, 8)
        distance = random.randint(100, 4754)
        if checker == 0:
            activity1 = "running"
            metric1 = "minutes"
            metric2 = "distance"
        elif checker == 1:
            activity1 = "walking"
            metric1 = "minutes"
            metric2 = "distance"
        elif checker == 2:
            activity1 = "cycling"
            metric1 = "minutes"
            metric2 = "distance"
        elif checker == 3:
            activity1 = "swimming"
            metric1 = "minutes"
            metric2 = "distance"
        elif checker == 4:
            activity1 = "soccer"
            metric1 = "minutes"
        elif checker == 5:
            activity1 = "push_ups"
            metric1 = "count"
        elif checker == 6:
            activity1 = "sit_up"
            metric1 = "count"
        elif checker == 7:
            activity1 = "other"
        if checker > 3:
            m = Metric(user = user_number, activity = activity1, timestamp = currenttimestamp, metric_type = metric1, value = minutes)
            m.save()
        else:
            m = Metric(user = user_number, activity = activity1, timestamp = currenttimestamp, metric_type = metric1, value = minutes)
            x = Metric(user = user_number, activity = activity1, timestamp = currenttimestamp, metric_type = metric2, value = distance)
            m.save()
            x.save()
