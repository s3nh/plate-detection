"""
Image Loader, box preparation
"""
from PIL import Image
import torch.nn as nn 
import torch.nn.functional as F
import numpy as np 
import re 
import os 
import sys 
import cv2
import argparse

def build_args():
    parser = argparser.ArgumentParser()
    parser.add_argument('--image', type = str, help = 'image_file')
    args = parser.parse_args()
    return args

class ImageLoader():
    def __init__(self, image_path ):
        """
        Get Image, box, label name
        """
        self.image_path = image_path
        self.image = self.load_image()
        self.label_path = self.image_path.split('.')[0] + '.txt' 
        print(self.label_path)
        self.label = self.load_label()
        print("Loaded image size {}".format(self.image.shape)) 
    
    def load_label(self):
        assert os.path.exists(self.label_path)
        with open(self.label_path, 'r') as labelfile:
            _label = labelfile.read()
        return _label
        
    def load_image(self):
        assert os.path.exists(self.image_path)
        image = cv2.imread(self.image_path)
        return image 
    
def main():
    iml = ImageLoader(image_path = 'data_files/benchmarks/endtoend/eu/test_062.jpg')
    print(iml.label_path)
    _image = iml.image
    #_image.show()
    #cv2.imshow('image0', _image)
    #cv2.waitKey(0)
    # Name x1 x2 y1 y2
    _label_coords = [el for el in iml.label.split()]
    x, y = int(_label_coords[1]) ,  int(_label_coords[3])
    height =  x - int(_label_coords[2])
    width = y  -  int(_label_coords[4] )
    label = _label_coords[-1]
    _l_plate = _image[ y:(y+height), x:(x+width)]
    _l_plate = Image.fromarray(_l_plate)


    _l_plate.save('_test_lplate.png')
    
    
if __name__ == "__main__":
    main()
        
