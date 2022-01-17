import config

from GA import Gene
from state import State

class Simurator:
    def __init__(self, state, gene):
        self.gene = gene
        self.state = state
        self.state.set_gene(gene)

    def simulate():
        for i in range(config.YEARS):
            #年ごとに判定を回す
            print("TODO")
    
    #評価値を計算する関数
    def calc_eval(self, year):
        print("TODO")