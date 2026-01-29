import glob
import os

MODELS = [
    'KMeans (TF-IDF)',
    'KMeans (Word2Vec)',
    'KMeans (Doc2Vec)',
    'DBSCAN (TF-IDF)',
    'DBSCAN (Doc2Vec)'
]

NO_TRAIN_MODELS = [
    'DBSCAN (TF-IDF)',
    'DBSCAN (Doc2Vec)'
]

MODELS_TRAINING_CONFIGS = {
    'KMeans (TF-IDF)': '{\n  "n_clusters": 6,\n  "max_iter": 100,\n  "n_init": 1\n}',
    'KMeans (Word2Vec)': '{\n  "vector_size": 100,\n  "window": 5,\n  "min_count": 1,\n  "workers": 3,\n  ' + \
        '"sg": 1,\n  "alpha": 0.025,\n  "min_alpha": 0.001,\n  "epochs": 10,\n  "start_alpha": 0.002,\n  ' + \
        '"end_alpha": 0.001,\n  "n_cluster": 6,\n  "init": "k-means++",\n  "max_iter": 100\n}',
    'KMeans (Doc2Vec)': '{\n  "vector_size": 100,\n  "window": 5,\n  "min_count": 1,\n  "workers": 3,\n  ' + \
        '"dm": 1,\n  "alpha": 0.025,\n  "min_alpha": 0.001,\n  "epochs": 10,\n  "start_alpha": 0.002,\n  ' + \
        '"end_alpha": -0.016,\n  "n_cluster": 6,\n  "init": "k-means++",\n  "max_iter": 100\n}',
    'DBSCAN (TF-IDF)': '{\n  "eps": 0.3,\n  "min_samples": 10\n}',
    'DBSCAN (Doc2Vec)': '{\n  "vector_size": 100,\n  "window": 5,\n  "min_count": 1,\n  "workers": 3,\n  ' + \
        '"dm": 1,\n  "alpha": 0.025,\n  "min_alpha": 0.001,\n  "epochs": 10,\n  "start_alpha": 0.002,\n  ' + \
        '"end_alpha": -0.016,\n  "eps": 0.3,\n  "min_samples": 10\n}'
}

MODELS_PREDICTING_CONFIGS = {
    'KMeans (TF-IDF)': '{\n  "vectorizer": "",\n  "model_file": ""\n}',
    'KMeans (Word2Vec)': '{\n  "w2v_file": "",\n  "kmeans_file": ""\n}',
    'KMeans (Doc2Vec)': '{\n  "d2v_file": "",\n  "kmeans_file": ""\n}',
    'DBSCAN (TF-IDF)': '{\n  "eps": 1,\n  "min_samples": 4\n}',
    'DBSCAN (Doc2Vec)': '{\n  "vector_size": 100,\n  "window": 5,\n  "min_count": 1,\n  "workers": 3,\n  ' + \
        '"dm": 1,\n  "alpha": 0.025,\n  "min_alpha": 0.001,\n  "epochs": 10,\n  "start_alpha": 0.002,\n  ' + \
        '"end_alpha": -0.016,\n  "eps": 0.3,\n  "min_samples": 10\n}'
}

PLOT_TYPES = ['Histogram', 'PCA']

WORD_CLOUD_DEFAULT_PARAMS = '{\n  "width": 800,\n  "height": 400,\n  "max_words": 50\n}'

SOURCES_CRAWL = [
    'Báo Tuổi trẻ (Tin mới nhất)', 
    'Báo Tuổi trẻ (Thời sự)',
    'Báo Tuổi trẻ (Pháp luật)',
    'Báo Tuổi trẻ (Kinh doanh)',
    'Báo Tuổi trẻ (Xe)',
    'Báo Tuổi trẻ (Du lịch)',
    'Báo Tuổi trẻ (Nhịp sống trẻ)',
    'Báo Tuổi trẻ (Văn hóa)',
    'Báo Tuổi trẻ (Giải trí)',
    'Báo Tuổi trẻ (Giáo dục)',
    'Báo Tuổi trẻ (Nhà đất)',
    'Báo Tuổi trẻ (Sức khỏe)',
    'Báo Tuổi trẻ (Giả thật)',
    'Báo Tuổi trẻ (Bạn đọc làm báo)',
    'Báo Thanh niên (Tin mới nhất)',
    'Báo Thanh niên (Thời sự)',
    'Báo Thanh niên (Sức khỏe)',
    'Báo Thanh niên (Giới trẻ)',
    'Báo Thanh niên (Văn hóa)',
    'Báo Thanh niên (Xe)',
]

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return [line.rstrip() for line in file]
    
def save_file_with_labels(original_corpus, labels, output_dir):
    # Delete old files
    pattern = os.path.join(output_dir, 'cluster_*.txt')
    files_to_delete = glob.glob(pattern)
    for file_path in files_to_delete:
        os.remove(file_path)

    # Write new result files
    for i in range(len(original_corpus)):
        file_path = output_dir + '/cluster_' + str(labels[i]) + '.txt'
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(original_corpus[i] + '\n')