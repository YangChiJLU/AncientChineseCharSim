import torch
from torch.utils.data import Dataset
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from PIL import Image
from PIL import ImageFile
import constants


ImageFile.LOAD_TRUNCATED_IMAGES = True
class JGWDataset(Dataset):
    def __init__(self, df,SIZE = 512,transform=None):
        self.data = df
        self.size = SIZE
        self.transform=transform
        self.loader = transforms.Compose([
            transforms.ToTensor()])

    def __len__(self):
        return len(self.data)
    def __getitem__(self, idx):
        img_name = self.data.loc[idx, 'name']
        img_path = constants.IMAGE_PATH + img_name

        try:
            img = Image.open(img_path)
            img = img.resize((self.size, self.size))
            img = self.loader(img)

            labels = torch.tensor(self.data.loc[idx,'label_number'])


        except:
            print('img_name',img_name)
            idx = 0
            img_name = self.data.loc[idx, 'name']
            img_path = constants.IMAGE_PATH + img_name
            img = Image.open(img_path)
            img = torch.tensor(img.resize((self.size, self.size)))
            img = self.loader(img)

            labels = torch.tensor(self.data.loc[idx, 'label_number'])

        return {'image': img, 'labels': labels}

def datasets(trn_df):

    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=(0.5), std=(0.5))
    ])
    trndataset = JGWDataset(trn_df, SIZE=100,transform = transform)
    num_workers = 0
    trnloader = DataLoader(trndataset, batch_size=64, num_workers=num_workers,shuffle=False,pin_memory=True)#batch=15174
    return trnloader




