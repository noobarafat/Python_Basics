import random

class Account:
    def __init__(self, number, owner, pin, balance=0):
        self.number = number
        self.owner = owner
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} TK into account {self.number}. New balance: {self.balance} TK")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} TK from account {self.number}. New balance: {self.balance} TK")
        else:
            print("Insufficient funds")

    def check_balance(self):
        print(f"Current balance for account {self.number}: {self.balance} TK")

    def change_pin(self, new_pin):
        self.pin = new_pin
        print("PIN changed successfully")

    def display_help(self):
        print("Welcome to EasyBank!")
        print("You can use the following options:")
        print("1. Deposit - Add funds to your account")
        print("2. Withdraw - Remove funds from your account")
        print("3. Balance - Check your account balance")
        print("4. Change Password - Change your account PIN")
        print("5. Help - Display this help message again")
        print("6. Logout - Log out of your account")

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def generate_account_number(self):
        return str(random.randint(100000, 999999))

    def add_account(self, owner, pin, initial_deposit):
        if initial_deposit < 1000:
            print("You need to deposit a minimum of 1000 TK to create an account.")
            return None
        number = self.generate_account_number()
        account = Account(number, owner, pin, initial_deposit)
        self.accounts.append(account)
        print(f"Account {account.number} created successfully for {account.owner} with an initial deposit of {initial_deposit} TK.")
        return account

    def login(self, account_number, pin):
        account = self.find_account(account_number)
        if account:
            if account.pin == pin:
                return account
            else:
                print("Incorrect PIN. Login failed.")
                return None
        else:
            print("Account not found. Please create an account first.")
            return None

    def find_account(self, number):
        for account in self.accounts:
            if account.number == number:
                return account
        return None

def welcome_message():
    print("*" * 50)
    print("*" + " " * 48 + "*")
    print("*" + " Welcome to EasyBank!".center(48) + "*")
    print("*" + " " * 48 + "*")
    print("*" * 50)

def print_options():
    print("\nOptions:")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

def print_account_options():
    print("\nAccount Options:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Balance")
    print("4. Change Password")
    print("5. Help")
    print("6. Logout")

def main():
    welcome_message()
    input("Press Enter to continue...")
    bank = Bank("EasyBank")

    while True:
        print_options()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            acc_owner = input("Enter account owner name: ")
            acc_pin = input("Enter PIN number: ")
            while True:
                initial_deposit = float(input("Enter initial deposit amount (minimum 1000 TK): "))
                if initial_deposit >= 1000:
                    break
                else:
                    print("You need to deposit a minimum of 1000 TK to create an account.")
            account = bank.add_account(acc_owner, acc_pin, initial_deposit)

        elif choice == '2':
            acc_number = input("Enter account number: ")
            acc_pin = input("Enter PIN number: ")
            account = bank.login(acc_number, acc_pin)
            if account:
                print(f"Login successful. Welcome {account.owner}")
                while True:
                    print_account_options()
                    acc_choice = input("Enter your choice: ").strip()

                    if acc_choice == '1':
                        amount = float(input("Enter amount to deposit: "))
                        account.deposit(amount)

                    elif acc_choice == '2':
                        amount = float(input("Enter amount to withdraw: "))
                        account.withdraw(amount)

                    elif acc_choice == '3':
                        account.check_balance()

                    elif acc_choice == '4':
                        new_pin = input("Enter new PIN number: ")
                        account.change_pin(new_pin)

                    elif acc_choice == '5':
                        account.display_help()

                    elif acc_choice == '6':
                        print("Logged out.")
                        break

                    else:
                        print("Invalid choice. Please try again.")

        elif choice == '3':
            print("Thank you for using EasyBank!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
