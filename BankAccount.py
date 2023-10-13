# This is the main project to create a Bank Account
# the class is BankAccount

import random

class BankAccount:

    def __init__(self, name, accountType ,balance = 0):
        self.name = name
        self.accountType = accountType
        self.balance = balance
        
    # create a new account
    def new_account(self):
        #self.name = str(input("Type in your name: "))
        #self.accountType = str(input("Type of account: "))
        self.balance = float(input("Initial balance for account: "))
        self.balance_info = open("balance_info.txt", "a")
        self.balance_info.write(str(self.balance) + "\n")
        self.balance_info.close
        self.accountNumber = str(random.randint(1, 1000000))
        
	
        self.Bank_Info=str(self.accountNumber)+"_"+self.accountType+"_"+self.name+"_"
	# function to deposit money
    def deposit(self):
        amount= float(input("Enter amount to be deposited: "))
        self.balance = self.balance + amount
        print(f"Amount deposited: {amount}  New Balance: {self.balance}")
        self.balance_info = open("balance_info.txt", "a")
        self.balance_info.write(str(self.balance) + "\n")
        self.balance_info.close()
        
        
	# function to withdraw money
	# the function should not allow to withdraw more than balance
    def withdraw(self):
        
        amount = float(input("Enter amount to be withdrawn: "))
       # assert self.balance > amount, "Incefficent balance to withdraw"
        if self.balance>=amount:
            self.balance = self.balance - amount
            print(f"Amount withdrawn: {amount}  New Balance: {self.balance}")
            self.balance_info = open("balance_info.txt", "a")
            self.balance_info.write(str(self.balance) + "\n")
            self.balance_info.close()
        else:
            print("Insufficient Balance")
            
        
    # display the function
    def display(self):
        print("The balance in your account is: ", self.balance)
        
    # see balance history
    def balance_history(self):
        self.balance_info = open("balance_info.txt", "r")
        self.file_lines = self.balance_info.readlines()
        for line in self.file_lines:
            print(line)
        self.balance_info.close()
        
    def Acc_info(self):
        print(self.Bank_Info)
        
        
        
 # main program
ch=9
 
while ch != 0:
 
    print("Welcome to Western ATM")
    print()
    print("Please choose from the following options")
    print()
    print("1 - Create a new account")
    print("2 - Deposit money")
    print("3 - Withdraw money")
    print("4 - Check balance")
    print("5 - Check account information")
    print("6 - Check balance history")
    print("0 - Exit")
    ch = int(input("Please select your option: "))
    
    
    
    if ch == 1:
        name = str(input("Type in your name: "))
        accountType = str(input("Type of account: "))
        my_Acc = BankAccount(name , accountType)
        my_Acc.new_account()
    elif ch == 2:
        my_Acc.deposit()
    elif ch == 3:
        my_Acc.withdraw()
    elif ch == 4:
        my_Acc.display()
    elif ch == 5:
        my_Acc.Acc_info()
    elif ch == 6:
        my_Acc.balance_history()
    elif ch == 0:
        print(" Thank you for using Western ATM")
        break
    else:
        print("Invalid option. Please choose again")
        
        
    







 
        
    
        
		
	
		