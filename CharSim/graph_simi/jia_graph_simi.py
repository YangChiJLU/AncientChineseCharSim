import constants
import readInfor
import numpy as np
import gensim



def getcidsimi(cid1,cid2,cfmodel):
    idlist1=cid2id[cid1]
    idlist2 = cid2id[cid2]
    maxsim=-1
    for id1 in idlist1:
        for id2 in idlist2:
            sim = cfmodel.similarity(id1, id2)
            if sim>maxsim:
                maxsim=sim

    return maxsim



def clevelnetworksimi(path):
    cfmodel = gensim.models.KeyedVectors.load_word2vec_format(path, binary=False)
    cpair2LCSsimi_np = np.zeros((constants.CHARACTER_NUM, constants.CHARACTER_NUM))
    idlist=list(range(constants.CHARACTER_NUM))
    for k, id in enumerate(idlist[:-1]):
        for idd in idlist[k + 1:]:
            sim=getcidsimi(index2cid[id],index2cid[idd],cfmodel)
            cpair2LCSsimi_np[id][idd] = sim
            cpair2LCSsimi_np[idd][id] = sim
    return cpair2LCSsimi_np






inforpath=constants.INFOR_PATH

word_pairdic,_=readInfor.get_relatedRadicalPairs(inforpath,ifid2id1=False)
id2word,word2id=readInfor.get_radicalInfor(inforpath)
index2cid,cid2id,word_pairdic,_=readInfor.get_charRadicalInfor(word_pairdic,word2id,inforpath)

#生成network文档
edge_file = open(constants.NET_PATH, 'w')
for pair in word_pairdic:
    edge_file.write(pair + '\n')

#使用OpenNE工具生成embedding文件，character_node2vec.txt
# cd /Users/chiyang/PycharmProjects/ancientCharacterSimi/OpenNE-master/src
# python3 -m openne --method node2vec --input /Users/chiyang/PycharmProjects/ancientCharacterSimi/data/radicalcharacterNet.txt  --output radical_character_node2vec.txt --representation 50


#Graph文字相似矩阵
path=constants.GRAPHSIM_EMB_PATH
cpair2Netsimi_np=clevelnetworksimi(path)
#np.save(constants.GRAPHSIM_MATRIX_PATH, cpair2Netsimi_np)






