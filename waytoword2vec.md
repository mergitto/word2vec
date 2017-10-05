## word2vecの利用方法
テキストから前処理を行い、word2vecを使用するまでの手順まとめ

### 手順
1. テキストを準備する（今回はcsvでやっている例：allAd.csv）
1. テキストの前処理を行う（zenLow.py）
1. 前処理を行ったテキストから記号を削除（vimで次の置換を行う %s/[^ぁ-んァ-ンーa-zａ-ｚA-ZＡ-Ｚ0-9一-龠０-９\-\r]//g）
1. 記号を削除したテキストを分かち書きする（~/Develop/word2vec/wakati.pyを使用）
ワードクラウドを作成する場合はここを実行する。word2vecはここを飛ばす
- ストップワードの除去を行う（~/Develop/word2vec/stopword.pyを使用）
- mecab -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd 分かち書きした.txt -o 返還後の.txt -E "" -F "%m,%H\n"
- 同フォルダのword2meishi.pyを使用して名詞のみを取り出して集計する
- 集計したデータの１行目を"word,count"に変更して、同フォルダのindex.htmlでcsvの部分を変更
1. 分かち書きしたテキストにword2vecで学習する（~/Develop/word2vec/train.py）
1. 学習したモデルを使用して類似度の高い単語を調べる（~/Develop/word2vec/similar.py）


