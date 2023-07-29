class employee:
    company="google"
    salary=10000
    salarybonus=2000
    @property
    def totalsalary(self):
        return self.salary+self.salarybonus
    @totalsalary.setter
    def totalsalary(self,val):
        self.salarybonus=val-self.salary
e=employee()
print(e.totalsalary)
e.totalsalary=15000
print(e.salary)
print(e.salarybonus)
print(e.totalsalary)
