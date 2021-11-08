import numpy as np
import pandas as pd

import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel

import spacy
from spacy.lang.de import German
from spacy.lang.de.stop_words import STOP_WORDS

from tqdm import tqdm_notebook as tqdm
from pprint import pprint

##
df = pd.read_csv("/Users/florianlorisch/PycharmProjects/open-discourse-dynamic-topic-model/corpus/speeches/speeches_preprocessed_grüne.csv")
print(df.head())

speeches = df["speechContent"]
print(speeches.head())
##
nlp = German()

# My list of stop words.
stop_list = ["herr","frau","präsident","freunde","freundinnen","kollegen","kolleginnen","[SEP]"]

# Updates spaCy's default stop words list with my additional words.
nlp.Defaults.stop_words.update(stop_list)

# Iterates over the words in the stop words list and resets the "is_stop" flag.
for word in STOP_WORDS:
    lexeme = nlp.vocab[word]
    lexeme.is_stop = True
print(len(STOP_WORDS))
##
parser = German ()
def tokenize(speeches):
    lda_tokens = []
    tokens = parser(speeches)
    for token in tokens:
        if token.orth_.isspace():
            continue
        elif token.like_url:
            lda_tokens.append('URL')
        elif token.orth_.startswith('@'):
            lda_tokens.append('SCREEN_NAME')
        else:
            lda_tokens.append(token.lower_)
    return lda_tokens
##
import nltk
nltk.download('wordnet')

from nltk.corpus import wordnet as wn
def get_lemma(word):
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma
def prepare_text_for_lda(speeches):
    tokens = tokenize(speeches)
    tokens = [token for token in tokens if len(token) > 4]
    tokens = [token for token in tokens if token not in STOP_WORDS]
    tokens = [get_lemma(token) for token in tokens]
    return tokens
##
import random
text_data = []
i=0
for line in speeches:
    tokens = prepare_text_for_lda(line)
    #if random.random() > .99:
    #print(tokens)
    text_data.append(tokens)
    if i % 50 == 0:
      print(str(i)+" Reden")
    i=i+1
##
text_data[1000]
##
import pickle

file = open("/Users/florianlorisch/PycharmProjects/open-discourse-dynamic-topic-model/corpus/speeches/speeches_plain_grüne.pkl",'wb')
pickle.dump(text_data, file)
file.close()
##

from gensim import corpora

dictionary = corpora.Dictionary(text_data)
dictionary.save("/Users/florianlorisch/PycharmProjects/open-discourse-dynamic-topic-model/corpus/speeches/own_dictionary.gensim")
##
corpus = [dictionary.doc2bow(text) for text in text_data]
##
import gensim

NUM_TOPICS = 20

ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = NUM_TOPICS, id2word=dictionary, passes=15)

# unser eigentliches LDA-Model
ldamodel.save("/Users/florianlorisch/PycharmProjects/open-discourse-dynamic-topic-model/models/model1.gensim")

# Ausgabe der entsprechenden gewünschten Topics
topics = ldamodel.print_topics(num_words=10)
for topic in topics:
    print(topic)