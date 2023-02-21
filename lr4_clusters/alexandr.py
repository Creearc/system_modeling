import lr4 as model
import pprint

print('Часть 1')
vecs = model.read_vectors('inp_alexandr.xls')    
print(vecs)

result = model.find_similarities(vecs)
print(result)
pprint.pprint(result)


import lr4_k_means as model
print('----------------------------')
print('Часть 2')
vectors = model.read_vectors('inp_k-means_alexandr.xls')
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

