import pandas as pd
import math
from pprint import pprint

# x1 = ['П', 'Н', 'Х'] # кредитная история
# x2 = ['В', 'Н'] # долг
# x3 = ['Н', 'А'] # поручительство
# x4 = [[0, 15], [15, 35], [35]] # доход
# y = ['В', 'С', 'Н']
data = pd.read_excel('inp.xls')


def calc_uncert(arr: list) -> float:
    out = 0
    unique = set(arr)
    for el in unique:
        cnt = arr.count(el)/len(arr)
        out += cnt * math.log(cnt, 2) * (-1)
    return out



def get_value(data, x, y):
    out = dict()
    out_un = dict()
    val_sum = 0

    keys = set(data[x])
    for key in keys:
        out[key] = []
        for i, el in enumerate(list(data[y])):
            if data[x].iloc[i] == key:
                out[key].append(el)
        out_un[key] = calc_uncert(out[key])

        val_sum += len(out[key])/len(data[y]) * out_un[key]

    return out, out_un, val_sum


if __name__ == '__main__':
    print(data)
    columns = list(data.columns)
    answer = dict()

    target = 'y'
    columns.pop(columns.index(target))
    current_uncert = []

    for cln in columns:
        
        out, un, val_sum = get_value(data, cln, target)
        current_uncert.append(val_sum)

        print('__________________')
        print(cln)
        pprint(out)
        pprint(un)
        print(val_sum)
    
    vert_ind = columns[current_uncert.index(min(current_uncert))]
    answer[vert_ind] = dict()
    columns.pop(columns.index(vert_ind))
    current_uncert = []

    print(answer)
    print(columns)

    print('======================')

    for cln in columns:
        
        out, un, val_sum = get_value(data, cln, target)
        current_uncert.append(val_sum)

        print('__________________')
        print(cln)
        pprint(un)
        print(val_sum)
    
    vert_ind = columns[current_uncert.index(min(current_uncert))]
    answer[vert_ind] = dict()
    columns.pop(columns.index(vert_ind))

    print(answer)
    print(columns)
