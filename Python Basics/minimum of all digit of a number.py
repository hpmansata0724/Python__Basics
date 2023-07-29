n=int(input("Enter the number:"))
min=n%10
while(n>0):
    if(n%10<=min):
        min=n%10
    n=int(n/10)
print("Minimum of numbers is",min)