# Image Processing Project

This project provides a solution for processing and resizing image data from a CSV file, storing the resized image data in a database, and providing an API to request image frames based on specified depth values. Additionally, it applies a custom color map to the generated frames.

## Project Structure

image_processing_project/
├── app.py
├── Dockerfile
├── requirements.txt
├── resize_and_store.py
├── apply_colormap.py
├── data/
│ └── Challenge2 1.csv


## Files Description

- `app.py`: Flask application to provide an API for requesting image frames based on depth values.
- `Dockerfile`: Docker configuration file for containerizing the application.
- `requirements.txt`: Python dependencies required for the project.
- `resize_and_store.py`: Script to read the CSV file, resize the image data, and store it in a SQLite database.
- `apply_colormap.py`: Script to apply a custom color map to the image data.
- `data/Challenge2 1.csv`: Example CSV file containing image data.

## Setup and Usage

### Prerequisites

- Docker
- Python 3.9+

### Steps

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd image_processing_project
   
2. **Install Python dependencies:**

   ```bash
   pip install -r requirements.txt
   
3. **Run the script to resize and store image data:**

   ```bash
   python resize_and_store.py
   
4. **Build the Docker image:**

   ```bash
   docker build -t image-api .

5. **Run the Docker container:**

   ```bash
   docker run -p 5000:5000 image-api

6. **Access the API endpoint to get image frames:**

   ```bash
   http://localhost:5000/get_image_frames?depth_min=0&depth_max=10
   
7. **Applying Custom Color Map**

   ```bash
   python apply_colormap.py
   
**Example Usage**

**Resize and Store Image Data:**

Running the resize_and_store.py script will read the data/Challenge2 1.csv file, resize the image data, and store it in an SQLite database located at data/image_data.db.

**Request Image Frames:**

Start the Flask server by running app.py in a Docker container. You can then request image frames based on depth_min and depth_max values.

**Apply Custom Color Map:**

The apply_colormap.py script demonstrates how to apply a custom color map to the resized image data and display it using Matplotlib.

