# Class is a blueprint of an object
# An object is instance of a class
class Person:
    # Properties/Attributes/Characteristics
    age = 23
    name = "Bill"
    # Method/Function/Behaviour
    def talk(self):
        print("Person is talking")

teacher = Person()
print(teacher.name)
print(teacher.age)

teacher.talk()