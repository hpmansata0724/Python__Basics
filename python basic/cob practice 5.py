class converter:
    def celtofer(self):
        return(self.cal*1.8)+32
    def kilometertomiles(self):
        return self.km*0.62137

obj1=converter()
obj1.cal=float(input("Enter temperature in celsius:"))
obj1.fer=obj1.celtofer()
print(obj1.cal,"degree celsius equal to",obj1.fer,"farheniet")
obj1.km=float(input("enter in km :"))
obj1.miles=obj1.kilometertomiles()
print(obj1.km,"is equal to",obj1.miles,"miles")
