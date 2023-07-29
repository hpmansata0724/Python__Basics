class employee:
    company="Google"
    def getsalary(self,signature):
        print("Salary of Employee whose name is",self.name,"and working in",self.company,"is",self.company,"is",self.salary)
        print(signature)
    @staticmethod
    def greet():
        print("GM.....Sir")
    @staticmethod
    def timeDisplay():
        import datetime
        print(datetime.datetime.now())

    raj =employee()
    raj.name = "Raj"
    raj.salary = 10000
    raj.great()  # Employee.great()
    raj.getsalary("Thanks...!")  # Employee.getsalary(raj)
    raj.timeDisplay()

