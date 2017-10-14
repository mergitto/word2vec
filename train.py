################
# モデル作成
################
## 使用方法
## python train.py 分かち書きしたテキスト.txt 適当なモデル名.model

from gensim.models import word2vec
import logging
import sys

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

sentences = word2vec.LineSentence(sys.argv[1])
model = word2vec.Word2Vec(sentences,
                          sg=1, # skip-gramを使用するかC-BOWを使うか 0 = C-BOW, 1 = skip-gram
                          size=100, # ベクトルの次元数
                          min_count=1, # n回未満出現する単語を削除
                          window=15, # 学習する前後の単語数
                          hs=1, # 学習にソフトマックス関数を使用するか 0 = 使用しない, 1 = 使用する
                          iter=100, # 学習回数
                          negative=0 # ネガティブサンプリングに用いる単語数
                          )
model.save(sys.argv[2])
