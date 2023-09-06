import os

from PIL import Image

from config.logger import setup_logger

logger = setup_logger(__name__)


def crop_image_center(img_path, save_path):
    try:
        image = Image.open(img_path)
        image = image.convert("RGB")

        width, height = image.size
        new_edge_length = min(width, height)

        # If the image is not square, crop it
        if width != height:
            left = (width - new_edge_length) / 2
            top = (height - new_edge_length) / 2
            right = (width + new_edge_length) / 2
            bottom = (height + new_edge_length) / 2

            cropped_image = image.crop((left, top, right, bottom))
            cropped_image.save(save_path, "JPEG")
        else:
            image.save(save_path, "JPEG")

        logger.info("Finished cropping image")

    except Exception as e:
        logger.error(f"An error occurred while cropping image {img_path}: {e}")
        pass


def main(sub_dirs):
    # Loop over all subdirectories
    for subdir in sub_dirs:
        cropped_sub_dir = os.path.join(subdir, "cropped")
        if not os.listdir(subdir):
            logger.error(f"No images: {subdir}")
            continue

        # Process each file in the subdirectory
        logger.info(f"Start cropping: {subdir}")
        files = sorted(os.listdir(subdir))
        if ".DS_Store" in files:
            files.remove(".DS_Store")

        for i, filename in enumerate(files):
            # Full path to the file
            filepath = os.path.join(subdir, filename)
            cropped_file_path = os.path.join(cropped_sub_dir, filename)
            os.makedirs(cropped_sub_dir, exist_ok=True)

            # Crop the image
            crop_image_center(filepath, cropped_file_path)


if __name__ == "__main__":
    # Path to the base directory
    logger.info("Start cropping engine...")
    base_directory = "/Users/treenulbo/Downloads/attheroom"

    logger.info(f"Base directory: {base_directory}")
    sub_directories = [
        os.path.join(base_directory, d)
        for d in os.listdir(base_directory)
        if os.path.isdir(os.path.join(base_directory, d))
    ]

    logger.info(f"Subdirectories: {len(sub_directories)}")
    main(sub_directories)
