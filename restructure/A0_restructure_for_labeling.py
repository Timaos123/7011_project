from sqlalchemy import create_engine
import pandas as pd
import numpy as np
import tqdm

if __name__ == "__main__":
    
    engine_loacl = create_engine(
        'mysql+pymysql://my7012:my7012@39.107.92.174/my7012', echo=True)
    mainDf = pd.read_sql(
        "select * from my7012.sentence_new limit 6000;", engine_loacl)
    with tqdm.tqdm(mainDf.values.tolist()) as process:
        for row in process:
            row[-1] = row[-1].split()
            newDf = pd.DataFrame(
                [row[-1], ["" for i in row[-1]], ["" for i in row[-1]]])
            try:
                newDf.to_csv("newData.csv", mode="a", encoding="gbk", index=None, header=None)
            except:
                with open("log.txt","a",encoding="utf8") as logFile:
                    logFile.write(" ".join(row[-1])+"\n")