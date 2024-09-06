import os
from PIL import Image
import pillow_heif

# Register HEIF opener
pillow_heif.register_heif_opener()

# Define source and destination folders
source_folder = r'c:\heic'
destination_folder = r'c:\jpg'

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Convert HEIC to JPG
for filename in os.listdir(source_folder):
    if filename.lower().endswith('.heic'):
        heic_path = os.path.join(source_folder, filename)
        jpg_path = os.path.join(destination_folder, f"{os.path.splitext(filename)[0]}.jpg")
        
        # Open HEIC file
        heif_file = pillow_heif.read_heif(heic_path)
        image = Image.frombytes(
            heif_file.mode, 
            heif_file.size, 
            heif_file.data, 
            "raw"
        )
        
        # Save as JPG
        image.save(jpg_path, "JPEG")
        print(f"Converted {filename} to {jpg_path}")
        