d1={'Rollno':101,'Name':'Mahesh','percentage':87.90}
print("Dictionary d1:",d1)
print("length:",len(d1))

for key in d1:
    print(key,":",d1[key])
print("Your rollno is:",d1['Rollno'])
print("Your name is :",d1['Name'])
print("Your percentage is:",d1['percentage'])

print("Rollno:",d1.get("Rollno"))

d2={'Rollno':101,'Name':'Mahesh','Percentage':87.90,'Name':'Rakesh'}
print(d2)

print(d2.keys())
for i in d2.values():
    print(i)

d3={'Rollno':101,'Name':'Mahesh','Percentage':87.90,'Name':'Rakesh'}
print(d2)

print(d2.keys())
for i in d2.values():
    print(i)

d3={'Rollno':101,'Name':'Mahesh','Percentage':87.90}
print("Values:",d3.values())
d3["Name"]="Rakesh"
d3["Age"]=23
print("Keys:",d3.keys())
print("Values:",d3.values())

print("item in d3:",d3.items())
for k,v in d3.items():
    print(k,":",v)
if "Name" in d3:
    print("Yes,'Name' is one of the keys in the 'd3' dictionary")
else:
    print("No,'Name'is not one of the keys in the 'd3'dictionary")