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
## python similar.py 作成したモデル名.model 検索したいワード(人生)

from gensim.models import word2vec
import logging
import sys

model   = word2vec.Word2Vec.load(sys.argv[1])

def neighbor_word(posi, nega=[], n=10):
    count = 1
    print('positiveWord',posi)
    print('negativeWord',nega)
    result = model.most_similar(positive = posi, negative = nega, topn = n)
    for r in result:
        print(str(count)+" "+str(r[0])+" "+str(r[1]))
        count += 1

def calc(equation):
    if "+" in equation or "-" in equation:
        posi,nega = [],[]
        positives = equation.split("+")
        for positive in positives:
            negatives = positive.split("-")
            posi.append(negatives[0])
            nega = nega + negatives[1:]
        neighbor_word(posi = posi, nega = nega)
    else:
        neighbor_word([equation])


if __name__=="__main__":
    equation = sys.argv[2]
    calc(equation)
