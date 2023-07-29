class employee:
    company="google"
    def showdetails(self):
        print("This is an employee")
class programmer(employee):
    language="python"
    def getlanguage(self):
        print("This is",self.language,"programmer")
e=employee()
e.showdetails()
p=programmer()
p.getlanguage()
p.showdetails()
print("This is in",p.company,"Company")

