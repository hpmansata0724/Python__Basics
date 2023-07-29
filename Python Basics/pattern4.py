# n=int(input("How many rows do you want to you enter"))
# for i in range(1,n+1):
#     for j in range(i,0,-1):
#         print(j,end="")
#     print("\r")
# n=int(input("How many rows do you want to enter"))
# print("")
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(j,end="")
#     print("")
# n=int(input("Enter number"))
# print("")
# for i in range(n,0,-1):
#     for j in range(i,n+1):
#         print(j,end="")
#     print("\r")
n=int(input("Enter the number:"))
for i in range(n,0,-1):
    for j in range(n,i-1,-1):
        print(j,end="")
    print("")