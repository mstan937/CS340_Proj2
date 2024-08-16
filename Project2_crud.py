
#wk7_Project2_CRUD


from pymongo import MongoClient
from pymongo.errors import PyMongoError
from bson.objectid import ObjectId

class CRUD:
    """CRUD operations for a MongoDB collection"""

    def __init__(self, user, password, host, port, db, collection):
        """Initialize the MongoDB client and specify the database and collection"""
        try:
           # self.client = MongoClient(f'mongodb+srv://{user}:{password}@{host}:{port}/{db}')
            self.client = MongoClient(f'mongodb://{user}:{password}@nv-desktop-services.apporto.com:{port}/?directConnection=true&appName=mongosh+1.8.0')

            self.database = self.client[db]
            self.collection = self.database[collection]
            docs = self.collection.find()
        except PyMongoError as e:
            raise Exception(f"Error connecting to MongoDB: {e}")

    def create(self, data):
        """Insert a document into the specified collection"""
        if data:
            try:
                result = self.collection.insert_one(data)
                return result.acknowledged
            except PyMongoError as e:
                print(f"Error inserting document: {e}")
                return False
        else:
            raise ValueError("Data parameter is empty")

    def read(self, query = None):
        """Query for documents from the specified collection"""
        
        try:
                cursor = self.collection.find(query)
                return list(cursor)
        except PyMongoError as e:
                print(f"Error querying documents: {e}")
                return []
      

    def update(self, query, new_values):
        """Update documents in the specified collection"""
        if query and new_values:
            try:
                result = self.collection.update_many(query, {"$set": new_values})
                return result.modified_count
            except PyMongoError as e:
                print(f"Error updating documents: {e}")
                return 0
        else:
            raise ValueError("Query or new values parameter is empty")

    def delete(self, query):
        """Delete documents from the specified collection"""
        if query:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except PyMongoError as e:
                print(f"Error deleting documents: {e}")
                return 0
        else:
            raise ValueError("Query parameter is empty")
