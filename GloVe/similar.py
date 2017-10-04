#####################################################
# 作成したモデルからsimilarワードを抜き出す
# 入力ワードからコサイン類似度の高いワードを取り出す
# コサイン類似度とは、ベクトル空間モデルにおいて、
# 文書同士を比較する際に用いられる類似度計算手法。
# コサイン類似度は、そのまま、ベクトル同士の成す
# 角度の近さを表現するため、三角関数の普通の
# コサインの通り、1に近ければ類似しており、
# 0に近ければ似ていないことになる。
#####################################################
## 使用方法 以下のコマンドを実行する
## python similar.py ./glove2word2vec.pyで作成したモデル名.txt 検索したいワード

from gensim.models.keyedvectors import KeyedVectors
import sys

model = KeyedVectors.load_word2vec_format(sys.argv[1], binary=False)
result = model.most_similar(sys.argv[2])

count = 1
for r in result:
    print(str(count) + "  " + str(r[0]) + "  " + str(r[1]))
    count += 1


