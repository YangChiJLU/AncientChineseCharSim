import constants
import numpy as np
import xlrd



def get_relatedRadicalPairs(path,ifid2id1=True):
    word_pairdic=[]
    r12r2 = {}
    wb = xlrd.open_workbook(path)
    sh = wb.sheet_by_name('相关部件对')
    for i in range(sh.nrows):
        li = sh.row_values(i)
        id1 = li[0]
        id2 = li[1]
        r12r2[id1 + " " + id2] = ""
        r12r2[id2 + " " + id1] = ""
        word_pairdic.append(id1+" "+id2)
        if ifid2id1:
            word_pairdic.append(id2 + " " + id1)
    return word_pairdic,r12r2


def get_radicalInfor(path):
    id2word={}
    word2id={}
    wb = xlrd.open_workbook(path)
    sh = wb.sheet_by_name('部件表')
    for i in range(sh.nrows):
        if i == 0:
            continue
        li = sh.row_values(i)
        id = li[0].split("_")[1]
        word = li[1]
        id2word[id]=word
        word2id[word]=id

    return id2word,word2id


def get_charRadicalInfor(word_pairdic,word2id,path):
    index2cid = {}
    id2radicalstring = {}
    cid2id = {}
    wb = xlrd.open_workbook(path)
    sh = wb.sheet_by_name('甲骨文-部件对应表')
    ccount=0
    for i in range(sh.nrows):
        if i == 0:
            continue
        if i==constants.SAMPLE_NUM:
            break
        li = sh.row_values(i)
        id = li[0]
        id=id.split("_")[3]+id.split("_")[4]
        pp=li[3]
        if "," in pp:
            pp=pp.split(",")
        else:
            pp=[pp]
        id2radicalstring[id]="".join(pp)

        if id[:-1] not in cid2id.keys():
            cid2id[id[:-1]]=[id]
            index2cid[ccount] = id[:-1]
            ccount=ccount+1
        else:
            cid2id[id[:-1]].append(id)
        for p in pp:
            if p not in word2id.keys():
                continue
            p = word2id[p]
            if (id + " " + p not in word_pairdic) :
                word_pairdic.append(id + " " + p)
            if (p + " " + id not in word_pairdic) :
                word_pairdic.append(p + " " + id)

    return index2cid,cid2id,word_pairdic,id2radicalstring


def get_charRadicalInfor_simple(path):
    index2cid = {}
    cid2id = {}
    index2ccharacter={}
    wb = xlrd.open_workbook(path)
    sh = wb.sheet_by_name('甲骨文-部件对应表')
    ccount=0
    for i in range(sh.nrows):
        if i == 0:
            continue
        if i==constants.SAMPLE_NUM:
            break
        li = sh.row_values(i)
        id = li[0]
        id=id.split("_")[3]+id.split("_")[4]
        cha = li[1]

        if id[:-1] not in cid2id.keys():
            cid2id[id[:-1]]=[id]
            index2cid[ccount] = id[:-1]
            index2ccharacter[ccount] = cha
            ccount=ccount+1
        else:
            cid2id[id[:-1]].append(id)
    return index2cid,cid2id,index2ccharacter


def get_charRadicalInfor_mix(path):
    cid2id={}
    index2cid={}
    index2ccharacter={}
    wb = xlrd.open_workbook(path)
    sh = wb.sheet_by_name('甲骨文-部件对应表')
    ccount=0
    for i in range(sh.nrows):
        if i == 0:
            continue
        li = sh.row_values(i)
        id = li[0]
        id=id.split("_")[3]+id.split("_")[4]
        cha=li[1]
        if id[:-1] not in cid2id.keys():
            cid2id[id[:-1]]=[id]
            index2cid[ccount] = id[:-1]
            index2ccharacter[ccount] = cha
            ccount=ccount+1
        else:
            cid2id[id[:-1]].append(id)
    return cid2id,index2cid,index2ccharacter






def get_charRadicalInfor_Index(path):
    cid2index={}
    wb = xlrd.open_workbook(path)
    sh = wb.sheet_by_name('甲骨文-部件对应表')
    ccount = 0
    for i in range(sh.nrows):
        if i == 0:
            continue
        li = sh.row_values(i)
        id = li[0]
        id = id.split("_")[3]

        if id not in cid2index.keys():
            cid2index[id] = ccount
            ccount = ccount + 1
    return cid2index


def get_SimiCharPairs(path):
    pairlist=[]
    wb = xlrd.open_workbook(path)
    sh = wb.sheet_by_name('相似部件对标注6405')
    for i in range(sh.nrows):
        li = sh.row_values(i)
        id1 = li[0].split("_")[0]
        id2 = li[1].split("_")[0]
        pairlist.append(id1+"_"+id2)
    return pairlist


def get_charpairs(path,num):
    idpairs=[]
    scores=[]
    wb = xlrd.open_workbook(path)
    sh = wb.sheet_by_name('部件对标注5400')
    for i in range(sh.nrows):
        if i==0:
            continue
        if i == num+1:
            break
        li = sh.row_values(i)
        ids = li[0]
        score = li[2]
        idpairs.append(ids)
        scores.append(int(score) * 0.1)
    return idpairs,scores