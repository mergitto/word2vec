from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument
import pandas as pd
import MeCab
import mojimoji

df = pd.read_csv("~/Develop/word2vec/doc2vec/allAdviceKaiDrop.csv")

# < >で囲まれた部分を削除する 例：<br />
df['テキスト'] = df['テキスト'].str.replace("\<.+?\>", "")

# 小文字化
df['テキスト'] = df['テキスト'].str.lower()

# [ ] で囲まれた部分は削除する 例：[就職活動のポイント ]
df['テキスト'] = df['テキスト'].str.replace("\[.+?\]", "")


# 半角から全角へ（数字を除く）
pd.tmp = []
for index, data in df['テキスト'].iteritems():
    df['テキスト'][index]  = mojimoji.han_to_zen(mojimoji.zen_to_han(str(data), kana=False, ascii=False), digit=False)

# 同意義語の表記統一
df['テキスト'] = df['テキスト'].str.replace("ｂｅｓｔ", "ベスト")
df['テキスト'] = df['テキスト'].str.replace("ｓｕｃｃｅｓｓｓｑｉ", "サクセスｓｑｉ")
df['テキスト'] = df['テキスト'].str.replace("ｅｌｓｅ", "ｅｌｓ")
df['テキスト'] = df['テキスト'].str.replace("ｏｐｅｎｅｓ", "エントリーシート")
df['テキスト'] = df['テキスト'].str.replace("ｏｐｅｎ　ｅｓ", "エントリーシート")
df['テキスト'] = df['テキスト'].str.replace("ｏｅｓ", "エントリーシート")
df['テキスト'] = df['テキスト'].str.replace("ｅｓ", "エントリーシート")
df['テキスト'] = df['テキスト'].str.replace("ｓｅ", "システムエンジニア")
df['テキスト'] = df['テキスト'].str.replace("ｇｄ", "グループディスカッション")
df['テキスト'] = df['テキスト'].str.replace("ｈｐ", "ホームページ")
df['テキスト'] = df['テキスト'].str.replace("ｐｒ", "ピーアール")

# 記号を削除
df['テキスト'] = df['テキスト'].str.replace("[^ぁ-んァ-ンーa-zａ-ｚA-ZＡ-Ｚ0-9一-龠０-９\-\r]", "")


# mecab
me = MeCab.Tagger('-Owakati -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
wakachi_list = []
for i, di in enumerate(df['テキスト']):
    try:
        w = me.parse(di)
    except:
        w = di

    if 'list' in str(type(w)):
        #print('No.', i, w[:30])
        wakachi_list += [w.split(' ')]
    else:
        #print('X No.', i, w)
        wakachi_list += [w]

wakati = pd.DataFrame(wakachi_list, columns=['wakati'])
dfwakati = pd.concat([df, wakati], axis=1)

training_code = []
for i in dfwakati.iterrows():
    training_code.append(TaggedDocument(words=i[1]['wakati'].split(), tags=[str(i[1]['企業名'])]))

# dm=0 DBOW dm=1 dmpv
model = Doc2Vec(documents=training_code, size=300 , window=15, min_count=1, dm=1, iter=400, negative=5, sample=1e-6)

model.save('~/Develop/word2vec/doc2vec/clensingModel/dmpv-ws-15-epo-400-ns-5.model')

