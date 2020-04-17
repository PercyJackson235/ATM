#-*-coding:utf8;-*-
#qpy:console
from time import sleep
from decimal import Decimal

class Bank:
    def __init__(self, balance=1000):
        self.balance = Decimal(str(balance)+'.00')
        self.run = True
    def checkbalance(self):
        print(f'Bank balance is : ${self.balance}')
        sleep(1)
    def deposit(self):
        amount = self.get_num()
        self.balance += amount
        self.checkbalance()
    def withdraw(self):
        while True:
            amount = self.get_num()
            if amount > self.balance:
                print("You don't have the money for that transaction.")
                print(f'You only have ${self.balance} which is less than ${amount}.')
                sleep(2)
            else:
                break
        self.balance -= amount
        self.checkbalance()
    def menu(self):
        menu1 = 'Would you like to : '
        menu2 = '1 - add or deposit'
        menu3 = '2 - subtract or withdraw'
        menu4 = '3 - check balance'
        menu5 = '4 - quit'
        print(menu1, menu2, menu3, menu4, menu5, sep='\n')
    def greeting(self):
        print('Welcome customer to the Bank of Python!')
        print('Your menu responds line number or keyword')
        sleep(1)
        self.menu()
    def shutdown(self):
        self.run = False
        print('Getting Ready to Shutdown....')
        sleep(1)
    def num_check(self, num):
        try:
            num = int(num)
            if num < 0:
                print('No negative numbers.')
                return None
            return Decimal(str(num)+'.00')
        except:
            print("That isn't a number.")
            print('Please try again.')
            return None
    def get_num(self):
        while True:
            amount = input('What is the amount : ').replace('$',"")
            num = self.num_check(amount)
            if num != None:
                return num
        
def main():
    bank = Bank()
    bank.greeting()
    while bank.run:
        action = input('Which action would you like to do : ').strip().lower()
        if action in [ '1', 'add', 'deposit', 'd']:
            bank.deposit()
        elif action in [ '2', 'subtract', 'sub', 'withdraw', 'w']:
            bank.withdraw()
        elif action in [ '3', 'check balance', 'check', 'balance', 'b', 'bal']:
            bank.checkbalance()
        elif action in [ '4', 'quit', 'shutdown', 'q', 'exit']:
            bank.shutdown()
            continue
        else:
            print('That is not a valid command.')
            sleep(1)
        bank.menu()
    print('Thank you for banking with us, Valued Customer.')


if __name__ == '__main__':

    main()