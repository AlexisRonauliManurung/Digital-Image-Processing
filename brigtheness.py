from PIL import Image

def brighten_image(image_path, output_path, brightness_factor):
    # Open the image
    image = Image.open(image_path)

    # Convert the image to RGB mode
    image = image.convert('RGB')

    # Adjust the brightness of each pixel
    for x in range(image.width):
        for y in range(image.height):
            r, g, b = image.getpixel((x, y))
            
            # Calculate the new pixel values with integer brightness_factor
            new_r = int(r * brightness_factor)
            new_g = int(g * brightness_factor)
            new_b = int(b * brightness_factor)

            # Clamp the new pixel values to the range [0, 255]
            new_r = min(max(new_r, 0), 255)
            new_g = min(max(new_g, 0), 255)
            new_b = min(max(new_b, 0), 255)

            # Set the new pixel value
            image.putpixel((x, y), (new_r, new_g, new_b))

    # Save the brightened image
    image.save(output_path)

# Example usage
image_path = 'nadifah.jpg'
output_path = 'brightened_image.jpg'
brightness_factor = 1.2

brighten_image(image_path, output_path, brightness_factor)


