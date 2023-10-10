import gensim
import gensim.corpora as corpora
from gensim.corpora import Dictionary
from gensim.models.coherencemodel import CoherenceModel
from gensim.models.ldamodel import LdaModel

from pprint import pprint

import spacy

import pickle
import re
import pyLDAvis
import pyLDAvis.gensim

import matplotlib.pyplot as plt
import pandas as pd

#https://neptune.ai/blog/pyldavis-topic-modelling-exploration-tool-that-every-nlp-data-scientist-should-know

def gen_html(data, p_num_topics = 5, filename = "lda.html"):
    id2word = Dictionary(data)
    # Term Document Frequency
    corpus = [id2word.doc2bow(text) for text in data]
    # print(corpus[:1])
    # Build LDA model
    lda_model = LdaModel(corpus=corpus,
                    id2word=id2word,
                    num_topics=p_num_topics,
                    random_state=0,
                    chunksize=100,
                    alpha='auto',
                    per_word_topics=True)
    # pprint(lda_model.print_topics())
    doc_lda = lda_model[corpus]
    p = pyLDAvis.gensim.prepare(lda_model, corpus, id2word)
    pyLDAvis.save_html(p, 'lda.html')

if __name__ == "__main__":
    data = [['Теги:', 'криптовалютыкриптовалютные', 'биржикриптовалютные', 'кошелькиинвестициифинансы']]
    gen_html(data, filename = "lda.html")