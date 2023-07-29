tup1=(10,22,30,40,50,60)
print(tup1)
print("length=",len(tup1))
#Separate
for i in tup1:
    print(i)

n=int(input("How many elements do you wanty to enter in the tuple"))
list1=[]
tup2=()
print("Enter",n,"ELements:")
for i in range(0,n):
    ele=int(input(""))
    list1.append(ele)
tup2=tuple(list1)
print(tup2)
for i in tup2:
    print(i)