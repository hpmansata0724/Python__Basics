while True:
    print("Press 'q' for Quit")
    a=input("Enter the number:")
    if a=='q':
        break
    try:
        print("Trying...")
        a=int(a)
        if(a>6):
            print("you entered the number greater then 6")
    except Exception as e:
        print("Error is occoured :{e}")
print("Thanks for playing the game")