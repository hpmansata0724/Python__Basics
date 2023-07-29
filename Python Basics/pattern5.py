# n=int(input("Enter the number:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if(j==1):
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#     print("\r")
# n=int(input("Enter the number:"))
# print("")
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if(i%2==1):
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#     print("\r")
# n=int(input("Enter the number:"))
# print("")
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if(j==1 or i==n or i==j):
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#     print("\r")
n=int(input("Enter the number:"))
print("")
for i in range(1,n+1):
    for j in range(1,i+1):
        if((i+j)%2==0):
            print("1",end=" ")
        else:
            print("0",end=" ")
    print("\r")