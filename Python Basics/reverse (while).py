n=int(input("Enter the numbers:"))
Reversed_n=0
while n!=0:
    digit=n%10
    Reversed_n=Reversed_n*10+digit
    n//=10
print("Reversed number:" +str(Reversed_n))