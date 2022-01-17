import config
import numpy as np
import copy

def crossover(child1, child2):
    if config.CROSSOVER_METHOD == "uniform":
        print("実装してください")
    return child1, child2

def mutation(child):
    print("実装してください")
    return child

def select_offspring(elite_population):
    print("実装してください")
    #deepcopyしないとpythonはだめ
    child = copy.deepcopy(elite_population[0])
    return child

class Gene:
    def __init__(self):
        self.value = [0.0 for _ in range(9)]
        self.evaluation_value = 0.0
        self._set_value()

    #評価値のリセット
    def reset_evaluation_value(self):
        self.evaluation_value = 0.0

    #初期値導入
    def _set_value(self):
        for i in range(9):
            self.value[i] = np.random.rand()

    def add_evaluation_value(self, evaluation_value):
        self.evaluation_value += evaluation_value