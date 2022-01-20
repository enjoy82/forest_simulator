import copy
import numpy as np
import pandas as pd
import os

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
    return population

def show_result(res):
    kind = ["針葉樹", "広葉樹", "灌木"]
    size = ["低", "中", "高"]
    for i, k in enumerate(kind):
        for l, s in enumerate(size):
            print(f"{k} {s}木: {res[i][l]}本")

#TODO 出力，最後のテスト
def main():
    score_list = []
    most_elite_score = 1e18
    most_elite_gene = None
    state = State()
    print("Start state")
    state.show()
    show_result(state.count_tree_num())
    population = make_init_population()
    for i in range(config.GENERATIONS):
        print(f'start {i+1} / {config.GENERATIONS}')
        #評価用個体格納場所
        calc_population = []
        for gene in population:
            gene.reset_evaluation_value()
            cp_state = copy.deepcopy(state)
            simulator = Simurator(cp_state, gene)
            simulator.simulate(config.YEARS)
            calc_population.append(simulator.gene)
        #昇順ソート
        elite_population = sorted(calc_population, key=lambda ga: ga.evaluation_value)[:config.ELITE_POPULATION]
        #最も優秀な個体を保存しておく(追加検証のため)
        score_list.append(elite_population[0].evaluation_value)
        print(f"best score : {elite_population[0].evaluation_value}")
        if most_elite_score > elite_population[0].evaluation_value:
            most_elite_score = elite_population[0].evaluation_value
            most_elite_gene = elite_population[0]
        child_population = []
        for _ in range(config.CHILD_POPULATION//2):
            #エリート選択
            child1 = select_offspring(elite_population)
            child2 = select_offspring(elite_population)
            #交叉
            if np.random.rand() < config.CHI:
                child1, child2 = crossover(child1, child2)
            child1 = mutation(child1)
            child2 = mutation(child2)
            child_population.append(child1)
            child_population.append(child2)
        elite_population.extend(child_population)
        #世代交代
        population = elite_population
    df1 = pd.DataFrame(score_list)
    df1.to_csv(os.path.join(".", "log", "score.csv"))
    df2 = pd.DataFrame(most_elite_gene.value)
    df2.to_csv(os.path.join(".", "log", "elite_gene.csv"))
    cp_state = copy.deepcopy(state)
    simulator = Simurator(cp_state, most_elite_gene)
    simulator.simulate(config.EXP_YEAR)
    print("150年後の推定値 : ")
    show_result(simulator.state.count_tree_num())
    print("150年後の推定フィールド ")
    simulator.state.show()


if __name__ == '__main__':
    main()
 