import urllib.request
import pandas as pd

f = urllib.request.urlopen('http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt')
sw = [line.decode('utf-8').strip() for line in f] # 読み込んだurlから文章を読み込み
sw = [ss for ss in sw if not ss==u''] # 空白を削除
f.close()

wakati = pd.read_table("./department/zyoho-wakati.txt", header=None)
wakatiList = [w.strip() for w in wakati[0]]
wakatiList = [ww for ww in wakatiList if not ww==u'']

pdsw = [];
for w in wakatiList:
    stopRemove = []
    words = w.split()
    for word in words:
        if not word in sw: # ストップワードを含んでいなければそのまま使う
            stopRemove.append(word)
    stopRemove = ','.join(stopRemove).replace(',', ' ') # カンマで区切り、カンマをスペースにすることで分かち書きの体裁を保つ
    pdsw.append(stopRemove)

f = open('./department/zyoho-st.txt', 'w')
for x in pdsw:
    f.write(str(x) + "\n")
f.close()

