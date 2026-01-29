from core.common import read_file, save_file_with_labels
from core.preprocess import clean_list
from sklearn.cluster import DBSCAN
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

class DBSCANModel():
    def __init__(self):
        pass

    def predict(self, corpus_file, stopwords_file, params, output_dir = None):
        try:
            # Doc du lieu tu file
            original_corpus = read_file(corpus_file)
            stopwords = read_file(stopwords_file)

            cleaned_corpus = clean_list(original_corpus, stopwords)
            vectorizer = TfidfVectorizer(max_df=0.5, min_df=5)
            X = vectorizer.fit_transform(cleaned_corpus)

            model = DBSCAN(
                eps=params.get('eps', 0.3), 
                min_samples=params.get('min_samples', 10))
            labels = model.fit_predict(X)

            if output_dir != None:
                pickle.dump(X, open(output_dir + '/X_test.pkl', 'wb'))
                pickle.dump(labels, open(output_dir + '/labels.pkl', 'wb'))
                save_file_with_labels(original_corpus, labels, output_dir)
        except:
            return False
        return True