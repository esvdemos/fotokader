import os
from PIL import Image


def overlay_mask(input_dir, mask_path, output_dir):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Load the mask image
    mask = Image.open(mask_path).convert("RGBA")

    # Process each image in the input directory
    for filename in reversed(os.listdir(input_dir)):
        if filename.lower().endswith(("png", "jpg", "jpeg")):
            input_image_path = os.path.join(input_dir, filename)
            output_image_path = os.path.join(output_dir, filename)

            # Skip images that already have a corresponding image in the output directory
            if os.path.exists(output_image_path):
                print(f"Skipping {filename}, already exists in the output directory.")
                continue

            # Open the input image
            image = Image.open(input_image_path).convert("RGBA")

            # Resize mask to match the image size
            mask_resized = mask.resize(image.size, Image.LANCZOS)

            # Overlay the mask on the image
            combined = Image.alpha_composite(image, mask_resized)
            combined = combined.convert("RGB")

            # Save the resulting image to the output directory
            combined.save(output_image_path, format="JPEG")
            print(f"Processed {filename}")


if __name__ == "__main__":
    input_dir = "/media/lukas/NIKON D3300/DCIM/100D3300/"
    mask_path = "./kaders/NED-2024.png"
    output_dir = "./gekaderd"

    overlay_mask(input_dir, mask_path, output_dir)
