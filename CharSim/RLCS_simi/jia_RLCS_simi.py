import constants
import numpy as np
import readInfor


def getNumofCommonSubstr(str1, str2,relatedRedical=True):
    lstr1 = len(str1)
    lstr2 = len(str2)
    record = [[0 for i in range(lstr2 + 1)] for j in range(lstr1 + 1)]  # 多一位
    maxNum = 0  # 最长匹配长度
    p = 0  # 匹配的起始位

    for i in range(lstr1):
        for j in range(lstr2):
            try:
                r1id = word2id[str1[i]]
                r2id = word2id[str2[j]]
            except:
                continue
            if relatedRedical==True:
                if str1[i] == str2[j]:
                    # 相同则累加
                    record[i + 1][j + 1] = record[i][j] + 1
                    if record[i + 1][j + 1] > maxNum:
                        # 获取最大匹配长度
                        maxNum = record[i + 1][j + 1]
                        # 记录最大匹配长度的终止位置
                        p = i + 1
                elif (r1id + " " + r2id in r12r2.keys()) or (r2id + " " + r1id in r12r2.keys()):
                    record[i + 1][j + 1] = record[i][j] + 0.7
                    if record[i + 1][j + 1] > maxNum:
                        # 获取最大匹配长度
                        maxNum = record[i + 1][j + 1]
                        # 记录最大匹配长度的终止位置
                        p = i + 1
            else:
                if str1[i] == str2[j]:
                    # 相同则累加
                    record[i + 1][j + 1] = record[i][j] + 1
                    if record[i + 1][j + 1] > maxNum:
                        # 获取最大匹配长度
                        maxNum = record[i + 1][j + 1]
                        # 记录最大匹配长度的终止位置
                        p = i + 1

    return maxNum



def getcidsimi(cid1,cid2,relatedRedical=True):
    idlist1=cid2id[cid1]
    idlist2 = cid2id[cid2]
    maxsim=-1
    for id1 in idlist1:
        for id2 in idlist2:
            maxNum = getNumofCommonSubstr(id2radicalstring[id1], id2radicalstring[id2],relatedRedical)
            sim = (2 * maxNum) / (len(id2radicalstring[id1]) + len(id2radicalstring[id2]))
            if sim>maxsim:
                maxsim=sim

    return maxsim



def clevelstringsimi(relatedRedical=True):
    cpair2LCSsimi_np = np.zeros((constants.CHARACTER_NUM, constants.CHARACTER_NUM))
    idlist=list(range(constants.CHARACTER_NUM))
    for k, id in enumerate(idlist[:-1]):
        for idd in idlist[k + 1:]:
            sim=getcidsimi(index2cid[id],index2cid[idd],relatedRedical)
            cpair2LCSsimi_np[id][idd] = sim
            cpair2LCSsimi_np[idd][id] = sim
    return cpair2LCSsimi_np



inforpath=constants.INFOR_PATH
word_pairdic,r12r2=readInfor.get_relatedRadicalPairs(inforpath)
id2word,word2id=readInfor.get_radicalInfor(inforpath)
index2cid,cid2id,word_pairdic,id2radicalstring=readInfor.get_charRadicalInfor(word_pairdic,word2id,inforpath)



#得到文字的LCSSIM相似矩阵
cpair2LCSsimi_np=clevelstringsimi(relatedRedical=True)
#np.save(constants.RLCSSIM_MATRIX_PATH, cpair2LCSsimi_np)

print(cpair2LCSsimi_np.shape)







