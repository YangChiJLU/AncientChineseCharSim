import numpy as np
import xlrd
import xlwt
import constants
import readInfor


def similarityRank(num,temp):
    #num：取排名最高的前几名
    max_value = []
    max_index = []
    for k in range(num):
        index_max = np.argmax(temp, axis=1)  # 其中，axis=1表示按行计算
        #print(index_max)
        max = temp[range(temp.shape[0]), index_max]
        #print(max)
        temp[range(temp.shape[0]), index_max] = -1
        max_value.append(max)
        max_index.append(index_max)
    max_index=np.array(max_index)
    max_value = np.array(max_value)
    return max_value.T, max_index.T



def wirte2excel(path,type=123,topk=30):
    cpair2LCSsimi_np = np.load(constants.RLCSSIM_MATRIX_PATH)
    cpair2Netsimi_np = np.load(constants.GRAPHSIM_MATRIX_PATH)
    cpair2Figuresimi_np = np.load(constants.PICSIM_MATRIX_PATH)
    if type==1:
        similarity_np=cpair2LCSsimi_np
    elif type==2:
        similarity_np = cpair2Figuresimi_np
    elif type==3:
        similarity_np = cpair2Netsimi_np
    elif type==12:
        similarity_np = constants.W_RLCS_2 * cpair2LCSsimi_np+constants.W_PIC_2 * cpair2Figuresimi_np
    elif type == 13:
        similarity_np = constants.W_RLCS_1 * cpair2LCSsimi_np + constants.W_GRAPH_1 * cpair2Netsimi_np
    else:
        similarity_np = constants.W_RLCS_3 * cpair2LCSsimi_np+constants.W_GRAPH_3*cpair2Netsimi_np+constants.W_PIC_3 * cpair2Figuresimi_np

    contexts=[]
    max_value, max_index=similarityRank(topk, similarity_np)
    for n in range(len(max_index)):#每一行，每一个字
        infos=[]
        cfid=index2cid[n]
        #cfid=cfid[:-1]+"_"+cfid[-1]
        cf=index2ccharacter[n]
        for k in range(topk):
            index=max_index[n][k]
            mcfid=index2cid[index]
            #mcfid = mcfid[:-1] + "_" + mcfid[-1]
            mcf = index2ccharacter[index]
            mvalue=max_value[n][k]
            mvalue=round(mvalue,4)
            info=str(k+1)+"_"+mcfid+"_"+mcf+"_"+str(mvalue)
            infos.append(info)
        contexts.append([cfid,cf,"; ".join(infos)])


    workbook = xlwt.Workbook(encoding='utf-8')
    sheet = workbook.add_sheet('Sheet1', cell_overwrite_ok=True)

    for i in range(len(contexts)):
        for j in range(3):
            sheet.write(i, j, contexts[i][j])

    workbook.save(path)


inforpath=constants.INFOR_PATH
cid2id,index2cid,index2ccharacter=readInfor.get_charRadicalInfor_mix(inforpath)



#得到每个字的topk相似字
excelpath1 =(constants.RLCSSIM_TOP500_PATH)
excelpath2 =(constants.PICSIM_TOP500_PATH)
excelpath3 =(constants.GLYPHSIM_TOP500_PATH)
excelpath12 =(constants.RLCSSIM_PICSIM_TOP500_PATH)
excelpath13 =(constants.RLCSSIM_GLYPHSIM_TOP500_PATH)
excelpath123 = constants.RLCSSIM_PICSIM_GLYPHSIM_TOP500_PATH

wirte2excel(excelpath1,1,topk=500)
wirte2excel(excelpath2,2,topk=500)
wirte2excel(excelpath12,12,topk=500)
wirte2excel(excelpath3,3,topk=500)
wirte2excel(excelpath13,13,topk=500)
wirte2excel(excelpath123,123,topk=500)






