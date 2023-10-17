from random import randint

class User:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = randint(1000, 9999)
        self.transaction_history = []
        self.loan_taken = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount"

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                self.transaction_history.append(f"Withdrew ${amount}")
                return f"Withdrew ${amount}. New balance: ${self.balance}"
            else:
                return "Withdrawal amount exceeded"
        else:
            return "Invalid withdrawal amount"

    def check_balance(self):
        return f"Available balance: ${self.balance}"

    def check_transaction_history(self):
        return self.transaction_history

    def take_loan(self, amount, loan_feature):
        if loan_feature:
            if self.loan_taken < 2:
                self.balance += amount
                self.loan_taken += 1
                self.transaction_history.append(f"Loan of ${amount} taken")
                return f"Loan of ${amount} taken. New balance: ${self.balance}"
            else:
                return "You have already taken the maximum number of loans."
        else:
            return "Loan feature is currently off."

    def transfer(self, recipient, amount):
        if recipient.balance > 0 and amount <= self.balance:
            recipient.balance += amount
            self.balance -= amount
            self.transaction_history.append(f"Transferred ${amount} to Account {recipient.account_number}")
            return f"Transferred ${amount} to Account {recipient.account_number}. New balance: ${self.balance}"
        else:
            return "Account does not exist or insufficient funds for the transfer."

    def show_info(self):
        return f"Name: {self.name}, Email: {self.email}, Address: {self.address}, Account Type: {self.account_type}, Account Number: {self.account_number}, Balance: ${self.balance}"

class Admin:
    def __init__(self):
        self.users = []
        self.bank_balance = 0
        self.loan_feature = True

    def create_account(self, name, email, address, account_type):
        user = User(name, email, address, account_type)
        self.users.append(user)
        return f"Account created successfully! Your account number is {user.account_number}"

    def delete_account(self, account_number):
        for user in self.users:
            if user.account_number == account_number:
                self.users.remove(user)
                return f"Account {account_number} deleted successfully."

    def see_user_accounts(self):
        users_info = [user.show_info() for user in self.users]
        return "\n".join(users_info)

    def check_bank_balance(self):
        for user in self.users:
            self.bank_balance += user.balance
        return f"Total available balance in the bank: ${self.bank_balance}"

    def check_total_loan_amount(self):
        total_loan_amount = sum(user.loan_taken for user in self.users)
        return f"Total loan amount in the bank: ${total_loan_amount}"

    def toggle_loan_feature(self):
        self.loan_feature = not self.loan_feature
        return f"Loan feature is now {'on' if self.loan_feature else 'off'}"

# Main program
admin = Admin()

while True:
    print("\nSelect User or Admin:")
    print("1. User")
    print("2. Admin")
    print("3. Exit")

    user_choice = input("Enter your choice: ")

    if user_choice == "1":
        print("\nUser Options:")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        user_option = input("Select an option: ")

        if user_option == "1":
            name = input("Name: ")
            email = input("Email: ")
            address = input("Address: ")
            account_type = input("Select Account Type (Savings/Current): ")
            if account_type.lower() in ["savings", "current"]:
                account_info = admin.create_account(name, email, address, account_type)
                print(account_info)
            else:
                print("Invalid account type. Please select Savings or Current.")

        elif user_option == "2":
            account_number = int(input("Enter your account number: "))
            user = None
            for u in admin.users:
                if u.account_number == account_number:
                    user = u
                    break
            if user is None:
                print("Account not found.")
            else:
                while True:
                    print("\nUser Actions:")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Transaction History")
                    print("5. Take Loan")
                    print("6. Transfer Money")
                    print("7. Show Account Info")
                    print("8. Logout")

                    user_action = input("Select an action: ")

                    if user_action == "1":
                        amount = float(input("Enter the deposit amount: "))
                        print(user.deposit(amount))
                    elif user_action == "2":
                        amount = float(input("Enter the withdrawal amount: "))
                        print(user.withdraw(amount))
                    elif user_action == "3":
                        print(user.check_balance())
                    elif user_action == "4":
                        print("Transaction History:")
                        for transaction in user.check_transaction_history():
                            print(transaction)
                    elif user_action == "5":
                        if admin.loan_feature:
                            amount = float(input("Enter the loan amount: "))
                            print(user.take_loan(amount, admin.loan_feature))
                        else:
                            print("Loan feature is currently off. Cannot take a loan.")
                    elif user_action == "6":
                        recipient_account = int(input("Enter the recipient's account number: "))
                        recipient = None
                        for u in admin.users:
                            if u.account_number == recipient_account:
                                recipient = u
                                break
                        if recipient is None:
                            print("Recipient account does not exist.")
                        else:
                            amount = float(input("Enter the transfer amount: "))
                            print(user.transfer(recipient, amount))
                    elif user_action == "7":
                        print(user.show_info())
                    elif user_action == "8":
                        break
                    else:
                        print("Invalid action. Please choose from the given options.")

        elif user_option == "3":
            continue

        else:
            print("Invalid option. Please select User or Admin.")

    elif user_choice == "2":
        print("\nAdmin Options:")
        print("1. Create Account")
        print("2. Delete Account")
        print("3. Show User Accounts")
        print("4. Check Bank Balance")
        print("5. Check Total Loan Amount")
        print("6. Toggle Loan Feature")
        print("7. Logout")

        admin_option = input("Select an option: ")

        if admin_option == "1":
            name = input("Name: ")
            email = input("Email: ")
            address = input("Address: ")
            account_type = input("Select Account Type (Savings/Current): ")
            if account_type.lower() in ["savings", "current"]:
                account_info = admin.create_account(name, email, address, account_type)
                print(account_info)
            else:
                print("Invalid account type. Please select Savings or Current.")

        elif admin_option == "2":
            account_number = int(input("Enter the account number to delete: "))
            result = admin.delete_account(account_number)
            print(result)

        elif admin_option == "3":
            user_accounts = admin.see_user_accounts()
            print("\nUser Accounts:\n")
            print(user_accounts)

        elif admin_option == "4":
            bank_balance = admin.check_bank_balance()
            print(bank_balance)

        elif admin_option == "5":
            total_loan_amount = admin.check_total_loan_amount()
            print(total_loan_amount)

        elif admin_option == "6":
            loan_feature_status = admin.toggle_loan_feature()
            print(loan_feature_status)

        elif admin_option == "7":
            continue

        else:
            print("Invalid option. Please select a valid option.")
    elif user_choice == "3":
        print("Exiting the system.Thank you!")
        break


