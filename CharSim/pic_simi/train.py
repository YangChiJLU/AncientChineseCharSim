import torchvision
from dataset import *
from test import *
import torch
import pandas as pd
import constants
#device = 'cuda'
device=torch.device("cuda" if torch.cuda.is_available() else 'cpu')

train_label_path = constants.PIC_LABEL_PATH
train_df = pd.read_csv(train_label_path)

trnloader= datasets(train_df)
model = torchvision.models.resnet18(pretrained=False)
model.conv1 = torch.nn.Conv2d(3, 64, kernel_size=7, stride=2, padding=3, bias=False)
model.fc = torch.nn.Linear(512,constants.CHARACTER_NUM)#2543个字
model.to(device)


criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001, weight_decay=5e-4)
scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=200)


for epoch in range(100):
    print('Epoch {}/{}'.format(epoch, 99))
    print('-' * 10)
    for param in model.parameters():
        param.requires_grad = True
    model.train()
    train_loss = 0
    correct = 0
    total = 0
    for step, batch in enumerate(trnloader):
        inputs = batch['image']
        targets = batch['labels']
        inputs, targets = inputs.to(device), targets.to(device)
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()
        train_loss += loss.item()
        _, predicted = outputs.max(1)
        total += targets.size(0)
        correct += predicted.eq(targets).sum().item()
    print('Trn Loss: {:.3f} | Trn Acc: {:.3f} ({}/{})'.format(round(train_loss / (step + 1), 4),
                                                          100. * round(correct / total, 4), correct, total))

    output_model_file = '../data/weights/model{}_{}_epoch{}transdata.bin'.format('resnet18', 200,epoch)
    torch.save(model.state_dict(), output_model_file)
    scheduler.step()



