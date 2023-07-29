class employess:
    company="Google"
    salary=100
    age=23
e1=employess()
e2=employess()
e1.salary=300
e2.salary=400
print(e1.company)
print(e2.company)
employess.company="Youtube"
print("Company of employee 1:",e1.company)
print("Company of employee 2:",e2.company)
print("Salary of employee 1:",e1.salary)
print("Salary of employee 2:",e2.salary)
e1.age=45
print("Age of employee 1:",e1.age)
print("Age of employee 2:",e2.age)