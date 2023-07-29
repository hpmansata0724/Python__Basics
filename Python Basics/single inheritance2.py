class employee:
    company="google"
    def showdetails(self):
        print("This is an employee class")
class programmer(employee):
    language="python"
    company="youtube"
    def getlanguage(self):
        print("This is",self.language)

    def showdetails(self):
        print("This is an programmer class")

e=employee()
e.showdetails()
print("This is in",e.company,"company")
p=programmer()
p.getlanguage()
p.showdetails()
print("This is in",p.company,"company")
