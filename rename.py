import os

def rename_images_with_prefix(folder_path):
    # Get folder name to use as prefix
    prefix = os.path.basename(os.path.normpath(folder_path))

    # Supported image file extensions
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'}

    # List and filter image files
    files = [f for f in os.listdir(folder_path)
             if os.path.isfile(os.path.join(folder_path, f)) and os.path.splitext(f.lower())[1] in image_extensions]

    # Sort to maintain consistent order
    files.sort()

    # Rename each file with prefix and padded counter
    for i, filename in enumerate(files, start=1):
        _, ext = os.path.splitext(filename)
        new_name = f"{prefix}{i:03d}{ext.lower()}"
        src = os.path.join(folder_path, filename)
        dst = os.path.join(folder_path, new_name)
        os.rename(src, dst)
        print(f"Renamed: {filename} -> {new_name}")

# Example usage
folder = "/full/path/to/JM-images"  # Replace with the path to your folder
rename_images_with_prefix(folder)
