x=int(input("Enter the the Number limit for structure"))
if x%2==0:
    for i in range(1,x+1):
        for j in range(1,x+1):
            if i==1 or i==x or j==1 or j==x:
                print("*",end="")
            else:
                print("",end="")
else:
    print("Please enter odd number")