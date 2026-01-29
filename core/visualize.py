import pickle
from typing import Counter
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA

def visualize(labels_file, X_test_file, plot_type):
    try:
        # Doc du lieu tu file
        labels = pickle.load(open(labels_file, 'rb'))
        X_test = None if X_test_file == None else pickle.load(open(X_test_file, 'rb'))
        
        if plot_type == 'Histogram':
            elm_count = Counter(labels)
            plt.figure('Histogram')
            plt.bar(elm_count.keys(), elm_count.values())
            plt.title('Distribution of documents across clusters')
            plt.xlabel('Cluster')
            plt.ylabel('Number of documents')
            plt.show()
        elif plot_type == 'PCA':
            pca = PCA(n_components=2)
            X_pca = None
            if isinstance(X_test, list):
                X_pca = pca.fit_transform(X_test)
            else:
                X_pca = pca.fit_transform(X_test.toarray())
            plt.figure('PCA')
            set_clusters = set(labels)
            for cluster in set_clusters:
                plt.scatter(X_pca[labels == cluster, 0], X_pca[labels == cluster, 1], label=str(cluster), s=5)
            plt.title('Distribution of documents across clusters')
            plt.legend(title='Cluster')
            plt.show()
    except:
        return False
    return True