import pandas as pd
import mojimoji

pd.data = pd.read_table('~/Develop/word2vec/sample.txt', header=None)

pd.data[0] = pd.data[0].str.replace("<br />", "")
pd.data[0] = pd.data[0].str.replace("\[就職活動のポイント,合格の決め手]", "")
pd.data[0] = pd.data[0].str.replace("\[どのような勉強、準備をしたか]", "", )
pd.data[0] = pd.data[0].str.replace("\[どのような勉強・準備をしたか]", "", )
pd.data[0] = pd.data[0].str.replace("どのような勉強や準備をしたか", "", )
pd.data[0] = pd.data[0].str.replace("就職活動のポイント", "")
pd.data[0] = pd.data[0].str.replace("合格の決め手", "")
pd.data[0] = pd.data[0].str.lower()

pd.data.to_csv('~/Develop/word2vec/sample1.csv', index=None)


