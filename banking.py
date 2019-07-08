
    import sys
    class Customer:
       "Customer Class With Bank Operation"
        bank_name="Apna Bank"
        def __init__(self,name,balance=0.0)
            self.name=name
            self.balance=balance
        def deposite(self,amt)
            self.balance=self.balance+amt
            print("Balance After Deposite Is:",self.balance)
        def withdrawal(self,amt)
            if amt>self.balance
                print("Insufficient Balance!!!!!Cannot Perform This Operation")
                sys.exit()
            else:    
                self.balance=self.balance-amt
                print("Balance After Withdrawal Is:",self.balance)
    print("Welcome To!!!",Customer.bank_name)
    name=input("Enter Your Name:")
    c=Customer(name)
    while True:
        print("D-Deposite\nW-Withdrawal\nE-exit")
        option=input("Enter Your Option:")
        if option=='d' or option=='D':
            amt=float(input("Enter Amount:"))
            c.deposite(amt)
        elif  option=='w' or option=='W':
            amt=float(input("Enter Amount:"))
            c.withdrawal(amt)n",
        elif option=='e' or option=='E':
            print("Thanks For Banking With Us!!!!!")
            sys.exit()
        else:
            print("Invalid Option!!!Please Choose Valid Option!!!")
