import pandas as pd
import mojimoji

pd.data = pd.read_table("~/Develop/word2vec/sugSample/allAd.csv", header=None)
pd.tmp = []

# 空白行を削除する
pd.data = pd.data.dropna()

# < >で囲まれた部分を削除する 例：<br />
pd.data[0] = pd.data[0].str.replace("\<.+?\>", "")

# 小文字化
pd.data[0] = pd.data[0].str.lower()

# [ ] で囲まれた部分は削除する 例：[就職活動のポイント ]
pd.data[0] = pd.data[0].str.replace("\[.+?\]", "")

# 半角から全角へ（数字を除く）
for data in pd.data[0].iteritems():
    #pd.tmp.append(mojimoji.han_to_zen(data[1], digit=False))
    pd.tmp.append(mojimoji.han_to_zen(mojimoji.zen_to_han(data[1], kana=False, ascii=False), digit=False)) # 数字だけ半角で、カナとローマ字は全角
pd.datum = pd.DataFrame(pd.tmp)

# 同意義語の表記統一
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

# 記号を削除
pd.datum[0] = pd.datum[0].str.replace("[^ぁ-んァ-ンーa-zａ-ｚA-ZＡ-Ｚ0-9一-龠０-９\-\r]", "")

pd.datum[0].to_csv("~/Develop/word2vec/sugSample/allAd1.csv", index=None)


