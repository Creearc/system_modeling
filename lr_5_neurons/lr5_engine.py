import pandas as pd
import numpy as np
import pprint


def read_vectors(file):
    data = pd.read_excel(file)

    vectors = dict()
    for i in range(len(data['Пример'])):
        vectors[data['Пример'][i]] = [data[j][i] for j in data.columns[1:]]
    return vectors


def sign(s):
    return -1 if s < 0 else 1


if __name__ == '__main__':
    vectors = read_vectors('inp.xls')    
    print(vectors)

    C = 0.2
