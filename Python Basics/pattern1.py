n=int(input("How many rows do you want to enter"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print("\r")
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print("\r")
