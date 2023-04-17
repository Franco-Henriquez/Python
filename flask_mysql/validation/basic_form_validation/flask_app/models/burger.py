from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
class Burger:
# Other Burger methods up yonder.
# Static methods don't have self or cls passed into the parameters.
# We do need to take in a parameter to represent our burger
    db = "burgers_and_ingredients"
    def __init__( self , data ):
        print("This is the id",data['id'])
        self.id = data['id']
        self.name = data['name']
        self.bun = data['bun']
        self.meat = data['meat']
        self.calories = data['calories']
        self.restaurant_id = data['restaurant_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,burger_data):
        query = """
        INSERT INTO burgers
        (name,bun,meat,calories,restaurant_id) 
        VALUES ( %(name)s,%(bun)s,%(meat)s,%(calories)s,%(restaurant_id)s)
        """
        return connectToMySQL(cls.db).query_db(query,burger_data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM burgers;"
        burgers_from_db = connectToMySQL(cls.db).query_db(query)
        # we must create a list to store the dictionary definitions we're about to retrieve
        burgers = []
        for burger in burgers_from_db:
            # for each burger, grab the data and pass it to the class Burger
            # and then append the recreated object (dictionary method) into the empty burgers list
            burgers.append(cls(burger))
        return burgers

    @staticmethod
    def validate_burger(burger):
        is_valid = True # we assume this is true
        if len(burger['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(burger['bun']) < 3:
            flash("Bun must be at least 3 characters.")
            is_valid = False
        if int(burger['calories']) < 200:
            flash("Calories must be 200 or greater.")
            is_valid = False
        if len(burger['meat']) < 3:
            flash("Bun must be at least 3 characters.")
            is_valid = False
        return is_valid

