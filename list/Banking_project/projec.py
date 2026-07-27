def login(self):
    while True:  # Loop = clean retry, no recursion risk
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")  # string, no int()

        if username in self.database and password == self.database[username][0]:
            print('--------------------------------------------')
            print('Login Successful!')
            print('--------------------------------------------')
            self.curr_user = username
            self.is_logged_in = True
            print(f"=========== Current user: {self.curr_user} ===========")
            print('--------------------------------------------')
            break  # ← exit loop on success
        else:
            print('--------------------------------------------')
            print("Invalid username or password. Please try again.")
            print('--------------------------------------------')
            # loop automatically retries — no __init__() needed