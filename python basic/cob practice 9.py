class time:
    def __init__(self, hours=0, minutes=0):
        self.hours = hours
        self.minutes = minutes

    def displaydata(self):
        print(self.hours, "-Hours", self.minutes, "-minutes")

    def addtimes(self, t1, t2):
        self.minutes = t1.minutes + t2.minutes
        self.hours = int(self.minutes / 60)
        self.minutes = self.minutes % 60
        self.hours = self.hours + t1.hours + t2.hours


t1 = time(2, 45)
t2 = time(3, 35)
t3 = time()
t3.addtimes(t1, t2)
print("T1:", end="")
t1.displaydata()
print("T2:", end="")
t2.displaydata()
print("*************")
print("T3:", end="")
t3.displaydata()
