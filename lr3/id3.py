import pandas as pd
import math
from pprint import pprint


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


def get_answer(data, columns, target, if_print=False, step=1):
    
    if if_print:
        print('\n----------------')
        print('Уровень дерева', step)
        print('\nДанные:')
        pprint(data)

    answer = dict()
    all_tar = dict()
    all_un = dict()
    all_current_uncert = dict()

    if target in columns:
        columns.pop(columns.index(target))

    for cln in columns:
        tar, un, val_sum = get_value(data, cln, target)
        all_tar[cln] = tar
        all_un[cln] = un
        all_current_uncert[cln] = val_sum

    if if_print:
        print('\nЗначения целевого показателя')
        pprint(all_tar)
        print('\nЗначения неопределенности целевого показателя')
        pprint(all_un)
        print('\nЗначения неопределенности ветки')
        pprint(all_current_uncert)

    if list(all_current_uncert.keys()) != []:
        vert = min(all_current_uncert, key=all_current_uncert.get)
        columns.pop(columns.index(vert))

        ans = all_un[vert]
        for key in all_un[vert]:
            if all_un[vert][key] == 0:
                ans[key] = all_tar[vert][key][0]
                data = data[data[vert] != key]
            else:
                ans[key] = get_answer(data[data[vert] == key], columns.copy(), target, if_print=if_print, step=step+1)
        answer[vert] = ans
        return answer
    else:
        return None


if __name__ == '__main__':

    data = pd.read_excel('inp.xls')
    target = 'y'

    answer = get_answer(data, list(data.columns), target)
    print('\n======================')
    print('---Финальное дерево---')
    pprint(answer)
