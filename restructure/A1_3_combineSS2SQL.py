#coding:utf8
import pandas as pd
import sqlalchemy
if __name__=="__main__":
    #loading data
    sbiDf=pd.read_csv("sbiDf.csv")
    svonDf=pd.read_csv("svonDf.csv")
    engine_loacl = sqlalchemy.create_engine(
        'mysql+pymysql://my7012:my7012@39.107.92.174/my7012', echo=False)
    oriDf = pd.read_sql(
        "select * from my7012.sentence_new limit 1500;", engine_loacl)
    
    #integrating data (intersection)
    newList=[]
    newDf=pd.DataFrame(pd.merge(sbiDf,svonDf,how="inner",on="text").values,columns=["text","tag1","tag2"])
    newDf.dropna(inplace=True)
                
    #get tag data
    print(newDf["tag1"][708])
    print(newDf["tag2"][708])
    
    newDf["tag"] = pd.Series([" ".join([newDf["tag1"][rowI].split()[tagI]+"-"+newDf["tag2"][rowI].split()[tagI] for tagI in range(
        len(newDf["tag1"][rowI].split()))]) for rowI in range(len(newDf["text"]))])
    
    #save data
    newDf.loc[:,["text","tag"]].to_csv("ssDf.csv",index=None)
    newDf.loc[:, ["text", "tag"]].to_sql(
        "SentenceTagDf", engine_loacl,index=None)
