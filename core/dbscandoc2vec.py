import pickle
from core.common import read_file, save_file_with_labels
from core.preprocess import clean_list
from gensim.models import Doc2Vec
from gensim.models.doc2vec import TaggedDocument
from sklearn.cluster import DBSCAN

class DBSCANDoc2Vec():
    def __init__(self):
        pass

    def predict(self, corpus_file, stopwords_file, params, output_dir = None):
        try:
            original_corpus = read_file(corpus_file)
            stopwords = read_file(stopwords_file)
            cleaned_corpus = clean_list(original_corpus, stopwords)

            tagged_train_data = []
            for i, _d in enumerate(cleaned_corpus):
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
            
            test_vectors = [d2v_model.infer_vector(doc.words) for doc in tagged_train_data]

            model = DBSCAN(
                eps=params.get('eps', 0.3),
                min_samples=params.get('min_samples', 10)
            )
            labels = model.fit_predict(test_vectors)

            if output_dir != None:
                pickle.dump(labels, open(output_dir + '/labels.pkl', 'wb'))
                pickle.dump(test_vectors, open(output_dir + '/test_vectors.pkl', 'wb'))
                save_file_with_labels(original_corpus, labels, output_dir)
        except:
            return False
        return True