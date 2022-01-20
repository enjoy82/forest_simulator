import config
import numpy as np
import copy

def crossover(child1, child2):
    if config.CROSSOVER_METHOD == "uniform":
        for i in range(len(child1.value)):
            if np.random.rand() < 0.5:
                child1.value[i], child2.value[i] = child2.value[i], child1.value[i]
    return child1, child2

def mutation(child):
    for i in range(len(child.value)):
        if np.random.rand() < config.MU:
            if np.random.rand() < 0.5:
                child.value[i] += np.random.rand() * config.M
                child.value[i] = min(2, child.value[i])
            else:
                child.value[i] -= np.random.rand() * config.M
                child.value[i] = max(0, child.value[i])
    return child

def select_offspring(elite_population):
    #ルーレット選択で選択する．
    taunament_size = int(((config.ELITE_POPULATION + 1) * config.ELITE_POPULATION) / 2)
    num = int(np.random.rand() * taunament_size)
    s = 0
    for i in range(len(elite_population)):
        s += config.ELITE_POPULATION - i
        if s > num:
            child = copy.deepcopy(elite_population[0])
            return child
    child = copy.deepcopy(elite_population[config.ELITE_POPULATION-1])
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