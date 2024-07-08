# All Mongo DB related stuff

from utils import compress_image
from pymongo import MongoClient
import os
import logger
from bson.objectid import ObjectId
from pydantic import BaseModel
from typing import Optional, Any
from datetime import datetime
from bson import Binary
import numpy as np

class DBModel(BaseModel):
    id: Optional[Any] = None
    created_at: datetime = datetime.now()
    image_contents: Any

class ImageDB:
    def __init__(self, host: str, port: str, db_name: str):
        # Create the MongoDB URI
        mongo_uri = f"mongodb://{host}:{port}/{db_name}"

        # Connect to MongoDB
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]

    def insert_image(self, image_array, image_id, collection='images'):
        """
        Insert a new image to the database
        """
        try:
            # Convert the NumPy array to bytes and wrap in BSON Binary for storage
            image_collection = self.db[collection]
            image_binary = Binary(image_array.tobytes())
            image_collection.insert_one({'_id': image_id, 'image_data': image_binary})
        except Exception as e:
            logger.error(f"Error inserting image: {e}")
    
    # Function to retrieve an image and convert it back to a NumPy array
    def retrieve_image(self, image_id, collection='images'):
        try:
            image_collection = self.db[collection]
            document = image_collection.find_one({'_id': image_id})
            if document:
                # Convert bytes back to NumPy array
                image_array = np.frombuffer(document['image_data'],dtype=np.uint8)
                return image_array
        except Exception as e:
            logger.error(f"Error retrieving image: {e}")
        return None

# MongoDB Connection
def create_db_instance():
    host = os.environ.get("MONGO_HOST", "localhost")
    port = os.environ.get("MONGO_PORT", "27017")
    db_name = os.environ.get("MONGO_DB_NAME", "images")
    mongo_storage = ImageDB(host=host, port=port, db_name=db_name)
    return mongo_storage

images_db = create_db_instance()