class employee:
    company="google"
    salary=10000
    location="pune"
    @classmethod
    def changesalary(cls,sal):
        cls.salary=sal
e=employee()
print(e.salary)
e.changesalary(15000)
print(e.salary)
print(employee.salary)