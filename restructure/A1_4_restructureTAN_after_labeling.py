#coding:utf8
import pandas as pd
import csv
import sqlalchemy
if __name__=="__main__":
    with open("raw_tan.csv","r",encoding="utf8") as tanFile:
        myReader = csv.reader(tanFile)

        tanList=[row for row in myReader]
        
        #delete
        newList=[]
        for i in range(len(tanList)):
            if (i-1)%3!=0:
                newList.append(tanList[i])
        
        #tag
        textList = [" ".join([word for word in newList[i] if len(word)>0]) for i in range(0, len(newList), 2)]
        tagList = ["N" if len("".join(newList[i])) == 0 else "".join(
            newList[i]) for i in range(1, len(newList), 2)]
        keyWordList = ["N" if len("".join(newList[i])) == 0 else " ".join([
            newList[i-1][wordI] for wordI in range(len(newList[i-1])) if len(newList[i][wordI]) > 0]) for i in range(1, len(newList), 2)]
        
        print(textList[0])
        print(tagList[0])
        print(keyWordList[0])
        
        tanDf = pd.DataFrame(list(zip(textList, tagList, keyWordList)), columns=[
                             "text", "tag", "keyword"])
        engine_loacl = sqlalchemy.create_engine(
            'mysql+pymysql://my7012:my7012@39.107.92.174/my7012', echo=False)
        tanDf.to_sql(
            "SentenceClassDf", engine_loacl, index=None)
