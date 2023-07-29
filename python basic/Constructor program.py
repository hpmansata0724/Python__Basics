class employee:
    company = "google"

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("employee is created..!!")

    def getDetails(self):
        print("Name of employee is:", self.name)
        print("salary of employee is:", self.salary)
        print("subunit of employee is:", self.subunit)

    def getsalary(self, signature):
        print("salary of employee whose name is", self.name, "and workint in", self.company, "is", self.salary)
        print(signature)

    @staticmethod
    def greet():
        print("Good morning")
    @staticmethod
    def timeDisplay():
        import datetime
        print(datetime.datetime.now())


raj = employee("Raj", "20000", "Youtube")
raj.greet()  # employee.greet()
raj.getDetails()
raj.getsalary("Thanks...!!")  # employee.getsalary(raj)
raj.timeDisplay()
