class complex:
    def __init__(self,real=1.6,image=1.6):
        self.real=real
        self.image=image
    def addition(self,c1,c2):
        self.real=c1.real+c1.real
        self.image=c1.image+c2.image
    def display(self):
        print(f"(self.real)+(self.image)")

c1=complex(2.7,3.5)
c2=complex(1,6)
c3=complex()
c3.addition(c1,c2)
print("C1:",end="")
c1.display()
print("C2:",end="")
c2.display()
print("*********")
print("C3:",end="")
c3.display()