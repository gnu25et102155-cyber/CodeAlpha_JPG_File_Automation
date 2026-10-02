import os
import shutil

# Folder containing the files
source_folder = "."

# Folder where JPG files will be moved
destination_folder = "JPG_Files"

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.mkdir(destination_folder)

# Count moved files
count = 0

# Check all files in the source folder
for filename in os.listdir(source_folder):

    # Check whether the file is a JPG file
    if filename.lower().endswith(".jpg"):

        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)

        # Move the JPG file
        shutil.move(source_path, destination_path)

        print(f"Moved: {filename}")
        count += 1

print("\nAutomation completed!")
print(f"Total JPG files moved: {count}")