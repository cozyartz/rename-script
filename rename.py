import os
import sys

def rename_images_with_folder_prefix(folder_path):
    # Resolve full path and extract folder name as prefix
    abs_path = os.path.abspath(folder_path)
    prefix = os.path.basename(abs_path)

    if not os.path.isdir(abs_path):
        print(f"Error: '{folder_path}' is not a valid directory.")
        return

    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'}
    files = [f for f in os.listdir(abs_path)
             if os.path.isfile(os.path.join(abs_path, f)) and os.path.splitext(f.lower())[1] in image_extensions]

    files.sort()

    for i, filename in enumerate(files, start=1):
        _, ext = os.path.splitext(filename)
        new_name = f"{prefix}{i:03d}{ext.lower()}"
        src = os.path.join(abs_path, filename)
        dst = os.path.join(abs_path, new_name)
        os.rename(src, dst)
        print(f"Renamed: {filename} -> {new_name}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        folder = "."  # default to current directory
    else:
        folder = sys.argv[1]

    rename_images_with_folder_prefix(folder)
