import lr2 as model
from pprint import pprint

# Есть струны | Есть гриф | Есть смычок | Есть клавиши | Размер (0 - небольшой, 1 - большой) | Материал (0 - Дерево, 1 - Металл) | Для извлечения звука нужно дуть
data = {'Гитара' :     [1, 1, 0, 0, 0, 0, 0],
        'Скрипка' :    [1, 1, 1, 0, 0, 0, 0],
        'Фортепиано' : [1, 0, 0, 1, 1, 0, 0],
        'Труба' :      [0, 0, 0, 0, 0, 1, 1],
        'Флейта' :     [0, 0, 0, 0, 0, 0, 1]}

test_data = {'Виолончель' : [1, 1, 1, 0, 1, 0, 0]}

features = 7
classes = ['Гитара', 'Скрипка', 'Фортепиано', 'Труба', 'Флейта']

model = model.Model(features, classes)
model.train(data, data, 10)
pprint(data)
print('Model: {}'.format(model.model))
print('Prediction: {}'.format(model.val(data)))
print('Prediction: {}'.format(model.run(test_data['Виолончель'])))
