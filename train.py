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
                          sg=1,
                          size=200,
                          min_count=1,
                          window=15,
                          hs=1,
                          negative=0)
model.save(sys.argv[2])
