from wordcloud import WordCloud
import matplotlib.pyplot as plt
from core.common import read_file
from core.preprocess import clean_list
import os

def draw_word_cloud(cluster_file, stopwords_file, params):
    text_list = None
    if os.path.exists(stopwords_file):
        text_list = clean_list(read_file(cluster_file), read_file(stopwords_file))
    else:
        text_list = read_file(cluster_file)
        
    text = " ".join(text_list)

    word_cloud = WordCloud(
        width=params.get('width', 800),
        height=params.get('height', 400),
        background_color='white',
        max_words=params.get('max_words', 50)
    ).generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()