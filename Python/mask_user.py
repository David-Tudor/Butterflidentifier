import os
from PIL import Image
import json
import itertools as it

data_folder_path = "/Users/david/Documents/Python/butterfly_json/leedsbutterfly"
# image_size = (1000, 700)

# image_names = os.listdir(data_folder_path + "/imagesOnly")
image_names = os.listdir(data_folder_path + "/segmentations")


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

# data = []

for name in image_names:
    name_start = name[:3]
    species = butterfly_names[name_start]
    image_path = data_folder_path + "/imagesOnly/" + name
    mask_path = data_folder_path + "/segmentations/" + name

    # must check files exist


    with Image.open(mask_path) as mask_im:
        width, height = mask_im.size
        pix = mask_im.load()
        dic = {}
        for i,j in it.product(range(width), range(height)):
            col = pix[i,j]
            print(col)
            key = f"{col}"
            if key in dic.keys():
                dic[key] += 1
            else:
                dic[key] = 1
            
        # print(dic)

    break
