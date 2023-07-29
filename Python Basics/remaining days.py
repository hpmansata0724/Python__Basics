days=int(input("Enter total days:"))
year=days/365
temp=days%365
month=temp/30
redayas=temp%30
print("Total days")
print("Year:",year)
print("remaining days:",redayas)
print("Remaining month:",month)