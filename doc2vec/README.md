### 学習したモデルを使用してある報告書と似たものを探す

ハイパーパラメータについては以下を参照すると良い  
[gensimのdoc2vec](https://radimrehurek.com/gensim/models/doc2vec.html)

```
python similar.py 作成した.model 企業名
```
doc2vec.pyによる学習時のパラメータについて
<例>以下のようなパラメータの場合
```
model = Doc2Vec(documents=training_code, size=300 , window=15, min_count=1, dm=0, iter=400, negative=5, sample=1e-6)
```
size:単語ベクトルの次元  
window:コンテキストの周辺単語の数  
min_count:この値よりも出現回数が小さい単語を破棄する  
dm:dm=1ならdmpv dm=0ならDBOW  
iter:エポックの数  
negative:ネガティブサンプルする単語の数  
sample:単語の出現頻度がこの値よりも大きい場合は無視されるしきい値  

