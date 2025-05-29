# Image Renamer Script

This Python script renames all image files in a specified folder using the folder name as a prefix, followed by a zero-padded number.

## 📦 What It Does

Given a folder (e.g. `JM-images`) containing image files, this script renames all image files in that folder like so:

JM-images001.jpg
JM-images002.png
JM-images003.webp
...

markdown
Copy
Edit

## ✅ Supported Formats

- `.jpg`
- `.jpeg`
- `.png`
- `.gif`
- `.bmp`
- `.webp`

## 🔧 How to Use

1. **Install Python 3** if it’s not already installed.
2. **Download or clone this repo**.
3. **Open a terminal** and navigate to the folder containing `rename.py`.

4. **Edit the script** and change the folder path:

```python
folder = "/full/path/to/your/folder"
Run the script:


python3 rename.py
