import lr2 as model

data = model.read_vectors('alexandr.xls')

features = 7
classes = list(data.keys())

model = model.Model(features, classes)
model.train(data, data, 12)
print('Model: {}'.format(model.model))
print('Prediction: {}'.format(model.val(data)))

