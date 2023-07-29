# n=int(input("Enter n"))
# s=0
# for i in range(1,n+1):
#     if(n%2!=0):
#         print(i,end="")
#         s=s+i
#
#         print("sum of odd is",s)

# n=int(input("Enter n"))
# for i in range(1,n+1):
#     print(n,"*","i","=","n*i")
n = int(input("Enter the number"))  # 3
j = 2 * n  # j=6
for i in range(1, n):
    print(i, j, end="")
    j = j - 1
    print("")
