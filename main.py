import copy
import numpy as np

import config
from GA import Gene, select_offspring, crossover, mutation
from state import State
from simulator import Simurator

def make_init_population():
    #初期個体を生成する
    population = []
    for _ in range(config.CHILD_POPULATION + config.ELITE_POPULATION):
        gene = Gene()
        population.append(gene)

#TODO 出力，最後のテスト
def main():
    state = State()
    population = make_init_population()
    for i in range(config.GENERATIONS):
        print(f'start {i+1} / {config.GENERATIONS}')
        #初期化
        population = []
        for gene in population:
            gene.reset_evaluation_value()
            cp_state = copy.deepcopy(state)
            simulator = Simurator(cp_state, gene)
            simulator.simulate()
            population.append(simulator.gene)
        elite_population = sorted(population, key=lambda ga: ga.evaluation_value, reverse=True)[:config.ELITE_POPULATION]
        child_population = []
        for _ in range(config.CHILD_POPULATION//2):
            #エリート選択
            child1 = select_offspring(elite_population)
            child2 = select_offspring(elite_population)
            #交叉
            if np.random.rand() < config.CHI:
                child1, child2 = crossover(child1, child2)
            #突然変異
            if np.random.rand() < config.MU:
                child1 = mutation(child1)
            if np.random.rand() < config.MU:
                child2 = mutation(child2)
            child_population.append(child1)
            child_population.append(child2)
        elite_population.extend(child_population)
        #世代交代
        population = elite_population


if __name__ == '__main__':
    main()
 