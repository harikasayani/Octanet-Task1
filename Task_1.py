class ATM:
    def __init__(self):
        self.accounts={}
        self.transactions={}
    def createaccount(self,id,pin,balance=0):
        self.id=id
        self.pin=pin
        self.balance=balance
        self.accounts[self.id]=[self.pin,self.balance]
        print("Account created successfully!")
    def accessaccount(self,id,pin):
        self.id=id
        self.pin=pin
        for key,val in self.accounts.items():
            if self.id==key:
                if self.pin==val[0]:
                    return True
        return False
    def withdraw(self,amount):
        self.amount=amount
        if(self.amount>self.accounts[self.id][1]):
            print("No sufficient balance!")
        else:
            self.accounts[self.id][1]-=self.amount
            self.transactions['Withdraw']=self.amount
            print("Withdraw successful!")
            for key,val in self.accounts.items():
                if(key==self.id):
                    print("After withdraw amount: ",end="")
                    print(val[1])
    def deposit(self,amount):
        self.amount=amount
        self.accounts[self.id][1]+=self.amount
        self.transactions['deposit']=self.amount   
        print("Amount deposited successfully!")  
        for key,val in self.accounts.items():
                if(key==self.id):
                    print("After deposit amount: ",end="")
                    print(val[1]) 
    def transaction(self):
        for key,val in self.transactions.items():
            print(key,"-->",val) 
    def transfer(self,target,amount):
        self.target=target
        self.amount=amount
        for key in self.accounts.keys():
            if key==self.target:
                self.withdraw(self.amount)
                self.accounts[self.target][1]+=self.amount
                self.transactions['transfer']=self.amount
                for key,val in self.accounts.items():
                    if(key==self.id):
                        print("After transfer amount: ")
                        print(val[1])
                return True
        return False
                
user=ATM() 
while(True):
    print("\n======== ATM INTERFACE ==========")
    print("1.Create Account")
    print("2.Access Account")
    print("3.Quit")
    print("=================================\n")
    ch=int(input("Enter your choice:"))
    if(ch==1):
        print("Create your account")
        id=int(input("Enter user id: "))
        pin=int(input("Enter pin number: "))
        balance=int(input("Enter balance: "))
        user.createaccount(id,pin,balance)
    elif(ch==2):
        print("Enter your details")
        id=int(input("Enter user id: "))
        pin=int(input("Enter pin number: "))
        res=user.accessaccount(id,pin)
        if(res):
            while(True):
                print("\n=== Options===")
                print("1.Withdraw")
                print("2.Deposit")
                print("3.transaction")
                print("4.transfer")
                print("5.Quit")
                print("==============\n")
                ch=int(input("Enter your choice"))
                if(ch==1):
                    amount=int(input("Enter amount to be withdraw: "))
                    user.withdraw(amount)
                elif(ch==2):
                    amount=int(input("Enter amount to be deposit: "))
                    user.deposit(amount)
                elif(ch==3):
                    user.transaction()
                elif(ch==4):
                    target=int(input("Enter transaction id: "))
                    amount=int(input("Enter amount to be transfer: "))
                    res=user.transfer(target,amount)
                    if(res):
                        print("Transfer successful!")
                    else:
                        print("Transfer failed!")
                elif(ch==5):
                    print("Thank you!")
                    break
        else:
            print("Create your account")
    elif(ch==3):
        print("Thank you!")
        break