def checkerror(no):
    try:
        for i in range(1,int(no)+1):
            try:
                if (i%3==0):
                    raise IndexError(f"Error at position={str(i)}")
                else:
                    print(i)
            except IndexError as e:
                print(e)
    except ValueError as e:

        print("plz Enter the valid value")
n=input("Enter the number:")
checkerror(n)
