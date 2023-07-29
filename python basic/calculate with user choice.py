i=int(input("Enter no 1:"))
j=int(input("Enter no 2:"))
print("1.Add\n 2.Sub\n 3.mul\n 4.Div")
ch=int(input("Enter the choice"))
if(ch==1):
    ans=i+j
    print("Total is",ans)
elif(ch==2):
    ans=i-j
    print("Total is",ans)
elif(ch==3):
    ans=i*j
    print("Total is",ans)
elif(ch==4):
    ans=i/j
    print("Total is",ans)
else:
    print("Enter the correct choice")

