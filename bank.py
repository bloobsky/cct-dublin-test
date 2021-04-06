class BankAccount():
    def __str__(self):
        return 

    def __init__(self, owner, money):
        self.owner = owner
        self.money = money

    def withdraw(self, amount):
        if (amount > self.money):
            return print("Cannot do that")
        else:
            amount = self.money - amount 
            print(amount)

    def deposit(self, amount):
        amount = self.money + amount
        print (amount)


user = BankAccount('Mateusz', 1000)
user.withdraw(5000)
user.deposit(500)

print (user)
withdraw = int(input("Give me the value"))

user.withdraw(withdraw)


print (BankAccount)