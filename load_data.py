
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
    # lines = load_data()
    # print(lines)
    str1 = "Привет я ёжик в тумане"
    print(remove_stopwords(str1))