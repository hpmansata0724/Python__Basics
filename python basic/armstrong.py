num=int(input("Enter the number"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if num==sum:
    print(num,"Is an armstron number")
else:
    print(num,"Is not an armstrong number")
