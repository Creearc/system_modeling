import lr4_k_means as model

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
