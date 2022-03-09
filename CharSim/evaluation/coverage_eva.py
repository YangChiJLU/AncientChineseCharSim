import readInfor
import xlrd
import constants



def readresult(num=20,method="LCS_Fig_Net"):
    pairlist={}
    if method == "RLCS":
        wb = xlrd.open_workbook(constants.RLCSSIM_TOP500_PATH+'x')
    elif method == "Pic":
        wb = xlrd.open_workbook(constants.PICSIM_TOP500_PATH+'x')
    elif method == "Graph":
        wb = xlrd.open_workbook(constants.GLYPHSIM_TOP500_PATH+'x')
    elif method == "RLCS_Graph":
        wb = xlrd.open_workbook(constants.RLCSSIM_GLYPHSIM_TOP500_PATH+'x')
    elif method == "RLCS_Pic":
        wb = xlrd.open_workbook(constants.RLCSSIM_PICSIM_TOP500_PATH+'x')
    else:
        wb = xlrd.open_workbook(constants.RLCSSIM_PICSIM_GLYPHSIM_TOP500_PATH+'x')

    sh = wb.sheet_by_name('Sheet1')
    for i in range(sh.nrows):

        # print(sh.row_values(i))
        li = sh.row_values(i)
        id1 = li[0]
        word = li[2]
        word=word.split("; ")
        for k,ww in enumerate(word):
            if k>num:
                break
            w=ww.split("_")[1]
            v = ww.split("_")[3]
            wordstr=str(id1)+"_"+w
            wordstr1 =  w+ "_" + str(id1)
            if (wordstr not in pairlist.keys())and(float(v)>0):
                pairlist[wordstr]=1
    return pairlist


def getresults(path,num=5,method="RLCS_Pic_Graph"):
    pairlist = readInfor.get_SimiCharPairs(path)
    resultpairlist = readresult(num, method)
    count = 0
    for wstr in pairlist:
        if (wstr in resultpairlist.keys()):
            count = count + 1
    return len(pairlist),count,count / len(pairlist)



path=constants.INFOR_PATH
topk=5#取前k

allcount1,count1,rate1=getresults(path,num=topk,method="RLCS")
allcount3,count3,rate3=getresults(path,num=topk,method="Pic")
allcount4,count4,rate4=getresults(path,num=topk,method="Graph")
allcount5,count5,rate5=getresults(path,num=topk,method="RLCS_Pic")
allcount6,count6,rate6=getresults(path,num=topk,method="RLCS_Graph")
allcount7,count7,rate7=getresults(path,num=topk,method="RLCS_Graph_Pic")




print("RLCS")
print(rate1)

print("Pic")
print(rate3)

print("Graph")
print(rate4)

print("RLCS_Pic")
print(rate5)

print("RLCS_Graph")
print(rate6)

print("RLCS_Graph_Pic")
print(rate7)

