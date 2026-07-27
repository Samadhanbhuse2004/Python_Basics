class Bank:

    def __init__(self):
        self.database = {}
        self.current_user = None
        self.is_logged_in = False

        print("-" * 50)
        print("        Welcome to Python Bank")
        print("-" * 50)

    # ---------------- Registration ----------------
    def register(self):
        print("\n------ Registration ------")

        username = input("Enter Username: ")

        if username in self.database:
            print("Username already exists!")
            return

        password = input("Enter Password: ")

        # password, balance
        self.database[username] = {
            "password": password,
            "balance": 0
        }

        print("Registration Successful!")

    # ---------------- Login ----------------
    def login(self):

        print("\n------ Login ------")

        username = input("Username: ")
        password = input("Password: ")

        if username in self.database:

            if self.database[username]["password"] == password:
                self.current_user = username
                self.is_logged_in = True

                print("Login Successful")
                print(f"Welcome {username}")

            else:
                print("Wrong Password")

        else:
            print("User Not Found")

    # ---------------- Check Balance ----------------
    def check_balance(self):

        if self.is_logged_in:
            balance = self.database[self.current_user]["balance"]
            print(f"Current Balance = ₹{balance}")

        else:
            print("Please Login First")

    # ---------------- Deposit ----------------
    def deposit(self):

        if not self.is_logged_in:
            print("Please Login First")
            return

        amount = int(input("Enter Deposit Amount: ₹"))

        self.database[self.current_user]["balance"] += amount

        print("Amount Deposited Successfully")
        self.check_balance()

    # ---------------- Withdraw ----------------
    def withdraw(self):

        if not self.is_logged_in:
            print("Please Login First")
            return

        amount = int(input("Enter Withdraw Amount: ₹"))

        balance = self.database[self.current_user]["balance"]

        if amount > balance:
            print("Insufficient Balance")

        else:
            self.database[self.current_user]["balance"] -= amount
            print("Amount Withdrawn Successfully")
            self.check_balance()

    # ---------------- Bank Statement ----------------
    def bank_statement(self):

        if not self.is_logged_in:
            print("Please Login First")
            return

        print("\n========== BANK STATEMENT ==========")
        print(f"Account Holder : {self.current_user}")
        print(f"Balance        : ₹{self.database[self.current_user]['balance']}")
        print("====================================")

    # ---------------- Logout ----------------
    def logout(self):

        if self.is_logged_in:
            self.current_user = None
            self.is_logged_in = False
            print("Logged Out Successfully")

    # ---------------- Menu ----------------
    def menu(self):

        while True:

            print("\n========== MENU ==========")
            print("1. Register")
            print("2. Login")
            print("3. Check Balance")
            print("4. Deposit")
            print("5. Withdraw")
            print("6. Bank Statement")
            print("7. Logout")
            print("8. Exit")

            choice = input("Enter Choice: ")

            if choice == "1":
                self.register()

            elif choice == "2":
                self.login()

            elif choice == "3":
                self.check_balance()

            elif choice == "4":
                self.deposit()

            elif choice == "5":
                self.withdraw()

            elif choice == "6":
                self.bank_statement()

            elif choice == "7":
                self.logout()

            elif choice == "8":
                print("Thank You For Banking With Us")
                break

            else:
                print("Invalid Choice")


# Driver Code
obj = Bank()
obj.menu()