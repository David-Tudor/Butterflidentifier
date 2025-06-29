import os
from PIL import Image
import json
import itertools as it
import numpy as np
import json_maker

data_folder_path = "/Users/david/Documents/Swift/Butterflidentifier/Python/leedsbutterfly"
# image_size = (1000, 700)

image_names = os.listdir(data_folder_path + "/imagesOnly")
# image_names = os.listdir(data_folder_path + "/segmentations")


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

mode = "crop" # options: crop, COM


for i, name in enumerate(image_names):
    print(f"Progress: {i}/{len(image_names)}")
    file_code = name[:-4] # [:-4] removes the .png suffix
    image_path = data_folder_path + "/imagesOnly/" + name
    mask_path = data_folder_path + "/segmentations/" + file_code + "_seg0.png" 

    if os.path.isfile(image_path) and os.path.isfile(mask_path):
        with Image.open(image_path) as im:
            with Image.open(mask_path) as mask_im:
                # Get size and check consistent
                width, height = im.size
                if (width, height) != mask_im.size:
                    print("Size mismatch, exiting")
                    break

                data = np.array(im)
                mask_pix = mask_im.load()

                match mode:
                    case "crop":
                        top, bottom, left, right = height+1000, -1, width+1000, -1
                    # case "COM":
                    #     x_avg = 0
                    #     y_avg = 0
                    #     num = 0
                
                for i,j in it.product(range(width), range(height)):
                    mask_col = mask_pix[i,j]
                    if mask_col == 1: # gets the butterfly pixels based on segmentation mask (which has int pix not RGB - maybe B&W?)
                        # data[j,i,:3] = [0,0,0] # makes butterfly black

                        match mode:
                            case "crop":
                                # print("t, b, l, r", top, bottom, left, right)
                                if i > right: right = i
                                elif i < left: left = i
                                if j < top: top = j # top has lower j value
                                elif j > bottom: bottom = j
                            # case "COM":
                            #     x_avg, y_avg, num = x_avg+i, y_avg+j, num+1

                match mode:
                    case "crop":
                        im1 = im.crop((left, top, right, bottom))
                        
                        cwd = os.path.abspath(os.getcwd())
                        im_folder = cwd+'/cropped_im/'
                        if not os.path.exists(im_folder): os.makedirs(im_folder)

                        im1.save(f'{im_folder}{file_code}.png')
                        json_maker.create_json(im_folder) # make after files made.


                    # case "COM":
                    #     x_avg, y_avg = x_avg/num, y_avg/num
                    #     print(x_avg, y_avg)
                    #     im1 = Image.fromarray(data)
                    #     im1.save(f'cropped_im/{file_code}.png')


    else:
        print(f"A file doesn't exist for {image_path} or \n {mask_path}")

    # break
