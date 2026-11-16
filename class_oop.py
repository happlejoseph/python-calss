

# class Car:

#     def __init__(self, name, year):
#         self.name = name
#         self.year = year

#     def start(self):
#         print('car started')



# # objects
# car1 = Car('alto', '1990')
# car2 = Car('benz', '1980')

# car1.start()
# car2.start()

# print(car1.name, car1.year)
# print(car2.name, car2.year)





# Bank Example
class Account:

    def __init__(self, account_num, account_balance):
        self.account_num = account_num
        self.account_balance = account_balance

    def withdraw(self, amount):
        if self.account_balance - amount > 0:
            self.account_balance = self.account_balance - amount
            print('withdraw successfull')

        else: print('Insefient Balance')

    def display(self):
        print('Your account balance is {}'.format(self.account_balance))


account_one = Account('A123', 1000)
account_two = Account('B123', 500)

amount = int(input('Enter the amount to withdraw from account one: '))
account_one.withdraw(amount)
account_two.display(amount)