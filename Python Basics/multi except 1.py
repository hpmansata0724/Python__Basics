try:
    a=int(input("Enter the value of a:"))
    b=int(input("Enter the number of b:"))
    c=a/b
    print("Ans",c)
except ValueError as e:
    print("Plz enter the valid value....")
except ZeroDivisionError as e:
    print("You cannot enter the value of b as zero")
print("Thanks for using the code")