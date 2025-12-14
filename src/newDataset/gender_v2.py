#get the gender of a person

class Person(object):
    def __init__(self):
        self.gender = "Unknown"

    def getGender(self):
	    print(self.gender)

class Male(Person):
    def __init__(self):
	    self.gender = "Male"

class Female(Person):
    def __init__(self):
	    self.gender = "Female"

Rick = Male()
Mandy = Female()
Rick.getGender()
Mandy.getGender()
