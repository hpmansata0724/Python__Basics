class person():
    company="India"
    def __init__(self):
        print("Initializing person")
    def takebreath(self):
        print("I am breathing")
class employee(person):
    company="honda"
    salary=10000
    def __init__(self):
        super().takebreath()
        print("I am an empoyee so I am Breathing")
class programmer(employee):
    company="fiverr"
    def __init__(self):
        super.__init__()
        print("Initializing programmer")
    def getsalary(self):
        print("No salary to programmer")
    def takebreath(self):
        super().takebreath()
        print("I am an employee so I am luckily breathing")
class programmer(employee):
    company="fiverr"
    def __init__(self):
        super().__init__()
        print("Initializing programmer")
    def getsalary(self):
        print("No salary to programmer")
    def takebreath(self):
        super().takebreath()
        print("I am programmer so I am breathing")
p=person()
p.takebreath()
e=employee()
e
