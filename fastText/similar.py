from gensim.models.wrappers.fasttext import FastText
import sys

model = FastText.load_fasttext_format('model')
print(model.most_similar(sys.argv[1]))
