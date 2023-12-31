import gensim
import gensim.corpora as corpora
from gensim.corpora import Dictionary
from gensim.models.coherencemodel import CoherenceModel
from gensim.models.ldamodel import LdaModel
import nltk
import pyLDAvis
import pyLDAvis.gensim
# import pandas as pd
import pprint

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
    pprint(lda_model.print_topics())
    doc_lda = lda_model[corpus]
    p = pyLDAvis.gensim.prepare(lda_model, corpus, id2word)
    pyLDAvis.save_html(p, 'lda.html')

def remove_stopwords(str1):
    import nltk
    nltk.download('stopwords')
    from nltk.corpus import stopwords
    russian_stopwords = stopwords.words("russian")
    #https://thecode.media/nlp/
    str2=""
    for word in str1.split(' '):
        if word not in russian_stopwords:
            str2+=" " + word
    return str2


def load_data(filename = "data.txt"):    
    with open(filename, encoding="utf8") as file:
        text = file.read()
    lines = []    
    for line in text.split('\n'):
        line_list = []
        if len(line)>5:
            line = remove_stopwords(line)
            for word in line.split(' '):
                if len(word)>1:
                    line_list.append(word)
            lines.append(line_list)
    return lines

if __name__ == "__main__":
    lines  = load_data()
    gen_html(lines, 5, "lda.html")