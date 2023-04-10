from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    db = 'dojos_and_ninjas_schema'
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def show_all_dojos(cls):
        query = """
        SELECT * FROM dojos
        """
        dojos = []
        results = connectToMySQL(cls.db).query_db(query)
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def create_dojo(cls,data):
        query = """
        INSERT
        INTO dojos(name,created_at,updated_at)
        VALUES(%(name)s,NOW(),NOW())
        """
        result = connectToMySQL(cls.db).query_db(query,data)
        print(result)
        return result
