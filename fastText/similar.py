from gensim.models.wrappers.fasttext import FastText
import sys

model = FastText.load_fasttext_format('model')
result = model.most_similar(sys.argv[1])

count = 1
for r in result:
    print(str(count) + "  " + str(r[0]) + "  " + str(r[1]))
    count += 1
