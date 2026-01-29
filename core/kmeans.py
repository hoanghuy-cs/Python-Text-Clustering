from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from core.common import read_file, save_file_with_labels
from core.preprocess import clean_list
import pickle

class KMeansModel():
    def __init__(self):
        pass

    def train(self, corpus_file, stopwords_file, params, output_dir = None):
        try:
            # Doc du lieu tu file
            corpus = read_file(corpus_file)
            stopwords = read_file(stopwords_file)

            corpus = clean_list(corpus, stopwords)
            vectorizer = TfidfVectorizer(max_df=0.5, min_df=5)
            X_train = vectorizer.fit_transform(corpus)

            n_clusters = params.get('n_clusters', 6)
            max_iter = params.get('max_iter', 100)
            n_init = params.get('n_init', 1)

            kmeans = KMeans(n_clusters=n_clusters, max_iter=max_iter, n_init=n_init)
            kmeans.fit(X_train)

            if output_dir != None:
                pickle.dump(vectorizer, open(output_dir + '/vectorizer.pkl', 'wb'))
                pickle.dump(kmeans, open(output_dir + '/kmeans.pkl', 'wb'))
        except:
            return False
        return True

    def predict(self, corpus_file, stopwords_file, vectorizer_file, model_file, output_dir = None):
        try:
            # Doc du lieu tu file
            original_corpus = read_file(corpus_file)
            stopwords = read_file(stopwords_file)
            vectorizer = pickle.load(open(vectorizer_file, 'rb'))
            model = pickle.load(open(model_file, 'rb'))

            cleaned_corpus = clean_list(original_corpus, stopwords)
            X_test = vectorizer.transform(cleaned_corpus)
            labels = model.predict(X_test)
            
            if output_dir != None:
                pickle.dump(labels, open(output_dir + '/labels.pkl', 'wb'))
                pickle.dump(X_test, open(output_dir + '/X_test.pkl', 'wb'))
                save_file_with_labels(original_corpus, labels, output_dir)
        except:
            return False
        return True