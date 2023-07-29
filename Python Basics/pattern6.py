# n=int(input("Enter the number:"))
# for i in range(1,n+1):
#     for j in range(i,0,-1):
#         print(j,end="")
#     print("\r")

# n=int(input("Enter the number:"))
# print("")
# for i in range(1,n+1):
#     for j in range(i,n+1):
#         print(j,end="")
#     print("3")

# n=int(input("Enter the number:"))
# print("")
# for i in range(n,0,-1):
#     for j in range(i,n+1):
#         print(j,end="")
#         print("\r")
n=int(input("Enter the number:"))
print("")
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
    print("\r")
