import re
import getpass
from datetime import datetime


class InsufficientBalanceError(Exception):
    """Raised when withdrawal amount exceeds available balance."""
    pass


class InvalidAmountError(Exception):
    """Raised when a deposit/withdrawal amount is invalid (negative, zero, non-numeric)."""
    pass


class Bank:

    MIN_PASSWORD_LENGTH = 4

    def __init__(self):
        # name mangling used intentionally -> __database is "more private" than _database
        self.__database = {}
        self.__current_user = None
        self.__is_logged_in = False

        self.__print_header("Welcome to Python Bank")

    # ---------------- Helper / Utility ----------------
    @staticmethod
    def __print_header(text):
        print("-" * 50)
        print(f"{text:^50}")
        print("-" * 50)

    @staticmethod
    def __is_valid_username(username):
        # only letters, numbers, underscore, 3-20 chars
        return bool(re.match(r"^[A-Za-z0-9_]{3,20}$", username))

    def __get_valid_amount(self, prompt):
        """Keeps asking until user enters a valid positive number. Returns float."""
        while True:
            raw = input(prompt).strip()
            try:
                amount = float(raw)
                if amount <= 0:
                    print("Amount must be greater than 0. Try again.")
                    continue
                return round(amount, 2)
            except ValueError:
                print("Invalid input. Please enter a numeric amount (e.g. 500 or 500.50).")

    def __require_login(func):
        """Decorator: ensures user is logged in before running the wrapped method."""
        def wrapper(self, *args, **kwargs):
            if not self.__is_logged_in:
                print("Please Login First")
                return
            return func(self, *args, **kwargs)
        return wrapper

    # ---------------- Registration ----------------
    def register(self):
        print("\n------ Registration ------")

        username = input("Enter Username (3-20 chars, letters/numbers/underscore): ").strip()

        if not self.__is_valid_username(username):
            print("Invalid username. Use 3-20 letters, numbers, or underscores only.")
            return

        if username in self.__database:
            print("Username already exists!")
            return

        # getpass hides password input in terminal (won't work in some notebook environments)
        try:
            password = getpass.getpass("Enter Password (min 4 chars): ")
        except Exception:
            password = input("Enter Password (min 4 chars): ")

        if len(password) < self.MIN_PASSWORD_LENGTH:
            print(f"Password must be at least {self.MIN_PASSWORD_LENGTH} characters.")
            return

        self.__database[username] = {
            "password": password,
            "balance": 0.0,
            "transactions": []  # store history: (type, amount, timestamp)
        }

        print("Registration Successful! You can now login.")

    # ---------------- Login ----------------
    def login(self):
        print("\n------ Login ------")

        if self.__is_logged_in:
            print(f"Already logged in as {self.__current_user}. Logout first.")
            return

        username = input("Username: ").strip()

        try:
            password = getpass.getpass("Password: ")
        except Exception:
            password = input("Password: ")

        user = self.__database.get(username)

        if user is None:
            print("User Not Found")
            return

        if user["password"] != password:
            print("Wrong Password")
            return

        self.__current_user = username
        self.__is_logged_in = True
        print("Login Successful")
        print(f"Welcome {username}")

    # ---------------- Check Balance ----------------
    @__require_login
    def check_balance(self):
        balance = self.__database[self.__current_user]["balance"]
        print(f"Current Balance = Rs. {balance:.2f}")

    # ---------------- Deposit ----------------
    @__require_login
    def deposit(self):
        amount = self.__get_valid_amount("Enter Deposit Amount: Rs. ")

        self.__database[self.__current_user]["balance"] += amount
        self.__log_transaction("Deposit", amount)

        print("Amount Deposited Successfully")
        self.check_balance()

    # ---------------- Withdraw ----------------
    @__require_login
    def withdraw(self):
        amount = self.__get_valid_amount("Enter Withdraw Amount: Rs. ")
        balance = self.__database[self.__current_user]["balance"]

        try:
            if amount > balance:
                raise InsufficientBalanceError("Insufficient Balance")

            self.__database[self.__current_user]["balance"] -= amount
            self.__log_transaction("Withdraw", amount)
            print("Amount Withdrawn Successfully")
            self.check_balance()

        except InsufficientBalanceError as e:
            print(f"Transaction Failed: {e}")

    # ---------------- Transaction Logging ----------------
    def __log_transaction(self, tx_type, amount):
        entry = {
            "type": tx_type,
            "amount": amount,
            "time": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        }
        self.__database[self.__current_user]["transactions"].append(entry)

    # ---------------- Bank Statement ----------------
    @__require_login
    def bank_statement(self):
        user_data = self.__database[self.__current_user]

        print("\n========== BANK STATEMENT ==========")
        print(f"Account Holder : {self.__current_user}")
        print(f"Balance        : Rs. {user_data['balance']:.2f}")
        print("-" * 38)
        print("Recent Transactions:")

        transactions = user_data["transactions"]
        if not transactions:
            print("  No transactions yet.")
        else:
            for tx in transactions[-5:]:  # show last 5 only
                print(f"  [{tx['time']}] {tx['type']:<8} Rs. {tx['amount']:.2f}")

        print("=====================================")

    # ---------------- Logout ----------------
    def logout(self):
        if self.__is_logged_in:
            print(f"Goodbye, {self.__current_user}!")
            self.__current_user = None
            self.__is_logged_in = False
            print("Logged Out Successfully")
        else:
            print("No user is currently logged in.")

    # ---------------- Menu ----------------
    def menu(self):

        menu_options = {
            "1": ("Register", self.register),
            "2": ("Login", self.login),
            "3": ("Check Balance", self.check_balance),
            "4": ("Deposit", self.deposit),
            "5": ("Withdraw", self.withdraw),
            "6": ("Bank Statement", self.bank_statement),
            "7": ("Logout", self.logout),
            "8": ("Exit", None),
        }

        while True:
            print("\n========== MENU ==========")
            for key, (label, _) in menu_options.items():
                print(f"{key}. {label}")

            choice = input("Enter Choice: ").strip()

            if choice == "8":
                print("Thank You For Banking With Us")
                break

            option = menu_options.get(choice)

            if option is None:
                print("Invalid Choice. Please enter a number between 1-8.")
                continue

            _, action = option
            try:
                action()
            except Exception as e:
                # catch-all so one bad interaction doesn't crash the whole program
                print(f"Something went wrong: {e}")


# Driver Code
if __name__ == "__main__":
    obj = Bank()
    obj.menu()