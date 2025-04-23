import random
import time
class Account:
    def __init__(self,bal,acc,name):
        self.bal=bal
        self.name=name
        self.acc=acc
        print(f"Fetching acc details for {self.name}....")
    def credit(self,amount):
        self.bal += amount
        print("Rs",amount,"credited")
        print("Remaining balance is:",self.bal)
    def debit(self,amount):
        self.bal -= amount
        print("Rs",amount,"debited")
        print("Remaining balance is:",self.bal)
    def bank(self):
        while True:
            a=input("DEBIT,CREDIT OR CHECK BALANCE OR EXIT:  ").upper()
            if a=='DEBIT':
                b=int(input("Amount to be debited:"))
                if b>self.bal:
                    print("Amount exceeds current balance")
                else:
                    self.debit(b)
            elif a=="CHECK BALANCE":
                print(f"The current bank balance is : {self.bal}")
            elif a=='CREDIT':
                b=int(input("Amount to be credited:"))
                if b<1:
                    print("Amount to be credited should be greater than 1")
                else:
                    self.credit(b)
            elif a == "EXIT":
                print("Logging out from banking operations...\n")
                break
            else:
                print("Invalid operation")
def menu():
    print('                 Menu')
    a=int(input("1 For Creating Account\n2 For Login to existing Account\n"))
    return a

user={}
while True:
    a=menu()
    if a==1:
        pn=int(input("Enter mobile number"))
        if pn in user:
            print("Account already exists")
        else:
            name=input("Enter your Name:")
            pwd=input("Enter password")
            n=0
            s=random.randint(1000,9999)
            user[s]=[name,pwd,n,pn]
            print("Account created successfully!!")
            print(f'Your Account Number is:{s}')
            time.sleep(1)

    elif a==2:
        s=int(input("Enter Account Number"))
        if s in user:
            pwd=input("Enter password")
            if pwd==user[s][1]:
                s1 = Account(user[s][2], s, user[s][0])
                time.sleep(1)
                s1.bank()
                user[s][2] = s1.bal 
            else:
                print("Incorect Paassword")
        else:
            print("User doesnt exist")
        break
    
    else:
        print("Invalid option")
        break

                



