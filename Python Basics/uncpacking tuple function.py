fruits=("apple","banana","cherry")
print("Packing:")
print(fruits)
print("Unpacking:")
fruits1=("apple","banana","cherry")
(green,yellow,red)=fruits1
print(green)
print(yellow)
print(red)

fruits2=("apple","banana","cherry","strawberry","rasberry")
(green,yellow,*red)=fruits2
print(green)
print(yellow)
print(red)