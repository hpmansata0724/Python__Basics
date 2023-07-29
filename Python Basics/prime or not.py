num=int(input("Enter a number:"))
flag=False
if num >1:
    for i in range(2,num):
        if(num%i)==0:
            flag=True
            break
if not flag:

     print(num,"It is a prime number")

else:
     print(num,"Not a prime number")








