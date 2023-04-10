# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database


class User:
    DB = "facegram"
    def __init__( self , data ):
        print("This is the id",data['id'])
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        # aka the database name, in this case, facegram
        results = connectToMySQL(cls.DB).query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append( cls(user) )
            # print("User debug from user.py:",users[0].first_name)
        return users
    
    @classmethod
    def add_user(cls, data):
        query = """INSERT INTO users (first_name,last_name,email,password)
    		VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"""
        result = connectToMySQL(cls.DB).query_db(query,data)
        #WHY DOES RESULT RETURN THE ID?
        print("Added User ID:",result)
        return result
            
    @classmethod
    def get_by_id(cls, user_id):
        query = "SELECT * FROM users WHERE id='%(id)s';"
        data = {'id':user_id}
        results = connectToMySQL(cls.DB).query_db(query,data)
        user_info = []
        user_info = cls(results[0])
        return user_info

    @classmethod
    def delete_by_id(cls, user_id):
        query = "DELETE FROM users WHERE id='%(id)s';"
        data = {'id':user_id}
        connectToMySQL(cls.DB).query_db(query,data)
        return

    @classmethod
    def update_by_id(cls, data, user_id):
        query = """UPDATE users 
                SET first_name=%(first_name)s,
                last_name=%(last_name)s,
                email=%(email)s,
                password=%(password)s
                WHERE id=%(id)s;"""
        
        #creating an empty dictionary to save dissected data into
        rebuilt_data = {}

        #take apart the ImmutableDictionary created by request.form
        for key, value in data.items():
            rebuilt_data.update({key: value})
            print("This object:", key,':', value)
        print("This object:", rebuilt_data)





        # we took the dictionary apart so that we could rebuild it
        rebuilt_data.update({'id':str(user_id)})



        
        # and update/add the id in order to pass it via the query_db code below
        results = connectToMySQL(cls.DB).query_db(query,rebuilt_data)
        print("printing results...:",results)
        return results