import lr4 as clustering
import lr4_k_means as model
from pprint import pprint

print('Часть 1')
vecs = clustering.read_vectors('inp_pavel.xls')    
print(vecs)

result = clustering.find_similarities(vecs)
print(result)
pprint(result)

print('----------------------------')
print('Часть 2')
vectors = model.read_vectors('inp_k-means_pavel.xls')
print(vectors)

k = 2
clusters = model.train(vectors, k, max_iter=10)

clusters_elements = model.run_clusters(clusters, vectors)
print(clusters_elements)


k = 3
clusters = model.train(vectors, k, max_iter=10)

clusters_elements = model.run_clusters(clusters, vectors)
print(clusters_elements)

k = 4
clusters = model.train(vectors, k, max_iter=10)

clusters_elements = model.run_clusters(clusters, vectors)
print(clusters_elements)
