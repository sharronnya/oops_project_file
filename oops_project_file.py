class ATM:
    def __init__(self, balance):
        self._balance = balance
        self._mini_statement = []

    def check_balance(self):
        print(f"Your current balance is: ${self._balance}")

    def show_mini_statement(self):
        print("\n------ MINI STATEMENT -------")

        if len(self._mini_statement) == 0:
            print("No transactions found.")

        else:
            for i in self._mini_statement:
                print(i)
        print(f"Available Balance: ${self._balance}")

class Transaction(ATM):

    def credit(self):

        amount = float(input("Enter amount to credit: "))
        if amount <= 0:
            print("Please enter a positive amount.")

        else:
            self._balance += amount
            self._mini_statement.append(f"Credited: ${amount}")

            print(f"${amount} credited to your account.")

        def debit(self):

            amount = float(input("Enter amount to debit: "))

            if amount <= 0:
                print("Please enter a positive amount.")

            elif amount > self._balance:
                print("Insufficient balance.")

            else:
                self._balance -= amount
                self._mini_statement.append(f"Debited:{amount}")
                print(f"${amount} debited from your account.")

class User(Transaction):

    def menu(self):

        while True:

            print("\n-------- ATM MENU -------")

            print("1. Credit")
            print("2. Debit")
            print("3. Balance")
            print("4. Mini Statement")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                self.credit()

            elif choice == '2':
                self.debit()

            elif choice == '3':
                self.check_balance()

            elif choice == '4':
                self.show_mini_statement()

            elif choice == '5':
                print("Thank you for using the ATM. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")


# object creation
obj = User(50000)

#method calling
obj.menu()


                                                

        