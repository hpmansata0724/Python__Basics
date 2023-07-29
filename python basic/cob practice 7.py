class bank:
    bankname = "hdfc bank"

    def __init__(self):
        print("welcome in", bank.bankname, "services")

    def setaccountdetails(self):
        self.accountno = int(input("Enter your account number"))
        self.accountname = input("Enter account holder name")
        self.typeofaccount = input("Enter type of account(saving/current):")
        self.pinno = int(input("Enter your pinno:"))
        self.mainbalance = float(input("Enter your initial main balance:"))

    def getaccountdetails(self):
        no = int(input("To display account details enter your account number:"))
        if (no == self.accountno):
            print("*****************")
            print("account number", self.accountno)
            print("account name", self.accountname)
            print("type of account", self.typeofaccount)
            print("main  balance", self.mainbalance)
            print("******************")
        else:
            print("Enter valid account number")

    def depositamount(self):
        amt = float(input("Enter deposit amount:"))
        pno = int(input("Enter your pin no"))
        if (pno == self.pinno):
            self.mainbalance = self.mainbalance + amt
            print(amt, "is created in your amount")
            self.displaymainbalance()
        else:
            print("Invalid pin number")

    def withdrawamount(self):
        if (self.mainbalance >= 500.0):
            amt = float(input("Enter withdraw amount:"))
            pno = int(input("Enter your pinno:"))
            if (pno == self.pinno):
                self.mainbalance = self.mainbalance - amt
                print(amt, "is debited in your account")
                self.displaymainbalance()
            else:
                print("invalid pinno")
        else:
            print("sorry...! you don't have sufficient balance in your account")

    def displaymainbalance(self):
        print("Now,your main balance is:", self.mainbalance)


customer1 = bank()
while True:
    print(
        "1.set account details\n2.display account details\n3.deposit amount\n4.withdraw amount\n5.display main balance\n6.exit")
    ch = int(input("Enter the choice:"))
    if (ch == 1):
        customer1.setaccountdetails()
    elif (ch == 2):
        customer1.getaccountdetails()
    elif (ch == 3):
        customer1.depositamount()
    elif (ch == 4):
        customer1.withdrawamount()
    elif (ch == 5):
        customer1.displaymainbalance()
    elif (ch == 6):
        print("Thank you to choose", bank.bankbalance, "services")
        break
    else:
        print("Invalid choice")
