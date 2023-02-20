# import math
# import numpy as np
# import pandas as pd
from random import randint
from pprint import pprint


def activation_step(x, h):
    return 0 if x < h else 1

def activation_heaviside(x, h):
    if x == h:
        return 0.5
    return 0 if x < h else 1

def or_neuron(inp: list):
    w = [1, 1]
    h = 1
    return activation_step(sum([a*b for a,b in zip(inp, w)]), h)

def and_neuron(inp: list):
    w = [1, 1]
    h = 2
    return activation_step(sum([a*b for a,b in zip(inp, w)]), h)

def not_neuron(inp: list):
    w = [-1]
    h = 0
    return activation_step(sum([a*b for a,b in zip(inp, w)]), h)

def test_1():
    weights = [-1, 2]
    for h in range(-1, 3):
        print('________\nh =',h)
        print('x1', 'x2', 'y')
        for x1 in [0,1]:
            for x2 in [0,1]:
                print(x1, x2, neuron([x1,x2], weights, h))

def test_OR_AND_NOT():
    out_or = []
    out_and = []
    out_not = []
    for x1 in [0,1]:
        out_not.append([x1, not_neuron([x1])])
        for x2 in [0,1]:
            out_or.append([x1, x2, or_neuron([x1,x2])])
            out_and.append([x1, x2, and_neuron([x1,x2])])
    print('OR')
    pprint(out_or)
    print('AND')
    pprint(out_and)
    print('NOT')
    pprint(out_not)


def neuron(inp: list, w: list, h):
    return activation_step(sum([a*b for a,b in zip(inp, w)]), h)


class Memory:
    def __init__(self):
        self.q = 0

    def event(self, mx=1):
        if self.q < mx:
            self.q += 1
        return self.q

    def reset(self):
        self.q = 0


def cocroach(inp: list): # Вход: касание, ветер, нет касания
    n1 = neuron(inp[:-1], [1, 1], 2)
    n2 = neuron(inp[1:], [1, 1], 2)
    return [n1, n2]

def dog(inp: list): # Вход: миска, стол, хозяин
    out = neuron(inp, [1, 2, -1], 2)
    return out

def dog2(inp: list): # Вход: миска, стол, хозяин
    n1 = neuron(inp, [2, -1, 1], 2) # Ест в миске
    n2 = neuron(inp, [1, 2, -2], 2) # Ест на столе
    return [n1, n2]

def butterfly(inp: list): # Вход: солнце, температура меньше равна 36 градусов
    out = neuron(inp, [2, -1], 2)
    return out

def chicken(inp: list, memory): # Вход: пища, желтое и полосатое
    n1 = neuron(inp, [0, memory.q], 1)
    n2 = neuron(inp, [1, -memory.q], 1)
    if inp[1] == 1:
        memory.event()
    return [n1, n2] # Бежать, клевать

# def crow(inp: list, memory): # Вход: [заходит, выходит]
#     n1 = neuron(inp, [memory.q], 1)
#     if inp == 1:
#         memory.event()
#     return n1 # 1 - Ждать/ 0 - лететь


if __name__ == '__main__':
    # test_1()
    # test_OR_AND_NOT()

    # out = butterfly([0, 0])
    # print(out)

    # ----------------------------------------

    chicken_memory = Memory()
    events = [randint(0, 1) for i in range(20)]
    print(events)

    for i, e in enumerate(events):
        print(e)
        out = chicken([1, e], chicken_memory)
        print(out)
        if i == 10:
            print('_____')
            chicken_memory.reset()

    # ----------------------------------------

    # crow_memory = Memory()
    # events = [[randint(0, 1), randint(0, 1)] for i in range(20)]

    # for i, e in enumerate(events):
    #     print(e, crow_memory.q)
    #     out = crow(e, crow_memory)
    #     print(out)

