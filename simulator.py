import config
import input
from GA import Gene
from state import State


class Simurator:
    def __init__(self, state, gene):
        self.gene = gene
        self.state = state
        self.state.set_gene(gene)

    def simulate(self, year):
        for i in range(year):
            self.state.grouwth() #木を成長させる
            self.state.is_disease() #木を病気にする
            self.state.is_blast() #枯れ木にする
            self.state.set_new_tree() #木を生やす
            for year in input.EVAL_YEARS: 
                if i+1 == year:
                    self.calc_eval(year) #評価する
    
    #評価値を計算する関数
    def calc_eval(self, year):
        mul = config.NORMALIZE_SIZE // (config.HEIGHT * config.WIDTH)
        score = 0
        count_tree = self.state.count_tree_num()
        #TODO check!!
        print(count_tree)
        #self.state.show()
        if year == 50:
            for i in range(len(input.SECOND_Needle_Leaf)):
                num = int((input.SECOND_ALL * input.SECOND_Needle_Leaf[i]) // mul)
                score += abs(num - count_tree[0][i])
            for i in range(len(input.SECOND_Broad_Leaf)):
                num = int((input.SECOND_ALL * input.SECOND_Broad_Leaf[i]) // mul)
                score += abs(num - count_tree[1][i]) 
            for i  in range(len(input.SECOND_Shrub)):
                num = int((input.SECOND_ALL * input.SECOND_Shrub[i]) // mul)
                score += abs(num - count_tree[2][i])
        if year == 100:
            for i in range(len(input.THIRD_Needle_Leaf)):
                num = int((input.THIRD_ALL * input.THIRD_Needle_Leaf[i]) // mul)
                score += abs(num - count_tree[0][i])
            for i in range(len(input.SECOND_Broad_Leaf)):
                num = int((input.THIRD_ALL * input.THIRD_Broad_Leaf[i]) // mul)
                score += abs(num - count_tree[1][i])
            for i  in range(len(input.THIRD_Shrub)):
                num = int((input.THIRD_ALL * input.THIRD_Shrub[i]) // mul)
                score += abs(num - count_tree[2][i])
        self.gene.add_evaluation_value(score)