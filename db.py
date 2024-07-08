# All Mongo DB related stuff
from utils import compress_image
from pymongo import MongoClient
import os
import logger
from bson.objectid import ObjectId
from pydantic import BaseModel
from typing import Optional, Any
import datetime

class DBModel(BaseModel):
    id: Optional[Any] = None
    message_id: Optional[str] = None
    created_at: datetime = datetime.now()
    response: Optional[str] = None

class ImageDB:
    def __init__(self, host: str, port: str, db_name: str):
        # Create the MongoDB URI
        mongo_uri = f"mongodb://{host}:{port}/{db_name}"

        # Connect to MongoDB
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]

    def insert_image(self, collection, image):
        """
        Insert a new image to the database
        """
        try:
            collection = self.db[collection]
            if data.id is None:
                data.id = ObjectId()  # Generate new ObjectId if not provided
            return collection.insert_one(data.dict()).inserted_id
        except Exception as e:
            logger.error(f"Error storing data: {collection} | {e}")
        self.db.images.insert_one(image)
    
    def compress_and_insert_image(self, image):
        """
        Compress an image and insert it to the database
        """
        # Compress the image
        compressed_image = compress_image(image)
        # Insert the compressed image
        self.insert_image(compressed_image)

    def get_image(self, image_id):
        """
        Get an image from the database
        """
        return self.db.images.find_one({'_id': image_id})

    def get_all_images(self):
        """
        Get all images from the database
        """
        return self.db.images.find()
    

# MongoDB Connection
def create_db_instance():
    host = os.environ.get("MONGO_HOST", "localhost")
    port = os.environ.get("MONGO_PORT", "27017")
    db_name = os.environ.get("MONGO_DB_NAME", "compressed_images")
    mongo_storage = ImageDB(host=host, port=port, db_name=db_name)
    return mongo_storage