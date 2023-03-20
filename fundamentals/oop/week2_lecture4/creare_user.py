re_persons = [
        {'first': 'A', 'last': 'Wong', 'email': 'ada.wong@umbrella.com', 'password': 'password123', 'age': 39},
        {'first': 'Chris', 'last': 'Redfield', 'email': 'chris.redfield@bssa.org', 'password': 'password123', 'age': 48},
        {'first': 'Leon', 'last': 'Kennedy', 'email': 'leon_kennedy@usgov.gov', 'password': 'password123', 'age': 46},
        {'first': 'Piers', 'last': 'Nivans', 'email': 'piers.nivans@bsaa.gov', 'password': 'password123', 'age': 26},
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
            print(f"Account ID: {acc.user_id}")
            print(f"Password: {acc.password}")

    @staticmethod
    def is_valid(first_n,last_n,email,password,age):
        if len(first_n) < 3:
            return False
        if len(last_n) < 3:
            return False
        if len(email) < 10:
            return False
        if len(password) < 3:
            return False
        if age < 18:
            return False
        return True

for user in re_persons:
    # User.is_valid("A","test","somebig@email.com","somebigpass",41)
    if User.is_valid(user["first"], user["last"], user["email"], user["password"], user["age"]):
        temp_user = User(user)
        print("Added user")
    else:
        print("Invalid User")

# DEBUG INFO
# chrisredfield = User(re_persons[1])
# chrisredfield.user_info().user_info()
User.all_info()


# WAYS TO FETCH INFO FROM CONTAINERS
# fetch user list from class list
for users in User.user_list:
    print(users)
# fetch user and id objects (dictionary entries) from a class list
for user_idnames in User.user_id_name_list:
    # for key, value in user_idnames.items():
    #     print(f"{key}: {value}")
    print(user_idnames["id"], user_idnames["Name"])