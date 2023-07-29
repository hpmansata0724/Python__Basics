class listclass:
    # l1 = []
    #
    def __init__(self, list1, n):
        self.l1 = list1
        self.n = n

    def Displaylist(self):
        print(self.n, "elements are:")
        for item in self.l1:
            print(item)

    def sumofall(self):
        self.sum = 0
        for item in range(0, len(self.l1)):
            self.sum = self.sum + self.l1[item]
        print("sem of all elements=", self.sum)

    def sumofeven(self):
        self.sum = 0
        for item in range(0, len(self.l1)):
            if (self.l1[item] % 2 == 0):
                self.sum = self.sum + self.l1[item]
        print("sum of all elements", self.sum)

    def maximinimum(self):
        print("max elements", max(self.l1))
        print("min elements", min(self.l1))

    def sorting(self):
        self.l2 = sorted(self.l1)
        self.l3 = sorted(self.l1, reverse=True)
        print("ascending order:")
        for i in self.l2:
            print(i)
            print(n, "descending order:")
            for i in self.l3:
                print(i)


n = int(input("How many elements:"))
l1 = []
print("enter", n, "elements:")
for i in range(0, n):
    l1.append(int(input()))

obj = listclass(1, n)
print("1.sum\n2.sum of even\n3.maximum\n4.sorting\n5.display list")
ch = int(input("Enter the choice:"))
if ch == 1:
    obj.sumofall()
elif ch == 2:
    obj.sumofeven()
elif ch == 3:
    obj.maximinimum()
elif (ch == 4):
    obj.sorting()
elif (ch == 5):
    obj.displaylist()
else:
    print("invalid choice")
