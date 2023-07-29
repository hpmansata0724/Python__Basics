class employee:
    company="google"
    salary=10000
    bonus=1000
    @property
    def totalsalary(self):
        return self.salary+self.bonus
    @totalsalary.setter
    def totalsalary(self,val):
        self.bonus=val-self.salary

e=employee()
print("salary:",e.salary)
print("bonus",e.bonus)
print("total salary",e.totalsalary)
e.totalsalary=15000
print("after change in total salary")
print("salary",e.salary)
print("bonus",e.bonus)
print("total salary:",e.totalsalary)
