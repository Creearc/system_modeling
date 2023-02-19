import pandas as pd
import numpy as np
import pprint

def read_vectors(file):
    data = pd.read_excel(file)

    vectors = dict()
    for i in range(len(data['Объект'])):
        vectors[data['Объект'][i]] = [data[j][i] for j in data.columns[1:]]
    return vectors


def similarity(vectors):    
    e1 = sum([np.prod([vectors[j][i] for j in range(len(vectors))]) for i in range(len(vectors[0]))])
    e2 = np.prod([sum([vectors[i][j] ** 2 for j in range(len(vectors[i]))]) for i in range(len(vectors))])
    return round(e1 / np.sqrt(e2), 3)


def find_similarities(vectors):
    keys = list(vectors.keys())
    keys_high = keys.copy()
    mx = [-1, []]
    mx_old = mx[1].copy()

    result = None

    while len(mx[1]) < len(vectors.keys()):
        for key_1 in keys_high:
            for key_2 in keys:
                if key_1 == key_2:
                    continue
                tmp_keys = key_1 + [key_2] if isinstance(key_1, list) else [key_1, key_2]
                res = similarity([vectors[i] for i in tmp_keys])
                if res > mx[0]:
                    mx = [res, tmp_keys]

        for i in mx[1][-2:]:
            if i in keys:
                keys.pop(keys.index(i))

        print(mx)
        result = {mx[0] : [result, mx[1][len(mx_old):]]}
        
        keys_high = [mx[1].copy()]
        mx[0] = -1
        mx_old = mx[1].copy()
        
    return result


def calc_uncert(arr: list) -> float:
    out = 0
    unique = set(arr)
    for el in unique:
        cnt = arr.count(el)/len(arr)
        out += cnt * math.log(cnt, 2) * (-1)
    return out


if __name__ == '__main__':
    vectors = read_vectors('inp.xls')    
    print(vectors)

    result = find_similarities(vectors)
    print(result)
    pprint.pprint(result)

    


