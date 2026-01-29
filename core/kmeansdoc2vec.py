import pickle
from sklearn.cluster import KMeans
from core.common import read_file, save_file_with_labels
from core.preprocess import clean_list
from gensim.models import Doc2Vec
from gensim.models.doc2vec import TaggedDocument

class KMeansDoc2Vec():
    def __init__(self):
        pass

    def train(self, corpus_file, stopwords_file, params, output_dir = None):
        try:
            # Doc du lieu tu file
            corpus = clean_list(read_file(corpus_file), read_file(stopwords_file))

            tagged_train_data = []
            for i, _d in enumerate(corpus):
                tagged_train_data.append(TaggedDocument(words=_d.split(), tags=[str(i)]))

            d2v_model = Doc2Vec(
                vector_size=params.get('vector_size', 100), 
                window=params.get('window', 5),
                min_count=params.get('min_count', 1),
                workers=params.get('workers', 3), 
                dm=params.get('dm', 1),
                alpha=params.get('alpha', 0.025), 
                min_alpha=params.get('min_alpha', 0.001))
            
            d2v_model.build_vocab(tagged_train_data)
            
            d2v_model.train(
                tagged_train_data,
                total_examples=d2v_model.corpus_count,
                epochs=params.get('epochs', 10),
                start_alpha=params.get('start_alpha', 0.002),
                end_alpha=params.get('end_alpha', -0.016))
            
            train_vectors = [d2v_model.infer_vector(doc.words) for doc in tagged_train_data]
            kmeans = KMeans(
                n_clusters=params.get('n_cluster', 6),
                init=params.get('init', 'k-means++'),
                max_iter=params.get('max_iter', 100))
            kmeans.fit(train_vectors)

            if output_dir != None:
                pickle.dump(d2v_model, open(output_dir + '/d2v.pkl', 'wb'))
                pickle.dump(kmeans, open(output_dir + '/kmeans.pkl', 'wb'))
        except:
            return False
        return True

    def predict(self, corpus_file, stopwords_file, vectorizer_file, model_file, output_dir = None):
        try:
            # Doc du lieu tu file
            original_corpus = read_file(corpus_file)
            cleaned_corpus = clean_list(original_corpus, read_file(stopwords_file))
            d2v = pickle.load(open(vectorizer_file, 'rb'))
            model = pickle.load(open(model_file, 'rb'))

            test_vectors = [d2v.infer_vector(doc.split()) for doc in cleaned_corpus]
            labels = model.predict(test_vectors)

            if output_dir != None:
                pickle.dump(labels, open(output_dir + '/labels.pkl', 'wb'))
                pickle.dump(test_vectors, open(output_dir + '/test_vectors.pkl', 'wb'))
                save_file_with_labels(original_corpus, labels, output_dir)
        except:
            return False
        return True