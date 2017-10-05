import pandas as pd
import mojimoji

pd.data = pd.read_table("~/Develop/word2vec/sugSample/allAd.csv", header=None)
pd.tmp = []

pd.data = pd.data.dropna()
pd.data[0] = pd.data[0].str.replace("\<.+?\>", "") # <br />を削除する
pd.data[0] = pd.data[0].str.lower() # 小文字化
pd.data[0] = pd.data[0].str.replace("\[.+?\]", "") # [ ] で囲まれた部分は削除する

for data in pd.data[0].iteritems():
    pd.tmp.append(mojimoji.han_to_zen(data[1], digit=False))
pd.datum = pd.DataFrame(pd.tmp)

pd.datum[0] = pd.datum[0].str.replace("ｂｅｓｔ", "ベスト")
pd.datum[0] = pd.datum[0].str.replace("ｓｕｃｃｅｓｓｓｑｉ", "サクセスｓｑｉ")
pd.datum[0] = pd.datum[0].str.replace("ｅｌｓｅ", "ｅｌｓ")
pd.datum[0] = pd.datum[0].str.replace("ｏｐｅｎｅｓ", "エントリーシート")
pd.datum[0] = pd.datum[0].str.replace("ｏｐｅｎ　ｅｓ", "エントリーシート")
pd.datum[0] = pd.datum[0].str.replace("ｏｅｓ", "エントリーシート")
pd.datum[0] = pd.datum[0].str.replace("ｅｓ", "エントリーシート")

pd.datum[0] = pd.datum[0].str.replace("ｓｅ", "システムエンジニア")

pd.datum[0] = pd.datum[0].str.replace("ｇｄ", "グループディスカッション")

pd.datum[0] = pd.datum[0].str.replace("ｈｐ", "ホームページ")

pd.datum[0] = pd.datum[0].str.replace("ｐｒ", "ピーアール")

pd.datum[0] = pd.datum[0].str.replace("[^ぁ-んァ-ンーa-zａ-ｚA-ZＡ-Ｚ0-9一-龠０-９\-\r]", "") # 記号を削除

pd.datum[0].to_csv("~/Develop/word2vec/sugSample/allAd1.csv", index=None)


