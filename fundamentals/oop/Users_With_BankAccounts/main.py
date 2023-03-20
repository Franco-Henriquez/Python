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
        # self.bank_name()
        BankAccount.all_accounts.append(self)
        #defaults
        self.account_id += 1

    # def bank_name(self, passed_bank_name):
    #     BankAccount.bank_name = passed_bank_name
    #     return self.bank_name

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


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        # self.account = BankAccount(user=self.name,int_rate=0.02, balance=0)
        self.accounts = {}
        self.account_type = "Checking"
    
    # other methods
    def make_new_account_type(self, int_rate=0.02, balance=0, account_type="Checking"):
        new_account_type = BankAccount(self.name, int_rate, balance)
        self.accounts[account_type] = new_account_type
    
    def make_deposit(self, amount, account_type):
        # your code here
        self.accounts[account_type].deposit(amount)

        
        return self
    
    def make_withdrawal(self, amount, account_type):
        # your code here
        self.accounts[account_type].withdraw(amount)
        return self
    
    def display_user_balance(self, account_type="Checking"):
        # your code here
        current_balance = self.accounts[account_type].balance
        name = self.accounts[account_type].user
        print(f"{name} current balance for {account_type} Account: ${current_balance}")
        return self
            


#creating account using associated User class to BankAccounts class
AlbertWesker_Account = User("Albert Wesker", "albert_wesker@umbrella.com")
AlbertWesker_Account.make_new_account_type()
print(AlbertWesker_Account.email)
AlbertWesker_Account.make_deposit(80, "Checking").make_withdrawal(60, "Checking").display_user_balance()


# Creating Accounts using BankAccounts class
ChrisRedfield_Account = BankAccount("Chris Redfield",.05, 50)
AdaWong_Account = BankAccount("Ada Wong",.02, 50)

BankAccount.all_info()
