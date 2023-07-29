try:
    a = float(input("Enter the value of a:"))
    b = float(input("Enter the value of b:"))
    c = a / b
except ZeroDivisionError as e:
    print(e)

else:
    print("Div=", c)
finally:
    print("we are done")