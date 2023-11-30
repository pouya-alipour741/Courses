#!/usr/bin/env python
# coding: utf-8

# In[696]:


import torch
from torch import nn
from torchvision import models, transforms
from torch.utils.data import Dataset
from torchvision.io import read_image
from torch.utils.data import DataLoader

from pathlib import Path
import pandas as pd
import os


# In[697]:


class Cat_Dog_Dataset(Dataset):
    def __init__(self, csv,root_dir, transform=None):
        self.annonations = pd.read_csv(csv)
        self.transform = transform
        self.root = Path(str(root_dir))
                                       
    def __len__(self):
        return len(self.annonations) 
                                       
    def __getitem__(self, idx):
        img_path = self.root / self.annonations.iloc[idx, 0] 
        img = read_image(str(img_path))
        img = img / 255
        y_label = torch.tensor(int(self.annonations.iloc[idx, 1]))
        
        if self.transform:
            img = self.transform(img)
        return img, y_label

        



