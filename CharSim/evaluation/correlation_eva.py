import numpy as np
import constants
import scipy.stats
import readInfor
import pandas as pd




LCSpsimi_np = np.load(constants.RLCSSIM_MATRIX_PATH, allow_pickle=True)
Netsimi_np = np.load(constants.GRAPHSIM_MATRIX_PATH, allow_pickle=True)
Figsimi_np = np.load(constants.PICSIM_MATRIX_PATH, allow_pickle=True)
LCS_Netsimi_np = constants.W_RLCS_1 * LCSpsimi_np+constants.W_GRAPH_1 * Netsimi_np
LCS_Figsimi_np = constants.W_RLCS_2 * LCSpsimi_np+constants.W_PIC_2 * Figsimi_np
LCS_Fig_Netsimi_np = constants.W_RLCS_3 * LCSpsimi_np+constants.W_PIC_3 * Figsimi_np+constants.W_GRAPH_3 * Netsimi_np



def getresult(cid1,cid2,method):

    if method=="RLCS":
        sim = LCSpsimi_np[cid2index[cid1]][cid2index[cid2]]
    elif method=="Pic":
        sim = Figsimi_np[cid2index[cid1]][cid2index[cid2]]
    elif method=="Graph":
        sim = Netsimi_np[cid2index[cid1]][cid2index[cid2]]
    elif method=="RLCS_Pic":
        sim = LCS_Figsimi_np[cid2index[cid1]][cid2index[cid2]]
    elif method=="RLCS_Graph":
        sim = LCS_Netsimi_np[cid2index[cid1]][cid2index[cid2]]
    else:
        sim = LCS_Fig_Netsimi_np[cid2index[cid1]][cid2index[cid2]]
    return round(sim, 4)



def readannotation(num=50):
    idpairs,scores=readInfor.get_charpairs(constants.INFOR_PATH, num)
    return idpairs,scores


path=constants.INFOR_PATH
cid2index=readInfor.get_charRadicalInfor_Index(path)
idpairs,scores=readannotation(num=5400)

sim_scores=[]
for ids in idpairs:
    id1=ids.split("_")[0]
    id2 = ids.split("_")[1]
    sim = getresult(id1, id2, method="RLCS_Pic_Graph")#几种方法RLCS,Pic,Graph, RLCS_Graph, RLCS_Pic, RLCS_Pic_Graph
    sim_scores.append(sim)

print(len(sim_scores))


data = pd.DataFrame({'A':np.array(sim_scores),
                     'B':np.array(scores)})
corr=data.corr('spearman')#'spearman'



print(corr)

corr1=scipy.stats.spearmanr(sim_scores, scores)

print(corr1)




