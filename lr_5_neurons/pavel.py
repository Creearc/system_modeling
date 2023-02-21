import lr5_engine as model

vectors = model.read_vectors('pavel.xls') 
print(vectors)

C = 0.2
neuron = model.Neuron(4, C)

neuron.train(vectors, 1000)
