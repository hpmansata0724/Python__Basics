def checkeligibility(a,w):
    try:
        if a<18 or w<40:
            raise ValueError("You are not eligible...Try again for next time")
        else:
            print("Congratulation....!!")
            print("You are selected for entrance exam")
            print(f"Your age and weight are:{a}and {w}kg respectively")
    except ValueError as e:
        print(e)
    age=int(input("Enter the age of student:"))
    weight=float(input("Enter the weight of student:"))
    checkeligibility(age,weight)