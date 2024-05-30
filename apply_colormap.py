import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pandas as pd


def apply_custom_colormap(image_data):
    colormap = cm.get_cmap('viridis')
    image_data = image_data / 255.0  # Normalize the data
    colored_image = colormap(image_data)
    return colored_image


# Example usage
if __name__ == '__main__':
    # Load the resized image data
    resized_file_path = 'data/resized_image_data.csv'
    resized_data = pd.read_csv(resized_file_path)

    # Extract the first image row for demonstration
    sample_image_data = resized_data.drop(columns=['depth']).iloc[0].values
    colored_image = apply_custom_colormap(sample_image_data)

    # Display the colored image
    plt.imshow(colored_image.reshape(1, -1, 4))
    plt.title("Sample Colored Image")
    plt.show()
