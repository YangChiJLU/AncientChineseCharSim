import constants
import numpy as np
import readInfor
import gensim



def getcidsimi(cid1,cid2):
    idlist1=cid2id[cid1]
    idlist2 = cid2id[cid2]
    maxsim=-1
    for id1 in idlist1:
        for id2 in idlist2:
            sim = cfmodel.similarity(id1, id2)
            if sim>maxsim:
                maxsim=sim

    return maxsim


def clevelnetworksimi(filterRadical=True):
    cpair2LCSsimi_np = np.zeros((constants.CHARACTER_NUM, constants.CHARACTER_NUM))
    idlist=list(range(constants.CHARACTER_NUM))
    for k, id in enumerate(idlist[:-1]):
        for idd in idlist[k + 1:]:
            try:
                sim = getcidsimi(index2cid[id], index2cid[idd])
                cpair2LCSsimi_np[id][idd] = sim
                cpair2LCSsimi_np[idd][id] = sim
            except:
                continue
    if filterRadical== True:
        cpair2LCSsimi_np1 = np.load(constants.RLCSSIM_MATRIX_PATH)
        cpair2LCSsimi_np1=np.where(cpair2LCSsimi_np1 > 0, 1, constants.ALPHA)
        cpair2LCSsimi_np=cpair2LCSsimi_np*cpair2LCSsimi_np1
    return cpair2LCSsimi_np



cfmodel = gensim.models.KeyedVectors.load_word2vec_format(constants.GLYPH_EMB_PATH, binary=False)
inforpath=constants.INFOR_PATH
index2cid,cid2id,_=readInfor.get_charRadicalInfor_simple(inforpath)

#得到文字pic相似矩阵
cpair2Figuresimi_np=clevelnetworksimi(filterRadical=True)
#np.save(constants.PICSIM_MATRIX_PATH, cpair2Figuresimi_np)
print(cpair2Figuresimi_np.shape)
















