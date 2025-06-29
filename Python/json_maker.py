import os
from PIL import Image
import json


def create_json(image_folder_path):
    """
    creates a json in the image folder with label and coord for each image.
    e.g. image_folder_path = "/Users/david/Documents/Swift/Butterflidentifier/Python/leedsbutterfly/images/"
    """

    image_names = os.listdir(image_folder_path)
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
        if name[-3:] != "png": continue
        name_start = name[:3]

        species = butterfly_names[name_start]
        image_path = image_folder_path + name


        with Image.open(image_path) as img:
            width, height = img.size

        
        coords = {"x": 0, "y": 0, "height": height, "width": width}
        annotation = [{"label": species, "coordinates": coords}]

        entry = {"imagefilename": image_path, "annotation": annotation}
        data.append(entry)

    with open(image_folder_path+"mydata.json", "w") as f:
        json.dump(data, f, sort_keys=True, indent=4)
        # print("Created json")



# Example usage 
create_json(image_folder_path = "/Users/david/Documents/Swift/Butterflidentifier/Python/cropped_im/")