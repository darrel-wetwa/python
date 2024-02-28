class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def salary(self):
        print(self.name,"is being paid",self.salary)

x = Employee("John",34000)
y = Employee("Indiana",45000)
z = Employee("Marcus",67000)