import pandas as pd
import numpy as np
import pprint
import random


def read_vectors(file):
    data = pd.read_excel(file)

    vectors = dict()
    for i in range(len(data['Пример'])):
        vectors[data['Пример'][i]] = [data[j][i] for j in data.columns[1:]]
    return vectors


def sign(s):
    return -1 if s < 0 else 1


pavel = lambda inp, w : sum([a*b for a,b in zip(inp, w)])


class Neuron:
    def __init__(self, size, c):
        self.k = [random.randint(-100, 100) / 100 for i in range(size)]

        self.c = c


    def run(self, inp: list):
        return sign(pavel(inp, self.k))


    def delta_rule(self, res, y, x):
        res = self.c * (y - res)
        for i in range(len(self.k)):
            self.k[i]+= res * x[i]


    def train(self, vector, max_iter=100):
        for iter_number in range(max_iter):
            print('Iter {} {}'.format(iter_number, self.k))
            ready = True
            for i, vector in vectors.items():
                x, y = vector[:-1], vector[-1]
                res = neuron.run(x)
                if res != y:
                    neuron.delta_rule(res, y, x)
                    ready = False
            if ready:
                break
        print('Train is over')
            
    

if __name__ == '__main__':
    vectors = read_vectors('inp.xls')    
    print(vectors)

    C = 0.2
    neuron = Neuron(3, C)

    neuron.train(vectors, 1000)

    print(neuron.run(vectors[1][:-1]))

    
