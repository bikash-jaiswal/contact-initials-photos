import random

from PIL import Image, ImageDraw, ImageFont
import os

# Directory to store the images
IMAGE_DIR = "contact-initials-photos/"
if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)


def create_initials_image(first_name, last_name=None, image_size=(250, 250), bg_color="white", text_color="black",
                          font_size=100):
    # Extract initials
    initials = first_name[0].upper()
    if last_name:
        initials += last_name[0].upper()

    rainbow_colors = [
        "#DC3545",  # Red
        "#FD7E14",  # Orange
        "#FFC107",  # Yellow
        "#198754",  # Green
        "#0D6EFD",  # Blue
        "#D63384",  # Pink
        "#6F42C1",  # Purple
    ]
    bg_color = random.choice(rainbow_colors)

    # Image size and font settings
    image_size = (250, 250)
    font_size = 60
    font_color = "white"

    # Create a new image with random background color
    img = Image.new('RGB', image_size, color=bg_color)

    # Get a font
    font = ImageFont.truetype("JetBrainsMono-Light.ttf", font_size, encoding="unic")

    # Get a drawing context
    draw = ImageDraw.Draw(img)

    # Calculate text size and position
    text = f"{first_name[0] if first_name else ''}{last_name[0] if last_name else ''}"

    text_x = (image_size[0]) / 3
    text_y = (image_size[1]) / 3

    # Draw the text
    draw.text((text_x, text_y), text, fill=font_color, font=font, align="center")

    return img, initials


def generate_initials_images():
    for char in range(ord('A'), ord('Z') + 1):
        first_name = chr(char)
        image, initials = create_initials_image(first_name)
        file_path = os.path.join(IMAGE_DIR, f"{initials}.png")
        image.save(file_path, format="PNG")

    for char1 in range(ord('A'), ord('Z') + 1):
        for char2 in range(ord('A'), ord('Z') + 1):
            first_name = chr(char1)
            last_name = chr(char2)
            image, initials = create_initials_image(first_name, last_name)
            file_path = os.path.join(IMAGE_DIR, f"{initials}.png")
            image.save(file_path, format="PNG")


generate_initials_images()
