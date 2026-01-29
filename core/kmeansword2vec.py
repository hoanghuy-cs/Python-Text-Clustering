import pickle
import numpy as np
from sklearn.cluster import KMeans
from core.common import read_file, save_file_with_labels
from core.preprocess import clean_list
from gensim.models import Word2Vec

class KMeansWord2Vec():
    def __init__(self):
        pass

    def train(self, corpus_file, stopwords_file, params, output_dir=None):
        try:
            # Đọc dữ liệu từ file
            corpus = clean_list(read_file(corpus_file), read_file(stopwords_file))

            # Tách các câu thành danh sách từ
            sentences = [sentence.split() for sentence in corpus]

            # Huấn luyện mô hình Word2Vec
            w2v_model = Word2Vec(
                sentences=sentences,
                vector_size=params.get('vector_size', 100),
                window=params.get('window', 5),
                min_count=params.get('min_count', 1),
                workers=params.get('workers', 3),
                sg=params.get('sg', 1),
                alpha=params.get('alpha', 0.025),
                min_alpha=params.get('min_alpha', 0.001)
            )
            
            w2v_model.train(
                sentences,
                total_examples=w2v_model.corpus_total_words,
                epochs=params.get('epochs', 10),
                start_alpha=params.get('start_alpha', 0.002),
                end_alpha=params.get('end_alpha', 0.001)
            )
            
            # Tạo vector biểu diễn cho mỗi văn bản bằng cách lấy trung bình các vector từ
            document_vectors = []
            for sentence in sentences:
                word_vectors = [w2v_model.wv[word] for word in sentence if word in w2v_model.wv]
                if word_vectors:
                    document_vector = np.mean(word_vectors, axis=0)
                    document_vectors.append(document_vector)

            # Gom cụm bằng KMeans
            kmeans = KMeans(
                n_clusters=params.get('n_cluster', 6),
                init=params.get('init', 'k-means++'),
                max_iter=params.get('max_iter', 100)
            )
            kmeans.fit(document_vectors)

            # Lưu mô hình nếu output_dir được cung cấp
            if output_dir is not None:
                with open(output_dir + '/w2v.pkl', 'wb') as w2v_file:
                    pickle.dump(w2v_model, w2v_file)
                with open(output_dir + '/kmeans.pkl', 'wb') as kmeans_file:
                    pickle.dump(kmeans, kmeans_file)
                    
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
        
        return True
    
    def predict(self, corpus_file, stopwords_file, vectorizer_file, model_file, output_dir=None):
        try:
            # Doc du lieu tu file
            original_corpus = read_file(corpus_file)
            cleaned_corpus = clean_list(original_corpus, read_file(stopwords_file))
            w2v = pickle.load(open(vectorizer_file, 'rb'))
            model = pickle.load(open(model_file, 'rb'))

            # Chuyển văn bản thành vector sử dụng word2vec
            test_vectors = []
            for document in cleaned_corpus:
                words = document.split()
                word_vectors = [w2v.wv[word] for word in words if word in w2v.wv]
                if word_vectors:
                    document_vector = np.mean(word_vectors, axis=0)
                else:
                    document_vector = np.zeros(w2v.vector_size)
                test_vectors.append(document_vector)
            
            # Dự đoán nhãn của cụm
            labels = model.predict(test_vectors)

            if output_dir != None:
                pickle.dump(labels, open(output_dir + '/labels.pkl', 'wb'))
                pickle.dump(test_vectors, open(output_dir + '/test_vectors.pkl', 'wb'))
                save_file_with_labels(original_corpus, labels, output_dir)
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
        return True