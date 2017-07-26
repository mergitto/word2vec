# Word2Vecを使用してテキストから意味的に近いワードを表示させる
Python3.6を使用

## ファイル構成
1. wakati.py => テキスト文書を分かち書きする
1. train.py => 分かち書きした文書をWord2Vecによって学習させる
1. similar.py => 学習させたモデルを使用して意味的に近いワードを表示させる

### ファイル使用方法
```wakati.py
python wakati.py 分かち書きさせたい文書.txt 分かち書き後に保存する文書.txt
```

```train.py
python train.py 分かち書きした文書.txt 適当なモデル名.model
```

```similar.py
python similar.py 学習させたモデル.model 適当な検索ワード[-+で連結可能]
```
例：python similar sample.model サンプル

例：python similar sample.model サンプル+食品-カップラーメン

