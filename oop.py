class Person:
    def __init__(self,firstname,age,gender):
        self.firstname=firstname
        self.age = age
        self.gender=gender
    def details(self):
        print(self.firstname,"is studying")

teacher = Person("Joe",34,"male")
accountant = Person("Mary",34,"female")
director = Person("John",23,"male")

print(teacher.firstname,teacher.age,teacher.gender)
print(director.firstname,director.age,director.gender)
print(accountant.firstname,accountant.age,accountant.gender)