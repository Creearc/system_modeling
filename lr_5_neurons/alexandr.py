import lr5_engine as model

vectors = model.read_vectors('alexandr.xls') 
print(vectors)

C = 0.2
neuron = model.Neuron(3, C)

neuron.train(vectors, 1000)
