class employee:
    'common base class for employee'
    empcount=0
    company="google"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def getdetails(self):
        print("employee",self.name,"has Rs",self.salary,"salary")
        employee.empcount+=1

    @staticmethod
    def gettotalemployee():
        print("Total employee in",employee.company,"are",employee.empcount)
emp1=employee("Mahesh",10000)
emp2=employee("Rajesh",20000)
emp3=employee("paresh",30000)
employee.gettotalemployee()
#Built in class employee
print(employee.__doc__)
print(employee.__name__)
print(employee.__module__)
print(employee.__bases__)
print(employee.__dict__)