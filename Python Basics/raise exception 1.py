def increment(no):
    try:
        no=int(no)
        return no+1
    except:
        raise ValueError("plz Enter valid value")
n=input("Enter no:")
ans=increment(n)
print(f"Next value is:{ans}")
