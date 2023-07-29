print("1.Car\n2.Bike")
ch1=int(input("Enter the choice"))
if(ch1==1):
    print("You select car choice further:")
    ch2=int(input("Enter the choice for car"))
    if(ch2==1):
        print("You selected 'BMW'car")
    elif(ch2==2):
        print("you selected 'Audi'")
    elif(ch2==3):
        print("you selected'Amaze'")
    else:
        print("Invalid choice")
elif(ch1==2):
    print("Yoy selected the choice for the Bikes")
    ch2=int(input("Enter the choice for the bike"))
    if(ch2==1):
        print("You selected 'R15'bike")
    elif(ch2==2):
        print("You selected 'BMW gt1000'bike")
    elif(ch2==3):
        print("You selected 'Pulsar'bike")
    else:
        print("Invalid choice")

