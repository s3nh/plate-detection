import torch 
import torch.nn as nn 
import torchvision
import os 



class SSDLoader():
    def __init__(self, model_path='pretrain/mb2-ssd-lite-mp-0_686.pth'):
        self.model_path = model_path
        self.model = self.load_model(self.model_path)
    def __call__(self):
        assert os.path.exists(self.model_path)
        
    def load_model(self):
        model = torch.load(self.model_path)
        return model
    
def main():
    ssd_l = SSDLoader()
    ssd_l    

if __name__ == "__main__":
    main()