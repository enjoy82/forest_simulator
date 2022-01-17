import config 
from GA import Gene

#基底クラス
class Tree:
    #初期入力で木の直径は知りたい
    def __init__(self, diameter):
        self.diameter = diameter
        self.gene = [1.0 for _ in range(9)]

    #geneを投げる
    def get_gene(self, gene):
        self.gene = gene

    #寿命で枯れているかの判定関数 TODO
    def blast(self):
        return False
    
    #木の直径を増やす関数 TODO
    def grow(self):
        self.diameter += 1.0
    
    #病気で枯れているかの判定関数 TODO
    def desease(self):
        return False
    
    def get_class(self):
        return "no_class"

    def get_class(self):
        if self.diameter < 3.0:
            return "Short"
        elif self.diameter < 15.0:
            return "Medium"
        else:
            return "Tall"
    
    #次に生えてくるかどうかの確率 TODO
    def breed(self):
        return False

class Needle_Leaf(Tree):
    #寿命で枯れているかの判定関数
    def blast(self):
        return False
    
    #木の直径を増やす関数
    def grow(self):
        self.diameter += 1.0
    
    #病気で枯れているかの判定関数
    def desease(self):
        return False
        
    def get_class(self):
        return "Needle"
    
    def breed(self):
        return False
    
class Broad_Leaf(Tree):
    #寿命で枯れているかの判定関数
    def blast(self):
        return False
    
    #木の直径を増やす関数
    def grow(self):
        self.diameter += 1.0
    
    #病気で枯れているかの判定関数
    def desease(self):
        return False
        
    def get_class(self):
        return "Broad"
    
    def breed(self):
        return False

class Shrub(Tree):
    #寿命で枯れているかの判定関数
    def blast(self):
        return False
    
    #木の直径を増やす関数
    def grow(self):
        self.diameter += 1.0
    
    #病気で枯れているかの判定関数
    def desease(self):
        return False
        
    def get_class(self):
        return "Shrub"

    def breed(self):
        return False