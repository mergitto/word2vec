from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument
import pandas as pd
import MeCab
import mojimoji

df = pd.read_csv("~/Develop/word2vec/doc2vec/allAdvice.csv", header=None)

# < >で囲まれた部分を削除する 例：<br />
df[2] = df[2].str.replace("\<.+?\>", "")

# 小文字化
df[2] = df[2].str.lower()

# [ ] で囲まれた部分は削除する 例：[就職活動のポイント ]
df[2] = df[2].str.replace("\[.+?\]", "")


# 半角から全角へ（数字を除く）
pd.tmp = []
for index, data in df[2].iteritems():
    df[2][index]  = mojimoji.han_to_zen(mojimoji.zen_to_han(str(data), kana=False, ascii=False), digit=False)

# 同意義語の表記統一
df[2] = df[2].str.replace("ｂｅｓｔ", "ベスト")
df[2] = df[2].str.replace("ｓｕｃｃｅｓｓｓｑｉ", "サクセスｓｑｉ")
df[2] = df[2].str.replace("ｅｌｓｅ", "ｅｌｓ")
df[2] = df[2].str.replace("ｏｐｅｎｅｓ", "エントリーシート")
df[2] = df[2].str.replace("ｏｐｅｎ　ｅｓ", "エントリーシート")
df[2] = df[2].str.replace("ｏｅｓ", "エントリーシート")
df[2] = df[2].str.replace("ｅｓ", "エントリーシート")
df[2] = df[2].str.replace("ｓｅ", "システムエンジニア")
df[2] = df[2].str.replace("ｇｄ", "グループディスカッション")
df[2] = df[2].str.replace("ｈｐ", "ホームページ")
df[2] = df[2].str.replace("ｐｒ", "ピーアール")

# 記号を削除
df[2] = df[2].str.replace("[^ぁ-んァ-ンーa-zａ-ｚA-ZＡ-Ｚ0-9一-龠０-９\-\r]", "")


# mecab
me = MeCab.Tagger('-Owakati')
wakachi_list = []
for i, di in enumerate(df[2]):
    try:
        w = me.parse(di)
    except:
        w = di

    if 'list' in str(type(w)):
        print('No.', i, w[:30])
        wakachi_list += [w.split(' ')]
    else:
        print('X No.', i, w)
        wakachi_list += [w]

wakati = pd.DataFrame(wakachi_list, columns=['wakati'])
dfwakati = pd.concat([df, wakati], axis=1)

training_code = []
for i in dfwakati.iterrows():
    training_code.append(TaggedDocument(words=i[1]['wakati'].split(), tags=[str(i[1][1])]))

model = Doc2Vec(documents=training_code, size=100 , window=3, min_count=1, dm=1)

model.save('./doc2vec.model')

for i in model.docvecs.most_similar(['日本電信電話株式会社（NTT持株会社）']):
    print(i[0], i[1])

