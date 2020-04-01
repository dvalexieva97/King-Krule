from stop_words import get_stop_words
from sklearn.feature_extraction.text import CountVectorizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk

#from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
lancaster = LancasterStemmer()

albums = ['lyrics_6feet', 'lyrics_A New Place 2 Drown', 'lyrics_Ooz', ] #'lyrics_Man Alive']

stopwords = get_stop_words("en") + ['chorus', 'verse', 'intro', 'outro', 'title', 'song']

vectorizer = CountVectorizer()

for album in albums:
    lyrics = open(f'{album}.txt', encoding = 'utf-8').read()
    print(type(lyrics))


    lyrics =  lyrics.split(' ---------------------')
    #lyrics.replace('\n', ' ')

    #lyrics = str(lyrics).split('\n', '\\n', '\n\n')
    print(lyrics)

    data = vectorizer.fit_transform(lyrics) #getting data into BOW form
    words = vectorizer.get_feature_names()

    print("data type is:", type(data))
    print("words type is:", type(words))

    stemmed_words = ""
    for word in words:
        stemmed_words += f" {lancaster.stem(word)}"

    #print(type(lyrics))
    print(words)
    print(stemmed_words)
    #print("done album")

    cloud = WordCloud(stopwords = stopwords, background_color = 'black').generate(stemmed_words)
    #cloud = WordCloud(stopwords = stopwords, background_color = 'black').generate(words)
    plt.imshow(cloud, interpolation= 'bilinear')
    plt.axis("off")
    print(plt.show())
