from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash # used for validation messages
import re # for regex email validation
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask_app import app
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app) 

class User:
    db = "log_and_reg"
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.updated_at = data["updated_at"]
        self.created_at = data["created_at"]

    @classmethod
    def add_user(cls,data):
        query = """
        INSERT INTO users (first_name, last_name, email, password)
        VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);
        """
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def get_user_by_id(cls,user_id):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,user_id)
        #results would look like this if two dictionaries inside the list:
        #[
        # {first_name: name here
        #  },
        # {first_name: name here
        #  },
        #]
        print("################# get_user_by_id #################\n\n")
        print("Lenght:",len(results))
        print("\n\n##################################")
        if len(results) == 0:
            return None
        else:
            return cls(results[0]) # create a User object from the results list
    @classmethod
    def get_user_by_email(cls,data):
        #because the only dictionary entry is email, we just pass email
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        print("################# get_user_by_id #################\n\n")
        print("Lenght:",len(results))
        print("\n\n##################################")
        if len(results) == 0:
            return None
        else:
            return cls(results[0]) # create a User object from the results list
        
    @staticmethod
    def validate_registration(form_data):
        is_valid = True
        if len(form_data['first_name']) < 3:
            is_valid = False
            flash("First name must be more than 2 characters.","register")
        if len(form_data['last_name']) < 3:
            is_valid = False
            flash("last name must be more than 2 characters.","register")
            
        if not EMAIL_REGEX.match(form_data['email']): 
            flash("Invalid email format.","register")
            is_valid = False
            
        if len(form_data['password']) < 8:
            is_valid = False
            flash("Password must be 8 or more characters.","register")
        if form_data['password'] != form_data['confirm_password']:
            is_valid = False
            flash("Passwords do not match.","register")
        
        #check to see if email is already taken
        #by creating a dictionary out of the form_data containing the email
        email_dict = {
            "email": form_data['email']
        }
        #we then grab the user's info by using their email
        user_found = User.get_user_by_email(email_dict)
        #if nothing comes back, that means the email is open for registration use
        if user_found != None:
            is_valid = False
            flash("Email unavailable. Please use a different email.","register")
        
        return is_valid
    
    @staticmethod
    def validate_login(form_data):
        is_valid = True
        email_dict = {
            "email": form_data['email']
        }
        # if we explicitly are looking for an email, we can do a regex checka additionally
        if not EMAIL_REGEX.match(form_data['email']): 
            flash("Invalid email format.","login")
            is_valid = False
        # but if our login takes both a username or password, then a regex may not be a good validation

        found_user = User.get_user_by_email(email_dict)
        if found_user == None:
            is_valid = False
            flash("Invalid credentials","login")
            return False
        # if someone exists with this email, now check the password
        if not bcrypt.check_password_hash(found_user.password, form_data['password']):
            is_valid = False
            flash("Invalid credentials","login")

        return is_valid

    # EXAMPLE OF VALIDATING STR NUMBERS TO INT NUMBERS
    # this is not currently being used for this project
    @staticmethod
    def number_validation(form_data):
        is_valid = True
        print(form_data)
        # when dealing with numbers inside of a form, it will always return a string
        # we have to do a check using the int() function this converts a number str to number int
        # like this:
        if form_data["size"] == '' or int(form_data["size"]) <= 0:
            is_valid = False
            flash("Size has to be greater than 0")
        
        return is_valid
    
    @staticmethod
    def data_exist_validation(form_data):
        is_valid = True
        print(form_data)
        # in html forms, the <select> and <options> or radio buttons and dropdowns
        # will not appear in our form_data,

        # therefore we need to check if the dictionary entry even exists
        # or if it does exist, check if it's empty
        if "radio_or_select_option" not in form_data or form_data["radio_or_select_option"] == '':
            is_valid = False
            flash("Please select an option from the radio button or dropdown menu")
        
        return is_valid