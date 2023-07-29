n=int(input("Enter the number"))
add=0
mul=1
n1=n;
while(n1>0):
    s=n1%10
    add=add+s
    mul=mul*s
    n1=n1/10
print("sum of all digits",add)
print("mul of all digits",mul)
if(add==mul):
    print(n,"is perfect no")
else:
    print(n,"is not a perfect number")
