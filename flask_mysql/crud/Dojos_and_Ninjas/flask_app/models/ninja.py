from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    db = 'dojos_and_ninjas_schema'
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_by_dojo_id(cls, id):
        query = """
                SELECT * FROM ninjas
                LEFT JOIN dojos
                ON dojos.id = dojo_id
                WHERE dojos.id = '%(id)s';
                """
        data = {'id':id}
        results = connectToMySQL(cls.db).query_db(query,data)
        # created a list to store our dictionary results in
        ninjas_in_dojo = []
        # iterate through the results and save each dictionary entry in a list
        # in our ninjas_in_dojo list
        for ninja in results:
            ninjas_in_dojo.append(cls(ninja))
        return ninjas_in_dojo
    
    @classmethod
    def add_ninja(cls, data):
        query = """INSERT INTO ninjas (first_name,last_name,age,dojo_id)
    		VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);"""
        result = connectToMySQL(cls.db).query_db(query,data)
        #WHY DOES RESULT RETURN THE ID?
        print("Added User ID:",result)
        return result
    
    @classmethod
    def remove_ninja(cls, id):
        query = "DELETE FROM ninjas WHERE id='%(id)s';"
        data = {'id':id}
        result = connectToMySQL(cls.db).query_db(query,data)
        #WHY DOES RESULT RETURN THE ID?
        print("Removed User ID:",result)
        return result
