# Logic to retrieve images from  MongoDB
from db import images_db
import os

def get_image(image_id, collection=os.getenv("MONGO_COLLECTION", "images")):
    """
    Retrieve an image from the database
    """
    image_array = images_db.retrieve_image(image_id, collection)
    return image_array