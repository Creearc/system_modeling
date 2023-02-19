
def activation_step(x, h):
    return 0 if x < h else 1

class La_memory_neuron:
    def __init__(self):
        self.q = 0

    def run(self, inp: list):
        w = [1, self.q]
        h = 2
        self.q = activation_step(sum([a*b for a,b in zip(inp, w)]), h)
        return self.q


if __name__ == '__main__':
    la_memory_neuron = La_memory_neuron()
    
    for i in range(2):
        for j in range(2):
            for la_memory_neuron.q in range(2):
                print(i, j, la_memory_neuron.q, la_memory_neuron.run([i, j]))
    
