from login import User

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
