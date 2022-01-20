import config 
from GA import Gene

import numpy as np

#基底クラス
class Tree:
    #初期入力で木の直径は知りたい
    def __init__(self, diameter):
        #diameterは木の半径
        self.diameter = diameter

    #geneを投げる
    def get_gene(self, gene):
        self.gene = gene

    #寿命で枯れているかの判定関数 TODO
    def blast(self):
        return False
    
    #木の直径を増やす関数 TODO
    def grow(self):
        #TODO　計算式あやしい！！！
        #0.3mを8~15 -> 11.5として扱う
        self.diameter += 0.3 / 11.5
    
    #病気で枯れているかの判定関数 TODO
    def desease(self):
        return False
    
    def get_class(self):
        return "no_class"

    def get_size(self):
        #TODO　計算式あやしい！！！
        #高中低の順番のインデックスを返す
        if self.diameter < 10:
            return 2
        elif self.diameter < 30.0:
            return 1
        else:
            return 0
    
    #次に生えてくるかどうかの確率 TODO
    def breed(self):
        return False

class Needle_Leaf(Tree):
    #寿命で枯れているかの判定関数
    def blast(self):
        if self.diameter > 35 and np.random.rand() < 0.2:
            return True
        return False
    
    #木の直径を増やす関数
    def grow(self):
        self.diameter += (30 / 37.5) * self.gene.value[0]
    
    #病気で枯れているかの判定関数
    def desease(self):
        if np.random.rand() < 0.2 * self.gene.value[3+0]:
            return True
        return False
        
    def get_class(self):
        return "Needle"
    
    def breed(self):
        if np.random.rand() < 0.3*self.gene.value[2*3+0]:
            return True
        return False
    
class Broad_Leaf(Tree):
    #寿命で枯れているかの判定関数
    def blast(self):
        if self.diameter > 35 and np.random.rand() < 0.2:
            return True
        return False
    
    #木の直径を増やす関数
    def grow(self):
        self.diameter += (30 / 48) * self.gene.value[1]
    
    #病気で枯れているかの判定関数
    def desease(self):
        if np.random.rand() < 0.2 * self.gene.value[3+1]:
            return True
        return False
        
    def get_class(self):
        return "Broad"
    
    def breed(self):
        if np.random.rand() < 0.3*self.gene.value[2*3+1]:
            return True
        return False

class Shrub(Tree):
    #寿命で枯れているかの判定関数
    def blast(self):
        if self.diameter > 10 and np.random.rand() < 0.3:
            return True
        return False
    
    #木の直径を増やす関数
    def grow(self):
        self.diameter += (30 / 37.5) * self.gene.value[2]
    
    #病気で枯れているかの判定関数
    def desease(self):
        if np.random.rand() < 0.2 * self.gene.value[3+2]:
            return True
        return False
        
    def get_class(self):
        return "Shrub"

    def breed(self):
        if np.random.rand() < 0.5*self.gene.value[2*3+2]:
            return True
        return False