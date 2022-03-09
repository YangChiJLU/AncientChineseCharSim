from dataset import *
import torchvision
import torch
import pandas as pd
import numpy as np
import constants

from PIL import Image
device = 'cuda'
model = torchvision.models.resnet18(pretrained=True)
model.conv1 = torch.nn.Conv2d(3, 64, kernel_size=7, stride=2, padding=3, bias=False)
model.fc = torch.nn.Linear(512, constants.CHARACTER_NUM)#2543个字
model.load_state_dict(torch.load(constants.PIC_MODEL_PATH))
print(model)
criterion = torch.nn.CrossEntropyLoss()

class_name = ['NG','OK']
classList = []

train_label_path = constants.PIC_LABEL_PATH
train_df = pd.read_csv(train_label_path)

trnloader = datasets(train_df)

correct = 0
total = 0

for step, batch in enumerate(trnloader):
    train_loss = 0
    inputs = batch['image']
    targets = batch['labels']
    outputs = model(inputs)
    fout = outputs.detach().numpy()
    np.save(constants.IMAGE_EMB_PATH, fout)

