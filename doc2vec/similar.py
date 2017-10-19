from gensim.models import Doc2Vec
import sys

model = Doc2Vec.load(sys.argv[1])

for i in model.docvecs.most_similar([sys.argv[2]]):
    print(i[0], i[1])
