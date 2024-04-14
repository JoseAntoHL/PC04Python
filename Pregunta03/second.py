import zipfile

zip_filename = "imagen.zip"

extract_dir = "extracted_image"

with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

print(f"Imagen extraída en el directorio {extract_dir}")
