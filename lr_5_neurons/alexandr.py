import lr5_engine as model

vectors = model.read_vectors('alexandr.xls') 
print(vectors)

C = 0.2
neuron = model.Neuron(6, C)

neuron.train(vectors, 1000)

for i in range(1, 21):
    print(i, neuron.run(vectors[i][:-1]))
