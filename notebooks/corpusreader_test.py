import nltk
nltk.download('punkt')
import pandas as pd

from nltk.corpus.reader.plaintext import CategorizedPlaintextCorpusReader

print("test")
CAT_PATTERN = r'([\w_\s]+)/.*'
DOC_PATTERN = r'(?!\.)[\w_\s]+/[\w\s\d\-]+\.txt'

corpus = CategorizedPlaintextCorpusReader('/Users/florianlorisch/PycharmProjects/open-discourse-dynamic-topic-model/corpus/raw_corpus', DOC_PATTERN, cat_pattern=CAT_PATTERN)

categories = corpus.categories()
#fileids = corpus.fileids()

print('categories: ',categories)
#print('fileids: ',fileids)
#print(corpus.sents())

#print(corpus.words('month_2/tech_197.txt'))

# TODO: really dive into this and clean up the structure

