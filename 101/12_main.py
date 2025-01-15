
class Person:

    def __init__(self, name, surname, birthYear):
        self.name = name
        self.surname = surname
        self.birthYear = birthYear

    def getPersonlInfo(self):
        return self.name + " " + self.surname + " " + str(self.birthYear)

    def getNames(self):
        return self.name + " " + self.surname

    def getSurname(self):
        return self.surname

    def getBirthYear(self):
        return self.birthYear


person = Person("John", "Doe", 1990)

print(person.getPersonlInfo())
