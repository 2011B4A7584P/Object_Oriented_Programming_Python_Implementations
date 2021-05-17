# This is a program to simulate a simple working banking system
import random
from abc import ABCMeta, abstractmethod


class BankingApp(metaclass=ABCMeta):

    @abstractmethod
    def create_new_savings_account(self):
        return

    @abstractmethod
    def access_existing_savings_account(self):
        return

    @abstractmethod
    def withdraw(self):
        return

    @abstractmethod
    def deposit(self):
        return

    @abstractmethod
    def display_balance(self):
        return


class SavingsAccount:

    def __init__(self):
        print('Welcome to Citibank!')
        # [key][0] => name ; [key][1] => balance
        self.accounts = {}

    def create_new_savings_account(self, name, initial_deposit):
        self.account_number = random.randint(10000, 99999)
        self.accounts[self.account_number] = [name, initial_deposit]
        print('Savings Account with account number {} has been created successfully!'.format(self.account_number))

    def display_balance(self, acct_num):
        print('Available Balance : {}'.format(self.accounts[acct_num][1]))

    def withdraw(self, amount, acct_num):
        if amount > self.accounts[acct_num][1]:
            print('Insufficient Balance')
        else:
            self.accounts[acct_num][1] = self.accounts[acct_num][1] - amount
            print('Withdrawal Successful!')
            self.display_balance(acct_num)

    def deposit(self, amount, acct_num):
        self.accounts[acct_num][1] = self.accounts[acct_num][1] + amount
        print('Deposit Successful!')
        self.display_balance(acct_num)

    def access_existing_savings_account(self, name, acct_num):

        if acct_num in self.accounts.keys():
            if self.accounts[acct_num][0] == name:
                print('Authentication Successful!')
                while True:
                    print('Press 1 to check balance')
                    print('Press 2 to withdraw money')
                    print('Press 3 to deposit money')
                    print('Print 4 to exit out of your account')

                    userChoice = int(input())

                    if userChoice == 1:
                        self.display_balance(acct_num)
                    elif userChoice == 2:
                        print('Please enter the amount to withdraw')
                        amount = int(input())
                        self.withdraw(amount, acct_num)
                    elif userChoice == 3:
                        print('Please enter the amount to deposit')
                        amount = int(input())
                        self.deposit(amount, acct_num)
                    else:
                        break
            else:
                print('Authentication Unsuccessful!')
        else:
            print('Authentication Unsuccessful!')


if __name__ == '__main__':

    saving_account = SavingsAccount()

    while True:
        print('Press 1 to create a new savings account')
        print('Press 2 to access an existing account')
        print('Press 3 to exit')

        userChoice = int(input())

        if userChoice == 1:
            print('Please enter your name')
            name = input()
            print('Please enter your initial deposit')
            initial_deposit = int(input())
            saving_account.create_new_savings_account(name, initial_deposit)
        elif userChoice == 2:
            print('Please enter your name')
            name = input()
            print('Please enter your account number')
            acct_num = int(input())
            saving_account.access_existing_savings_account(name, acct_num)
        else:
            quit()
