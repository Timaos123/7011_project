#coding:utf8
import csv
import pandas as pd
if __name__=="__main__":
    with open("raw_svon.csv","r",encoding="utf8") as svonFile:
        myReader = csv.reader(svonFile)
        
        #删除空行
        i=1
        newSVONLabelList=[]
        for line in myReader:
            if i%3!=0:
                newSVONLabelList.append(line)
            i+=1
        
        #构建textList和tagList
        textList=[]
        tagList = []
        i = 1
        for line in newSVONLabelList:
            if i%2==0:
                tagList.append([tagItem.strip() if len(tagItem)>0 else "N" if tagItem!="of" else "O" for tagItem in line])
            else:
                textList.append(line)
            i+=1
        print(len(tagList))
        print(len(tagList))
        #删除空tag
        tagList = [tagList[rowI][:textList[rowI].index("")] \
                    if "" in textList[rowI] \
                        else tagList[rowI]
                    for rowI in range(len(tagList))]
        textList = [[wordItem for wordItem in row if len(
            wordItem) > 0] for row in textList]
        
        dfList = [[" ".join(textList[i]), " ".join(tagList[i])]
                  for i in range(min(len(textList), len(tagList)))]
        
        svonDf=pd.DataFrame(dfList,columns=["text","tag"])
        svonDf.to_csv("svonDf.csv",index=None)
