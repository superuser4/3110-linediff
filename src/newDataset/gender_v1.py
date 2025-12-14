#get the gender of a person

class Person(object):
    def getGender(self):
        return "Unknown"

class Male(Person):
    def getGender(self):
        return "Male"

class Female(Person):
    def getGender(self):
        return "Female"

Rick = Male()
Mandy= Female()
print (Rick.getGender())
print (Mandy.getGender())