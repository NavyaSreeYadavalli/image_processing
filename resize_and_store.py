import pandas as pd
import numpy as np
from skimage.transform import resize
import sqlite3

# Load the CSV file
file_path = 'data/Challenge2.csv'
data = pd.read_csv(file_path)

# Extract the depth column and image data
depth = data['depth']
image_data = data.drop(columns=['depth']).values

# Resize the image width from 200 to 150
original_width = 200
new_width = 150

# Calculate the resizing ratio
ratio = new_width / original_width

# Resize image data
resized_image_data = np.array([resize(image_row.reshape(1, -1), (1, new_width)).flatten() for image_row in image_data])

# Combine depth and resized image data
resized_data = pd.DataFrame(resized_image_data, columns=[f'pixel_{i}' for i in range(new_width)])
resized_data['depth'] = depth

# Save the resized data to a new CSV file
resized_file_path = 'data/resized_image_data.csv'
resized_data.to_csv(resized_file_path, index=False)

# Connect to SQLite database
db_path = 'data/image_data.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create table
table_creation_query = '''
CREATE TABLE IF NOT EXISTS images (
    depth INTEGER PRIMARY KEY,
    ''' + ', '.join([f'pixel_{i} INTEGER' for i in range(new_width)]) + '''
)
'''
cursor.execute(table_creation_query)

# Insert resized image data
resized_data.to_sql('images', conn, if_exists='replace', index=False)

# Commit and close connection
conn.commit()
conn.close()

print("Resized image data stored in the database successfully.")
