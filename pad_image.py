from PIL import Image
import sys


def rescale_and_pad_image(image_path):
    desired_width, desired_height = 800, 600
    
    # Open the image
    with Image.open(image_path) as img:
        # Calculate the scaling factor
        scale_w = desired_width / img.width
        scale_h = desired_height / img.height
        scale_factor = min(scale_w, scale_h)  # Ensure we do not upscale
        
        # Calculate the new size, maintaining aspect ratio
        new_width = int(img.width * scale_factor)
        new_height = int(img.height * scale_factor)
        
        # Rescale the image
        img_rescaled = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        print(img_rescaled.size)
        
        # Create a new image with a white background
        new_img = Image.new("RGB", (desired_width, desired_height), "white")
        
        # Calculate top-left corner coordinates to paste the rescaled image
        paste_x = (desired_width - new_width) // 2
        paste_y = (desired_height - new_height) // 2
        
        # Paste the rescaled image onto the white background
        new_img.paste(img_rescaled, (paste_x, paste_y))
        
        # Save the result
        new_img.save(image_path)
        print(f"Rescaled and padded image saved to {image_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <image_path>")
    else:
        image_path = sys.argv[1]
        rescale_and_pad_image(image_path)
