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
        self.label_path = os.path.split('.')[0] + '.txt' 
        print("Loaded image size {}".format(self.image.shape)) 
    
    def load_label(self):
        assert os.path.exists(self.label_path)
        with open(self.label_path, 'r') as labelfile:
            _label = labelfile.readlines()
        return _label
        
    def load_image(self):
        assert os.path.exists(self.image_path)
        image = cv2.imread(self.image_path)
        return image 
    
def main():
    if __name__ == "__main__":
        iml =  ImageLoader()
    
