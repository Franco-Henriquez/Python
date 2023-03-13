class User:

    def __init__(self,first_name,last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        #defaults
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"Points: {self.gold_card_points}")
        print("--------------------------")
        # for user in self:
        #     print(self.user.first_name)
    
    def enroll(self):
        if (self.is_rewards_member):
            print(f"{self.first_name} {self.last_name} is already a member.")
            return False
        elif not (self.is_rewards_member):
            self.is_rewards_member = True
            self.gold_card_points = 200
            print(f"{self.first_name} is now a rewards member with {self.gold_card_points} points")
            return True


    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points = (self.gold_card_points - amount)
            print(f"{self.first_name}'s rewards points decreased by {amount}, total points remaining: {self.gold_card_points}")
        else:
            print(f"{self.first_name} does not have enough points. Total points remaining: {self.gold_card_points}")



#using this as reference to make manual variable,
#to do for later: make a loop that makes a variable using the above class
# re_persons = [
#         {'first': 'Ada', 'last': 'Wong', 'age': 39, 'diseased': False},
#         {'first': 'Chris', 'last': 'Redfield', 'age': 48, 'diseased': False},
#         {'first': 'Leon', 'last': 'Kennedy', 'age': 46},
#         {'first': 'Piers', 'last': 'Nivans', 'age': 26, 'diseased': True},
#     ]

# re_persons = [
#         {'first': 'Ada', 'last': 'Wong', 'email': 'ada.wong@umbrella.com', 'age': 39},
#         {'first': 'Chris', 'last': 'Redfield', 'email': 'chris.redfield@bssa.org', 'age': 48},
#         {'first': 'Leon', 'last': 'Kennedy', 'email': 'leon_kennedy@usgov.gov', 'age': 46},
#         {'first': 'Piers', 'last': 'Nivans', 'email': 'piers.nivans@bsaa.gov', 'age': 26},
#     ]

# user_une = User("Ada", "Wong", "ada.wong@umbrella.com", 39)


# # To Do - Automate user creation in bulk
# for dictionary in re_persons:
#     i=0
#     user_string_build = ""
#     first_n = dictionary["first"]
#     last_n = dictionary["last"]
#     email = dictionary["email"]
#     age = dictionary["age"]

#     # # the below for loop wont work because everything gets converted into a string if it is stored in a var
#     # for key, value in dictionary.items():
#     #     # print(key, value)
#     #     user_string_build += f'"{value}",'
#     values = User(first_n, last_n, email, age)

        
#     # User()
#     # exec('user_' + str(i) + ' = ' + str(i))
#     exec("user_" + str(i) + " = ",values)
#     # manual code before also doesn't work
#     # user_1 = User(first_n, last_n, email, age)
#     # exec(f'user_{str(i)} = {User("Ada", "Wong", "ada.wong@umbrella.com", 39)}')

#     i += 1
# print(user_1.first_name)



user_une = User("Ada", "Wong", "ada.wong@umbrella.com", 39)
user_deux = User("Chris", "Redfield", "chris.redfield@bssa.org", 48)
user_une.is_rewards_member = True

user_une.spend_points(50)
user_deux.enroll()
user_deux.spend_points(80)
user_une.display_info()
user_deux.display_info()





