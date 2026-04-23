from PIL import Image

def get_pixel_colors_from_image(image_path, x1, y1, x2, y2,x3,y3):
    """
    Loads an image from the given path and extracts the RGB color of two specified pixels.

    Args:
        image_path (str): The path to the image file.
        x1 (int): The x-coordinate of the first pixel.
        y1 (int): The y-coordinate of the first pixel.
        x2 (int): The x-coordinate of the second pixel.
        y2 (int): The y-coordinate of the second pixel.

    Returns:
        tuple: A tuple containing two (R, G, B) tuples representing the colors
               of the two pixels, or (None, None) if an error occurs.
    """
    try:
        img = Image.open(image_path)

        pixel_color1 = img.getpixel((x1, y1))
        pixel_color2 = img.getpixel((x2, y2))
        pixel_color3 = img.getpixel((x3, y3))

        print(f"Pixel 1 at ({x1}, {y1}) from {image_path} has color: {pixel_color1}")
        print(f"Pixel 2 at ({x2}, {y2}) from {image_path} has color: {pixel_color2}")
        print(f"Pixel 3 at ({x3}, {y3}) from {image_path} has color: {pixel_color3}")
        return pixel_color1, pixel_color2, pixel_color3

    except FileNotFoundError:
        print(f"Error: The image file '{image_path}' was not found.")
        return None, None, None
    except Exception as e:
        print(f"An error occurred while processing the image: {e}")
        return None, None, None

if __name__ == "__main__":
    # --- Example Usage ---
    # You will need to replace these with the actual coordinates and the
    # correct path to your 'MK Screen.jpg' file.

    # Example coordinates for two pixels
    test_x1, test_y1 = 2413, 1346
    test_x2, test_y2 = 2413, 1346
    x3,y3= 2413, 1346
    # The name of your screenshot file
    image_file = "screenshot.png" # Ensure this file is in the same directory or provide full path

    print(f"Attempting to extract colors from '{image_file}' at coordinates:")
    print(f"  Pixel 1: ({test_x1}, {test_y1})")
    print(f"  Pixel 2: ({test_x2}, {test_y2})\n")
    print(f"  Pixel 3: ({x3}, {y3})\n")

    # Call the function to get the pixel colors
    color1, color2, color3 = get_pixel_colors_from_image(image_file, test_x1, test_y1, test_x2, test_y2,x3,y3)

    if color1 and color2 and color3:
        print("\nSuccessfully extracted pixel colors.")
    else:
        print("\nFailed to extract pixel colors due to an error.")
