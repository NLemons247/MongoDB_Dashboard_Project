from pymongo import MongoClient, ReturnDocument

class AnimalShelter(object):
    
    def __init__(self, user, password):
        # Connection Variables
        self.USER = user
        self.PASS = password
        HOST = "nv-desktop-services.apporto.com"
        PORT = 32127
        DB = "AAC"
        COL = "animals"
        
        # Initialize Connection
        self.client = MongoClient(f'mongodb://{self.USER}:{self.PASS}@{HOST}:{PORT}')
        self.database = self.client[DB]
        self.collection = self.database[COL]
        
    # Create method for the C in CRUD
    def create(self, data):
        if data is not None:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print(f"An error occurred: {e}")
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")
        
    # Read method for the R in CRUD
    def read(self, query):
        if query is not None:
            try:
                cursor = self.collection.find(query)
                results = list(cursor)
                return results
            except Exception as e:
                print(f"An error occurred: {e}")
                return []
        else:
            raise Exception("Query parameter is empty")
            
    # Update method for the U in CRUD
    def update(self, query, update_data):
        if query is not None and update_data is not None:
            try:
                updated_document = self.collection.find_one_and_update(
                    query,
                    {'$set': update_data},
                    return_document=ReturnDocument.AFTER
                )
                return updated_document
            except Exception as e:
                print(f"An error occurred: {e}")
                return None
        else:
            raise Exception("Query and update_data parameters cannot be empty")
    
    # Delete method for the D in CRUD
    def delete(self, query):
        if query is not None:
            try:
                result = self.collection.delete_one(query)
                return result.deleted_count > 0
            except Exception as e:
                print(f"An error occurred: {e}")
                return False
        else:
            raise Exception("Query parameter is empty")
