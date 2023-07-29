n=int(input("How many rows you want to enter"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print("\r")
for i in range(1,n+1):

    for j in range(1,i+1):
        print(j,end="")
    print("\r")
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print("\r")

