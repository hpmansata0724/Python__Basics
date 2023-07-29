class employee:
    company="CDAC computer education"
    def setdetails(self):
        set.name=input()
        set.salary=int(input())

    def getdetails(self):
        print("\nName.",self.name,"\t","salary.",self.salary)
list1=[]
for i in range(0,3):
    list1.append(employee())
print("Welcome in ",employee.company)
for i,obj in enumerate(list1):
    print("Enter name and salary of employee:",i+1,":")
    obj.setdetails()
for i,obj in enumerate(list1):
    print("Details of employee",i+1,":")
    obj.getdetails()

for i,obj in enumerate(list1):
    print("Details of employee",i+1,":")
    obj.getdetails()

