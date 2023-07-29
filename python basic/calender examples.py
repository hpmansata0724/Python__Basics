import calendar
cal=calendar.month(2022,7)
print("Here is the caleder:")
print(cal)
#User input
print("Calender of given month and year")
year=int(input("Enter month"))
month=int(input("Enter month"))
h=int(input("horizontal space"))
v=int(input("vertical space"))
print(calender.month(year,month,v,h))
#Leap year
print("Leap year:")
year1=int(input("Enter year to check it is a leap year or not"))
print(calender.isleap(year1))
y1=int(input("Enter year1"))
y2=int(input("Enter year2"))
print("there are",calender.leapdays(y1,y2),"leap years")
#Find weekdays
print("Weekdays:")
year2=int(input("Enter year:"))
month2=int(input("enter month"))
day2=int(input("Enter day:"))
print(calender.month(year2,month2))
print("No of day in week:",calender.weekday(year2,month2,day2))
#Full year calender
print("Full year calender:")
year3=int(input("enter year:"))
print(calendar.pracal(year3))