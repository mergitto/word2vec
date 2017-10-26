import pandas as pd
import mojimoji


df = pd.read_csv("~/Develop/word2vec/doc2vec/allAdCoTY.csv", header=None)

# < >で囲まれた部分を削除する 例：<br />
df[3] = df[3].str.replace("\<.+?\>", "")

# 小文字化
df[3] = df[3].str.lower()

# [ ] で囲まれた部分は削除する 例：[就職活動のポイント ]
df[3] = df[3].str.replace("\[.+?\]", "")


# 半角から全角へ（数字を除く）
pd.tmp = []
for index, data in df[3].iteritems():
    df[3][index]  = mojimoji.han_to_zen(mojimoji.zen_to_han(str(data), kana=False, ascii=False), digit=False)

# 同意義語の表記統一
df[3] = df[3].str.replace("ｂｅｓｔ", "ベスト")
df[3] = df[3].str.replace("ｓｕｃｃｅｓｓｓｑｉ", "サクセスｓｑｉ")
df[3] = df[3].str.replace("ｅｌｓｅ", "ｅｌｓ")
df[3] = df[3].str.replace("ｏｐｅｎｅｓ", "エントリーシート")
df[3] = df[3].str.replace("ｏｐｅｎ　ｅｓ", "エントリーシート")
df[3] = df[3].str.replace("ｏｅｓ", "エントリーシート")
df[3] = df[3].str.replace("ｅｓ", "エントリーシート")
df[3] = df[3].str.replace("ｓｅ", "システムエンジニア")
df[3] = df[3].str.replace("ｇｄ", "グループディスカッション")
df[3] = df[3].str.replace("ｈｐ", "ホームページ")
df[3] = df[3].str.replace("ｐｒ", "ピーアール")

# 記号を削除
df[3] = df[3].str.replace("[^ぁ-んァ-ンーa-zａ-ｚA-ZＡ-Ｚ0-9一-龠０-９\-\r]", "")

dfAdCoTy = pd.DataFrame()
dfAdCoTy[0] = df[1]
dfAdCoTy[1] = df[[0, 2, 3]].apply(lambda x: '{} {} {}'.format(x[0], x[2], x[3]), axis=1)
dfAdCoTy.columns = ['企業名','テキスト']
dfAdCoTy = dfAdCoTy.dropna(subset=['企業名'])

dfAdCoTy.to_csv('~/Develop/word2vec/doc2vec/AllAdviceKai.csv', index=None)

df = df.dropna()
df = df[df[3] != 'ｎａｎ']
dfDropCo = pd.DataFrame()
dfDropCo[0] = df[1]
dfDropCo[1] = df[[0, 2, 3]].apply(lambda x: '{} {} {}'.format(x[0], x[2], x[3]), axis=1)
dfDropCo.columns = ['企業名','テキスト']
dfDropCo = dfDropCo.dropna(subset=['企業名'])

dfDropCo.to_csv('~/Develop/word2vec/doc2vec/AllAdviceKaiDrop.csv', index=None)