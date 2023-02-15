import lr2 as model

data = {'птица' : [1, 1, 1, 0, 1, 0],
        'самолет' : [1, 1, 0, 1, 0, 1],
        'планер' : [1, 1, 0, 0, 0, 0]}

test_data = {'ракета' : [0, 1, 0, 1, 0, 0]}

features = 6
classes = ['птица', 'самолет', 'планер']

model = model.Model(features, classes)
model.train(data, data, 10)
print('Model: {}'.format(model.model))
print('Prediction: {}'.format(model.val(data)))
print('Prediction: {}'.format(model.run(test_data['ракета'])))
