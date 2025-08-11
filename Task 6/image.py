import os
from PIL import Image

input_folder = input("Enter the path to the input folder: ").strip()
output_folder = input("Enter the path to the output folder: ").strip()
width = int(input("Enter new width (pixels): "))
height = int(input("Enter new height (pixels): "))
output_format = input("Enter output format (JPEG/PNG): ").strip().upper()
os.makedirs(output_folder, exist_ok=True)
if not os.path.exists(input_folder):
    print(f"Input folder does not exist: {input_folder}")
    exit()
for filename in os.listdir(input_folder):
    file_path = os.path.join(input_folder, filename)
    if not os.path.isfile(file_path):
        continue
    try:
        with Image.open(file_path) as img:
            img_resized = img.resize((width, height))
            base_name = os.path.splitext(filename)[0]
            output_path = os.path.join(output_folder, f"{base_name}.{output_format.lower()}")
            img_resized.save(output_path, output_format)
            print(f"Resized and saved: {output_path}")
    except Exception as e:
        print(f" Could not process {filename}: {e}")
print("All images processed successfully!")
