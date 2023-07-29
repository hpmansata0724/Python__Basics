s1=[10,0,20,30]
s2={'BMw','Audi','Honda City'}
s3=s1.union(s2)
print(s1)
print(s2)
print(s3)

x={"apple","banana","cherry"}
y={"google","microsoft","apple"}
x.intersection_update(y)
print(x)

x1={"apple","banana","cherry"}
y1={"google","microsoft","apple"}
z1=x1.intersection(y1)
print(z1)

x2={"apple","banana","cherry"}
y2={"google","microsoft","apple"}
z1=x1.intersection(y1)
print(z1)

x2={"apple","banana","cherry"}
y2={"google","microsoft","apple"}
x2.symmetric_difference_update(y2)
print(x2)

x3={"apple","banana","cherry"}
y3={"google","microsoft","apple"}
z3=x3.symmetric_difference(y3)
print(z3)