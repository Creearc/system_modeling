import pandas as pd

def read_vectors(file):
    data = pd.read_excel(file)

    vectors = dict()
    for i in range(len(data['Объект'])):
        vectors[data['Объект'][i]] = [data[j][i] for j in data.columns[1:]]
    return vectors


class Model:
    def __init__(self, features, classes):
        self.features = features
        self.classes = classes
        
        self.model = [[0 for j in range(features)] for i in range(len(classes))]


    def iter(self, input_data, output):
        output_ind = self.classes.index(output)
        for i in range(len(self.model)):
            if i == output_ind:
                self.model[i] = [self.model[i][j] + input_data[j] for j in range(len(input_data))]
            else:
                self.model[i] = [self.model[i][j] - input_data[j] for j in range(len(input_data))]


    def train(self, train_data, val_data, max_iter=100):
        ind = 0
        keys = list(train_data.keys())
        ready = False
        iter_number = 0

        while not ready and iter_number != max_iter:
            print('Iter {} {}'.format(iter_number, self.model))
            iter_number += 1
            self.iter(train_data[keys[ind]], keys[ind])
            self.normalization()
            result = self.val(val_data)

            ind = -1
            for i in range(len(result)):
                if result[i][0] != result[i][1]:
                    ind = i
                    break
                
            if ind == -1:
                ready = True
        print('Train is over')


    def run(self, input_data):
        result = []
        for i in range(len(self.model)):
            result.append(sum([self.model[i][j] * input_data[j] for j in range(len(input_data))]))
        return self.classes[result.index(max(result))]


    def val(self, data):
        result = []
        for key ,element in data.items():
            result.append([self.run(element), key])
        return result
        

    def normalization(self):
        for i in range(len(self.model)):
            for j in range(len(self.model[i])):
                if self.model[i][j] > 1 : self.model[i][j] = 1
                if self.model[i][j] < -1 : self.model[i][j] = -1


if __name__ == '__main__':
    data  = read_vectors('inp.xls')

    test_data = {'ракета' : [0, 1, 0, 1, 0, 0]}

    features = 6
    classes = list(data.keys())

    
    model = Model(features, classes)
    print('Prediction: {}'.format(model.val(data)))
    
    print('Iter 1')
    model.iter(data['птица'], 'птица')
    print('Model: {}'.format(model.model))
    print('Prediction: {}'.format(model.val(data)))

    print('Iter 2')
    model.iter(data['самолет'], 'самолет')
    print('Model: {}'.format(model.model))
    print('Prediction: {}'.format(model.val(data)))
    

    print('Iter 3')
    model.iter(data['планер'], 'планер')
    model.normalization()
    print('Model: {}'.format(model.model))
    print('Prediction: {}'.format(model.val(data)))

    print('Iter 4')
    model.iter(data['планер'], 'планер')
    model.normalization()
    print('Model: {}'.format(model.model))
    print('Prediction: {}'.format(model.val(data)))


    print('Test')
    print('Prediction: {}'.format(model.run(test_data['ракета'])))
    print('________________________')

    model = Model(features, classes)
    model.train(data, data, 10)
    print('Model: {}'.format(model.model))
    print('Prediction: {}'.format(model.val(data)))
    print('Prediction: {}'.format(model.run(test_data['ракета'])))

    


