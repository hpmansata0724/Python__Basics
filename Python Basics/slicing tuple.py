tup1=('Raju','Baju','Giju','Miju')
tup2=(1,2,3,4,5,6,7,6,4,3,1)
print(tup1)
print(tup2)
print("tup1[0]:",tup1[0])
print("tup2[:4]:",tup1[:3])
print("tup1[-3:-1]:",tup1[-3:-1])
print("tup2[-1:]:",tup2[-1:])
print("tup2[2:5]:",tup2[2:5])

print("Max tuple 1:",max(tup1))
print("Min tuple1:",min(tup1))
print("Max tuple 2:",max(tup2))
print("Max tuple2:",min(tup2))

print("'3'is",tup2.count(3),"times in tuple2")

print("Index of 'giju'in tuple1:",tup1.index('giju'))

print("is'giju' in tuple 1:",'giju'in tup1)
print("Is 'English'in tuple1:",'English'not in tup1)
print("Is '5'in Tuple2:",5 in tup2)

tup3=tup1+tup2
print(tup1)
print(tup2)
print(tup1*2)
print(tup2*3)

t1=(6,7,8)
t2=(1,2,3)
t3=(6,5,4)
tup4=t1,t2,t3
print(tup4)
for i in tup4:
    for j in i:
        print(j,end="")
    print("")

