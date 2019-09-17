import torch 
import torch.nn as nn 
import torchvision
import os 
import cv2
import sys

def video_capture(file= None, camera = True):
    if camera:
        cap = cv2.VideoCapture(0)
        cap.set(3, 1920)
        cap.set(4, 1080)
    else:
        assert os.path.exists(file)
        cap = cv2.VideoCapture(file)
class SSDLoader():
    def __init__(self, model_path='pretrain/mb2-ssd-lite-mp-0_686.pth'):
        self.model_path = model_path
        self.model = self.load_model()
    def __call__(self):
        assert os.path.exists(self.model_path)
        
    def load_model(self):
        model = torch.load(self.model_path)
        return model
    
def main():
    ssd_l = SSDLoader()
    print(ssd_l)    

if __name__ == "__main__":
    main()
    