class BankAccount:
    def __init__(self, name, starting_balance):
        full_name = name.split()
        print(full_name)
        self.first_name = full_name[0]
        self.last_name = full_name[1]
        self.balance = starting_balance
        self.history = []

    def get_balance(self):
        print("Hello " + self.first_name + " " + self.last_name + " your balance is $" + str(self.balance))

    def add_money(self, amount):
        self.balance += amount
        self.history.append("+ " + str(amount))
        print("$" + str(amount) + " has been credited to your account.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Sorry you cannot withdraw that amount")
        else:
            self.balance -= amount
            self.history.append("- " + str(amount))
            print("$" + str(amount) + "  has been debited to your account.")

    def print_history(self):
        print(self.history)


def main():
    account1 = BankAccount("Abheek Bajaj", 32)
    account1.get_balance()
    account1.add_money(11)
    account1.withdraw(2)
    account1.get_balance()
    account1.withdraw(1000)
    account1.print_history()

    account2 = BankAccount("XXX YYY", 2000)
    account2.get_balance()


if __name__ == "__main__":
    main()
