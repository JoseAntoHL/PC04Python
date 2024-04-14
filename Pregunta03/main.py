import requests
from zipfile import ZipFile
from io import BytesIO
from PIL import Image

url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

response = requests.get(url)
image = Image.open(BytesIO(response.content))

with ZipFile("imagen.zip", "w") as zip_file:
    zip_file.writestr("imagen.jpg", response.content)

print("Imagen descargada y almacenada como imagen.zip")
