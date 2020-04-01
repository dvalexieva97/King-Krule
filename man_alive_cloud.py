
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
import numpy as np
from sklearn import preprocessing
from stop_words import get_stop_words
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk

from nltk.stem import LancasterStemmer
lancaster = LancasterStemmer()

stopwords = get_stop_words('en') + ['chorus', 'verse', 'intro', 'outro', 'title', 'song']
#print(stopwords)

def load_and_parse_data():
    data = pd.read_json('man_alive.json', encoding = 'utf-8')
    print(type(data))
    lyrics = data['lyrics']
    songs = data['name']
    #print(data.head())
    return lyrics, songs

lyrics, songs = load_and_parse_data()


vectorizers = [CountVectorizer(), TfidfVectorizer()]

def visualize_data(lyrics):
    for vect in vectorizers:
        lyrics_vec = vect.fit_transform(lyrics)
        words = vect.get_feature_names()
        print(type(lyrics_vec))
        print(type(words))

        stemmed_words = ""
        for word in words:
            stemmed_words += f" {lancaster.stem(word)}"
        #print(words)
        #print(lyrics_vec)
        #return stemmed_words
stemmed_words = visualize_data(lyrics)
        #words = vect.get_feature_names()
        #cloud = WordCloud(stopwords = 'stopwords', background_color = 'black').generate_from_frequencies()

cloud = WordCloud(stopwords = stopwords, background_color = 'black').generate(stemmed_words)
plt.imshow(cloud, cmap = 'plasma', interpolation= 'bilinear')
plt.axis("off")
print(plt.show())
