from flask_app.config.mysqlconnection import connectToMySQL
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash

class Recipe:
    db = "recipe_share"
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.under = data['under']
        self.description = data['description']
        self.instructions = data['instructions']
        self.posted_by = data['posted_by']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(cls.db).query_db(query)
        recipes = []
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes
    @classmethod
    def add_recipe(cls,data):
        query = """
                INSERT INTO recipes (name,under,description,instructions,posted_by,date_cooked,user_id)
                VALUES (%(name)s,%(under)s,%(description)s,%(instructions)s,%(posted_by)s,%(date_cooked)s,%(user_id)s)
                """
        return connectToMySQL(cls.db).query_db(query,data)
    
    @staticmethod
    def validate_add_recipe(data):
        is_valid = True
        # query = "SELECT * FROM users WHERE email = %(email)s;"
        # results = connectToMySQL(User.db).query_db(query,user)
        # if len(results) >= 1:
        #     flash("Email unavailable. Please use a different email.","register")
        #     is_valid = False
        if len(data['name']) < 3:
            flash("Recipe name must be at least 3 characters","add_recipe")
            is_valid = False
        if len(data['description']) < 1:
            flash("Description cannot be blank","add_recipe")
            is_valid = False
        if len(data['instructions']) < 1:
            flash("Instructions cannot be blank","add_recipe")
            is_valid = False
        # if user['password'] != user['confirm']:
        #     flash("Passwords don't match.","add_recipe")
        #     is_valid = False
        return is_valid