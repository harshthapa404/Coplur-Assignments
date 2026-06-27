#Assignment 12 

#In this we have to create the balance amount private. 
#And we can't access the balance amount 


class BankAccount:

    def __init__(self,balance=0):
        self.__balance=balance      #Private attribute 
    
    def deposit_amount(self,amount):

        self.__balance = self.__balance + amount
        print(f"\nDeposit Amount : {amount}")

    def withdraw_amount(self,amount):

        if amount <= self.__balance:
            self.__balance = self.__balance - amount
            print(f"\nWithdrawn Amount : {amount}")

        else: 
            print("\nInsufficient Balance Withdrawn denied")


    def get_balance(self):

        print(f"\nBalance : {self.__balance}")




add=BankAccount(5000)       #This is the balance amount that we have.

add.get_balance()           #Here we created a function to get the balance and balance is the private attribute.

add.deposit_amount(500)     #This is the deposit amount that we deposited.

add.get_balance() 

add.withdraw_amount(1000)    #This is the withdrawn amount that i want to withdraw.

add.get_balance() 

add.withdraw_amount(5500)   #This will show insufficient balance because withdrawn amount more than the balance amount.