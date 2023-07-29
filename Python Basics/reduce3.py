n=int(input("How many elements do you want to enter in list"))
list1=[]
print("Enter",n,"Elements:")
for i in range(0,n):
    ele=int(input(""))
    list1.append(ele)
list2=list(filter(lambda x:x%5==0,list1))
print("list1",list1)
print("filtered list",list2)