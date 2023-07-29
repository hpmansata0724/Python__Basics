try:
    i=int(input("Enter a number:"))
    c=1.0/i
    print(c)
except Exception as e:
    print(e)
    exit()
finally:
    print("we are done")
print("Thanks for using the program")
