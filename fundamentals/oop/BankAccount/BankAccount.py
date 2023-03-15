class BankAccount:
    bank_name = "Banko Umbrella"
    all_accounts = []
    account_id = 0
    # don't forget to add some default values for these parameters!
    def __init__(self, user, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon

        #account id 1 will be checking
        # id 2 will be savings
        # id 3 will be money market
        self.user = user
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        #defaults
        self.account_id += 1

    
        
    def deposit(self, amount):
        # your code here
        self.balance += amount
        # self.display_account_info()
        return self

    def withdraw(self, amount):
        # your code here with RE Merchant voice
        if self.balance >= amount:
            self.balance -= amount
            # self.display_account_info()
        elif self.balance < amount:
            print("Not enough cash, strangar!")
            print("You will now be charged a $5 for your inconvenience.")
            self.balance -= 5
            print(f"Current Balance: ${self.balance}")
            print("And an additional $5 for processing.")
            self.balance -= 5
            print(f"Current Balance: ${self.balance}")
            if self.balance + 10 <= -1:
                print("You account is negative, you will be charged an additional $10 as per policy agreement")
                self.balance -= 10
                print(f"Current Balance: {self.balance}")
                print("Any future transgressions while your account is negative, will result in an additional $30 account-upkeeping fee")
                if self.balance + 20 <= -5:
                # delinquent
                    print("Due to your account balance being already negative at the time of withdrawal, you will be charged a $30 account-upkeeping fee.")
                    self.balance -= 30
                    print("Heh heh heh... Thank you!")
                    print(f"Current Balance: {self.balance}")
        return self
                
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
        # your code here
    def yield_interest(self):
        self.int_amount = self.int_rate*self.balance
        self.balance += self.int_amount
        # self.display_account_info()
        return self
        # your code here
    @classmethod
    def all_info(cls):

        # we use cls to refer to the class
        for account in cls.all_accounts:
            acc = account
            print("")
            print("##################################")
            print(f"###### User: {acc.user} ######")
            print("##################################")
            print(f"Bank Name: {acc.bank_name}")
            print(f"Account ID: {acc.account_id}")
            print(f"Account Balance: {acc.balance}")
            print(f"Interest Rate: {acc.int_rate}")

            # need to figure out why this wouldn't work
            # for key, value in account.items():
            #                 print(f"{key}: {value}")

# Creating Accounts
ChrisRedfield_Account = BankAccount("Chris Redfield",.05, 50)
AdaWong_Account = BankAccount("Ada Wong",.02, 50)
# Changing bank for Chris only because he works for US gov
ChrisRedfield_Account.bank_name = "Bank Americana"

# Testing chaining methods
ChrisRedfield_Account.deposit(100).deposit(100).deposit(100).withdraw(50).yield_interest().display_account_info()
AdaWong_Account.deposit(100).deposit(100).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()

# Getting all info using a method that iterates through a list of object data (not sure if dict)
BankAccount.all_info()
# print(BankAccount.all_accounts[0].balance)





