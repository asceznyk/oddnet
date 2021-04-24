import os
import cv2
import glob
import math
import random
import argparse
import numpy as np

import torch
import torch.nn as nn
import torch.nn.functional as F

from torch.utils.data import Dataset, DataLoader

from torchvision import transforms

from torchvision.transforms import ToTensor

from utils import *
from models import *
from datasets import *
from drawbox import *

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def detect_darknet(options):
    imgsize = 416
    model = Darknet(options.cfg, imgwh=imgsize).to(device)
    model.load_state_dict(torch.load(options.weights))

    print('showing the actual boxes...')
    show_boxes(options.names, options.testdir, imgsize, options.savedir)

    print('the predictions made by the model...')
    predict_boxes(model, options.names, options.testdir, imgsize, 1, options.savedir)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--testdir', type=str, help='path to image folder')
    parser.add_argument('--names', type=str, help='path to names file')
    parser.add_argument('--cfg', type=str, help='a .cfg file for model architecture')
    parser.add_argument('--weights', type=str, help='path to pre-trained weights')
    parser.add_argument('--savedir', type=str, help='folder to save detected images')

    options = parser.parse_args()

    detect_darknet(options)