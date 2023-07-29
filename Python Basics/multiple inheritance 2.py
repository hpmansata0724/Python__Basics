#multilevel Inheritance
class person:
    country="India"
    def takebreath(self):
        print("I am breathing")
class employee(person):
    company="honda"
    salary=10000
    def getsalary(self):
        print("salary is ",self.salary)
    def takebreath(self):
        print("I am employee so I am luckily breathimg")
class programmer(employee):
    company="fiverr"
    def getsalary(self):
        print("No salary to programmer")
    def takebreath(self):
        print("I am programmer so i am breathing")
p=person()
p.takebreath()
e=employee()
e.takebreath()
print(e.company)
pr=programmer()
pr.takebreath()
print(pr.company)
print(pr.country)
pr.getsalary()

