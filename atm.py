class ATM:
    def _init_(self):
        # Simulated user database (username: [PIN, balance])
        self.users = {
            "user1": ["1234", 1000.0],
            "user2": ["5678", 2500.0]
        }
        self.current_user = None

    def login(self):
        print("=== Welcome to Python ATM ===")
        username = input("Enter your username: ")
        if username in self.users:
            pin = input("Enter your PIN: ")
            if pin == self.users[username][0]:
                self.current_user = username
                print(f"\nLogin successful. Welcome, {username}!\n")
                self.menu()
            else:
                print("Invalid PIN.")
        else:
            print("Username not found.")

    def menu(self):
        while True:
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            choice = input("Select an option (1-4): ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                print("Thank you for using Python ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

    def check_balance(self):
        balance = self.users[self.current_user][1]
        print(f"Your current balance is: ${balance:.2f}\n")

    def deposit(self):
        try:
            amount = float(input("Enter amount to deposit: $"))
            if amount > 0:
                self.users[self.current_user][1] += amount
                print(f"${amount:.2f} deposited successfully.\n")
            else:
                print("Amount must be positive.\n")
        except ValueError:
            print("Invalid input. Please enter a numeric value.\n")

    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: $"))
            balance = self.users[self.current_user][1]
            if 0 < amount <= balance:
                self.users[self.current_user][1] -= amount
                print(f"${amount:.2f} withdrawn successfully.\n")
            else:
                print("Insufficient funds or invalid amount.\n")
        except ValueError:
            print("Invalid input. Please enter a numeric value.\n")


# Run the ATM program
if _name_ == "_main_":
    atm = ATM()
    atm.login()
