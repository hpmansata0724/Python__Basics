# n=int(input("Enter the number:"))
# k=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(k)
#         k+=1
#         print("\r")
# n=int(input("Enter the number:"))
# print("")
# k=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if(k%2==1):
#             print("1")
#         else:
#             print("0")
#         k+=1
#     print("")
# n=int(input("Enter the number:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(i==1 or i==n or j==1 or j==n):
#             print("*",end=" ")
#         else:
#             print("",end=" ")
#     print("\r")
# n=int(input("Enter the number:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if(i==1 or i==n or j==1 or j==n or i==j or i+j==n+1):
#             print("*",end="")
#         else:
#             print("",end="")
#     print("\r")
# n=int(input("Enter the number:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(i==1 or i==n or j==1 or j==n or i==(n+1)/2 or j==(n+1)/2):
#             print("*",end="")
#         else:
#             print("",end="")
#     print("\r")
n=int(input("Enter the number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i==(n+1)/2 or j==(n+1)/2 or (i==1 and j<(n+1)/2) or (i==n and j<=(n+1)/2 or (j==1 and i<=(n+1)/2)) or (j==n and i>=(n+1)/2)):
            print("*",end="")
        else:
            print("",end="")
    print("\r")