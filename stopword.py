import urllib.request


f = urllib.request.urlopen('http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt')
sw = [line.decode('utf-8').strip() for line in f] # 読み込んだurlから文章を読み込み
sw = [ss for ss in sw if not ss==u''] # 空白を削除
f.close()

print(sw)

