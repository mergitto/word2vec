import pandas as pd

col_names = ['c{0:02d}'.format(i) for i in range(10)]
#### ファイルを一意に識別するためのプレフィックス
#     ./hoge.txt
#例 「hoge」の場合、 hoge-wordcloud.csvのようになる
#  以下は出力先のディレクトリを指定すれば良い
#  ※読み込みテキストファイルのパス指定
#  ※csv出力ファイルのパス指定
########################################################
add_file_name = 'zyoho-me'
add_dir_name = './'

#### 読み込みテキストファイルのパス指定
file_path = './%s/%s.txt' %(add_dir_name, add_file_name)

#### csv出力ファイルのパス指定
output_meisi_path = './%s/%s-wordcloud.csv' %(add_dir_name, add_file_name)



# テキストデータの読み込み
words = pd.read_csv(file_path, names=col_names)

# 一般名詞のみ抽出
words_meishi = words[words.c01 == '名詞']
words_mei_ipp = words_meishi
words_mei_ipp = words_mei_ipp[words.c07 != 'の']
words_mei_ipp = words_mei_ipp[words.c07 != '*']
words_mei_ipp = words_mei_ipp[words.c07 != 'こと']


# c07には単語の原形が入っている（名詞については、辞書登録されているもののみ単語が入る？）
words_mei_ipp_sort = words_mei_ipp.groupby('c07')[['c07']].count().sort_values('c07',ascending=False)

# 上位頻出単語1000位までの単語を抽出
print(words_mei_ipp_sort[1:1000]) # 0行目が「*」だったため外している
words_mei_ipp_sort[1:1000].to_csv(output_meisi_path)

