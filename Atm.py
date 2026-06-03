class Atm:
    def __init__(self):
        self.__pin = None
        self.__balance = int(0)
        self.menu()

    def menu(self):
        while True:
            user_input = input("""
                                Welcome to our bank sir !
                                How can we help you today !
                                1. create pin
                                2. change pin
                                3. check balance
                                4. deposit money
                                5. withdraw money
                                6. exit
    """)
            

            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.change_pin()
            elif user_input == "3":
                self.check_balance()
            elif user_input == "4":
                self.deposit()
            elif user_input == "5":
                self.withdraw()
            elif user_input == "6":
                break
            else:
                print("Invalid option, please choose between 1 to 6.")
                break

    def create_pin(self):
        self.__pin = input("enter new pin: ")
        print("pin set successfully")
    
    def change_pin(self):
        __current_pin = input("enter current pin: ")
        if __current_pin == self.__pin:
            self.__pin == input("enter new pin: ")
            print("pin changed successfully")
        else:
            print("pin not matched, try again")
            self.change_pin()
    
    def check_balance(self):
        __current_pin = input("enter pin: ")
        if __current_pin == self.__pin:
            print(f"Current Balance = {self.__balance}")
        else:
            print("pin not matched, try again")
            self.check_balance()
    
    def deposit(self):
        __current_pin = input("enter pin: ")
        if __current_pin == self.__pin:
            __temp = int(input("Enter amount to deposit: "))
            self.__balance += __temp
            print(f"Current balance = {self.__balance}")
        else:
            print("pin not matched, try again")
            self.deposit()

    def withdraw(self):
        __current_pin = input("enter pin: ")
        if __current_pin == self.__pin:
            print("Current balance = ", self.__balance)
            __temp = int(input("Enter amount to withdraw: "))
            if __temp <= self.__balance:
                self.__balance -= __temp
            print(f"Current balance = {self.__balance}")
        else:
            print("pin not matched, try again")
            self.withdraw()
