### GloVeでの分散学習方法
同フォルダ内に、build、eval、分かち書き済みコーパスがあることを確認する

1. `build/vocab_count -min-count 5 -verbose 2 < 分かち書き済みコーパスファイル > vocab.txt`
1. `build/cooccur -memory 4.0 -vocab-file vocab.txt -verbose 2 -window-size 15 <分かち書き済みコーパスファイル> cooccurrence.bin`
1. `build/shuffle -memory 4.0 -verbose 2 < cooccurrence.bin > cooccurrence.shuf.bin`
1. `build/glove -save-file vectors -threads 8 -input-file cooccurrence.shuf.bin -x-max 10 -iter 15 -vector-size 50 -binary 2 -vocab-file vocab.txt -verbose 2`
1. `python glove2word2vec.py vectors.txt > 変換後のファイル.txt`
1. `python similar.py glove2word2vecで変換したモデル.txt 検索したいワード`


6.ではGloVeの出力ベクトルをword2vecで使用できるようにする
7.では類似度を出力する

