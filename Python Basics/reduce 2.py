#print table using format function
def formattable(no):

    l1=[no*i for i in range(1,11)]
    for index,value in enumerate(l1):
        sentence="{}*{}={}".format(no,index+1,value)
        print(sentance)
no=int(input("Enter the number:"))
formatTable(no)
for i,obj in enumerate(list1):
    print("Details of employee",i+1,":")
    obj.getDetails()

