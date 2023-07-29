s1={'apple','banana','mango','apple'}
print(s1)

print(("length of s1:",len(s1)))
for i in s1:
    print(i)

print("'Banana' is in s:",'Banana'in s1)
print("'chiku' is in s1:"'chiku'in s1)
print("'grapes' is in s1",'grapes' in s1)

s3=('physics','chemistry','biology')
print(s3)
s3.add("maths")
print("After insertion:",s3)

thisset={"apple","banana","cherry","apple"}
tropical=("pineapple","mango","cherry")
print(tropical)
print(thisset)

thisset1={"apple","banana","cherry"}
mylist=["kiwi","orange"]
thisset1.update(mylist)
print(thisset1)

s1={"",}
n=int(input("How many items do you want to add in set"))
print("Enter",n,"Elements:")
for i in range(0,n):
    ele=input("")
    s1.add(ele)
print(n,"Elements are:")
for i in s1:
    print(i)
