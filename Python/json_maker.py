import os
from PIL import Image
import json

data_folder_path = "/Users/david/Documents/Python/butterfly_json/leedsbutterfly"
# image_size = (1000, 700)

image_names = os.listdir(data_folder_path + "/images")
butterfly_names = {
"001": "Danaus plexippus",
"002": "Heliconius charitonius",
"003": "Heliconius erato",
"004": "Junonia coenia",
"005": "Lycaena phlaeas",
"006": "Nymphalis antiopa",
"007": "Papilio cresphontes",
"008": "Pieris rapae",
"009": "Vanessa atalanta",
"010": "Vanessa cardui",
}

data = []

for name in image_names:
    name_start = name[:3]
    species = butterfly_names[name_start]
    image_path = data_folder_path + "/images/" + name


    with Image.open(image_path) as img:
        width, height = img.size

    
    coords = {"x": 0, "y": 0, "height": height, "width": width}
    annotation = [{"label": species, "coordinates": coords}]

    entry = {"imagefilename": image_path, "annotation": annotation}
    data.append(entry)

for entry in data:
    print(entry)

with open("mydata.json", "w") as f:
	json.dump(data, f)