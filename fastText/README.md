## fastTextの利用方法
まずはfastTextをインストールして、makeするまでを終わらせた状態だとする
[FacebookのfastTextでFastに単語の分散表現を獲得する](https://qiita.com/icoxfog417/items/42a95b279c0b7ad26589 "FacebookのfastTextでFastに単語の分散表現を獲得する")

おそらくfasttextシェルが作成されているはずなので、これを利用して学習させる
```
./fasttext skipgram -input 分かち書きしたテキスト.txt -output model -dim 100 -ws 15 -epoch 100
```
オプションは色々あるので自分でその場に合わせて調べる
上のコマンドはskip-gramを使用して次元数100、ウィンドウサイズ15、100回繰り返しで学習を行なっている

学習後に任意の単語への類似度を出力する
~/Develop/word2vec/fastText/similar.pyを利用して
```
python similar.py 任意の単語
```
にて類似度順で10個の単語を出力させる
