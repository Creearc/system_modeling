import pandas as pd
import numpy as np


def read_vectors(file):
    data = pd.read_excel(file)

    vectors = dict()
    for i in range(len(data['Название экземпляра'])):
        vectors[data['Название экземпляра'][i]] = [data[j][i] for j in data.columns[1:]]
    return vectors


def set_random_clusters_centers(k, vectors):
    res = []
    keys = list(vectors.keys())
    for i in range(k):
        res.append(vectors[keys[i]])
    return res


def calc_distance(point_1, point_2):
    return np.sqrt(sum([(point_1[i] - point_2[i]) ** 2 for i in range(len(point_1))]))
    

def calc_cluster_center(elements, vectors):
    return [sum([vectors[elements[i]][parameter_ind] for i in range(len(elements))]) / len(elements) for parameter_ind in range(len(vectors[elements[0]]))]

    
def run_clusters(clusters, vectors):
    clusters_elements = [[] for i in range(len(clusters))]
        
    for key in vectors.keys():
        min_d = [-1, 0]
        for cluster_ind in range(len(clusters)):
            d = calc_distance(clusters[cluster_ind], vectors[key])
            if d < min_d[0] or min_d[0] == -1:
                min_d = [d, cluster_ind]
                
        clusters_elements[min_d[1]].append(key)

    return clusters_elements


def train(vectors, k=2, max_iter=10):
    clusters = set_random_clusters_centers(k, vectors)

    for itteration in range(max_iter):
        print(itteration, clusters)

        clusters_elements = run_clusters(clusters, vectors)

        for cluster_ind in range(len(clusters)):
            clusters[cluster_ind] = calc_cluster_center(clusters_elements[cluster_ind], vectors)
            
    return clusters


if __name__ == '__main__':
    vectors = read_vectors('inp_k-means.xls')
    print(vectors)

    k = 2
    clusters = train(vectors, k, max_iter=10)
    
    clusters_elements = run_clusters(clusters, vectors)
    print(clusters_elements)


    k = 3
    clusters = train(vectors, k, max_iter=10)
    
    clusters_elements = run_clusters(clusters, vectors)
    print(clusters_elements)

    vectors = read_vectors('inp_k-means_example.xls')
    print(vectors)

    k = 3
    clusters = train(vectors, k, max_iter=10)
    
    clusters_elements = run_clusters(clusters, vectors)
    print(clusters_elements)

    
