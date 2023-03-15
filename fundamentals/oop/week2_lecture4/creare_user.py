re_persons = [
        {'first': 'Ada', 'last': 'Wong', 'email': 'ada.wong@umbrella.com', 'age': 39, 'password': 'password123'},
        {'first': 'Chris', 'last': 'Redfield', 'email': 'chris.redfield@bssa.org', 'age': 48, 'password': 'password123'},
        {'first': 'Leon', 'last': 'Kennedy', 'email': 'leon_kennedy@usgov.gov', 'age': 46, 'password': 'password123'},
        {'first': 'Piers', 'last': 'Nivans', 'email': 'piers.nivans@bsaa.gov', 'age': 26, 'password': 'password123'},
    ]

class User:
    user_list = []
    user_id_name_list = []
    user_accounts = []
    account_type = 0
    user_id = 0
    #account types
    # 1 = checking
    # 2 = savings
    # 3 = mortgage

    def __init__(self, re_persons):
        self.first_n = re_persons["first"]
        self.last_n = re_persons["last"]
        self.email = re_persons["email"]
        self.password = re_persons["password"]
        self.age = re_persons["age"]
        self.set_user_id()
        User.user_accounts.append(self)
        #creates a list that's indexible
        User.user_list.append(f"{self.first_n} {self.last_n}")
        #creates an object inside a list for each user
        User.user_id_name_list.append({"id":self.user_id, "Name":f'{self.first_n} {self.last_n}'})

    @classmethod
    def set_user_id(cls):
        cls.user_id += 1
        return cls.user_id

    def user_info(self):
        print(f"First Name: {self.first_n}")
        print(f"Last Name: {self.last_n}")
        print(f"Email: {self.email}")
        print(f"Password: {self.password}")
        return self
    
    @classmethod
    def all_info(cls):

        # we use cls to refer to the class
        for account in cls.user_accounts:
            acc = account
            print("")
            print("##################################")
            print(f"###### User: {acc.first_n} ######")
            print("##################################")
            print(f"Age: {acc.age}")
            print(f"Email: {acc.email}")
            print(f"Account ID: {acc.account_id}")
            print(f"Password: {acc.password}")

i = 0
for user in re_persons:
    temp_user = User(user)

    i += 1


chrisredfield = User(re_persons[1])
chrisredfield.user_info().user_info()
User.all_info()


# fetch user list from class
for users in User.user_list:
    print(users)

# fetch user and id objects (dictionary entries) from a class list
for user_idnames in User.user_id_name_list:
    # for key, value in user_idnames.items():
    #     print(f"{key}: {value}")
    print(user_idnames["id"], user_idnames["Name"])