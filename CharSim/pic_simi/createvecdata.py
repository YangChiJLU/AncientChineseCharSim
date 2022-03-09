import numpy as np
import constants
import csv
import xlrd
characters=np.load(constants.IMAGE_EMB_PATH)
print(characters.shape)



def getcfidlist(path=constants.PIC_LABEL_PATH):
    cfid_list = []
    with open(path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if "_" not in row[2]:
                continue
            id=row[2].split("_")[4]
            cfid_list.append(row[0]+id)
    return cfid_list



cfid_list=getcfidlist()
cfid2vec={}
cfid2num={}

for k,vector in enumerate(characters):#每一个图片向量
    #print(vector)
    if cfid_list[k] not in cfid2vec.keys():
        cfid2vec[cfid_list[k]]=vector
        cfid2num[cfid_list[k]]=1
    else:
        cfid2vec[cfid_list[k]]=cfid2vec[cfid_list[k]]+vector
        cfid2num[cfid_list[k]] = cfid2num[cfid_list[k]]+1
count=0
count2cfid={}

for cfid in cfid2vec.keys():
    cfid2vec[cfid]=cfid2vec[cfid]/cfid2num[cfid]
    cfid2vecli=list(cfid2vec[cfid])
    cfid2vecli = [str(i) for i in cfid2vecli]
    cfid2vecli=" ".join(cfid2vecli)
    count=count+1
    count2cfid[count]=cfid
    # print(str(count)+" "+cfid2vecli+"\n")
    with open(constants.GLYPH_EMB_PATH, "a") as f:
        f.write(str(cfid)+" ")
        f.write(cfid2vecli)
        f.write("\n")



