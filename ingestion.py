# Script for reading images, compressing them and storing in a MongoDB database, for later usage
import pandas as pd
from db import images_db


def ingest_image():
    """
    Function to convert an image from df chunk to a compressed image and store it in MongoDB.
    """
    pass

def main():
    # Read the CSV file
    df = pd.read_csv('img.csv',header=0)

    # Convert the first column to str
    df['depth'] = df['depth'].astype(str)

    # Split the depth column into frame_num and image_id
    
if __name__ == "__main__":
    main()