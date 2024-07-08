# Script for reading images, compressing them and storing in a MongoDB database, for later usage
import pandas as pd
from db import images_db
from utils import df_preprocess, compress_image
import cv2

def ingest_image(df):
    """
    Function to convert an image from df chunk to a compressed image and store it in MongoDB.
    """
    # Group the df by image_id
    grouped = df.groupby('image_id')
    
    count = 0
    # Extract all rows for each image_id
    for image_id, group in grouped:
        
        # Get all columns except image_id and frame_num
        image = group.drop(columns=['image_id','frame_num'])
        
        # Convert the df chunk to numpy array
        image_array = image.to_numpy()
        
        # Compress the image
        compressed_image = compress_image(image_array, image_array.shape[0], 150)

        # Insert the compressed image to MongoDB
        status = images_db.insert_image(compressed_image, image_id)

        if status:
            count += 1
        else:
            break
        
    
    return count


def main():
    # Read the CSV file
    df = pd.read_csv('img.csv',header=0)

    # preprocess the dataframe
    df = df_preprocess(df)

    # Ingest the images
    count = ingest_image(df)
    print(f"Total images ingested: {count}")

if __name__ == "__main__":
    main()