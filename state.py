import config
import input
from setting import Needle_Leaf, Broad_Leaf, Shrub

import numpy as np

class State:
    def __init__(self):
        self.field = [[None for _ in range(config.WIDTH)] for l in range(config.HEIGHT)]
        self._init_field()
    
    #初期フィールドの作成，この時点ではgene渡さない
    def _init_field(self):
        #20万の樹が入ると仮定して設計する
        mul = config.NORMALIZE_SIZE // (config.WIDTH * config.HEIGHT)
        #for文回しまくって，Noneのところにはやしていく
        for i in range(len(input.FIRST_Needle_Leaf)):
            Needle_Leaf_num = int((input.FIRST_Needle_Leaf[i] * input.FIRST_ALL) // mul)
            print(Needle_Leaf_num)
            for _ in range(Needle_Leaf_num):
                while(1):
                    pos = int(np.random.rand() * (config.WIDTH * config.HEIGHT))
                    pos_x = pos % config.HEIGHT
                    pos_y = pos // config.WIDTH
                    if self.field[pos_y][pos_x] == None:
                        self.field[pos_y][pos_x] = Needle_Leaf(input.INIT_diameter[i])
                        break
        
        for i in range(len(input.FIRST_Broad_Leaf)):
            Broad_Leaf_num = int((input.FIRST_Broad_Leaf[i] * input.FIRST_ALL) // mul)
            print(Broad_Leaf_num)
            for _ in range(Broad_Leaf_num):
                while(1):
                    pos = int(np.random.rand() * (config.WIDTH * config.HEIGHT))
                    pos_x = pos % config.HEIGHT
                    pos_y = pos // config.WIDTH
                    if self.field[pos_y][pos_x] == None:
                        self.field[pos_y][pos_x] = Broad_Leaf(input.INIT_diameter[i])
                        break
        
        for i in range(len(input.FIRST_Shrub)):
            Shrub_num = int((input.FIRST_Shrub[i] * input.FIRST_ALL) // mul)
            print(Shrub_num)
            for _ in range(Shrub_num):
                while(1):
                    pos = int(np.random.rand() * (config.WIDTH * config.HEIGHT))
                    pos_x = pos % config.HEIGHT
                    pos_y = pos // config.WIDTH
                    if self.field[pos_y][pos_x] == None:
                        self.field[pos_y][pos_x] = Shrub(input.INIT_diameter[i])
                        break

    def show(self):
        size = [10, 30, 9999]
        print("show state")
        for row in self.field:
            row_message = []
            for px in row:
                if px == None:
                    row_message.append(input.NONE)
                elif px.get_class() == "Needle":
                    for i, s in enumerate(size):
                        if px.diameter < s:
                            row_message.append(input.Needle_symbol[i])
                elif px.get_class() == "Broad":
                    for i, s in enumerate(size):
                        if px.diameter < s:
                            row_message.append(input.Broad_symbol[i])
                elif px.get_class() == "Shrub":
                    for i, s in enumerate(size):
                        if px.diameter < s:
                            row_message.append(input.Shrub_symbol[i])
                else:
                    print("error!!")
            print(row_message)

    def count_tree_num(self):
        """
        木を数え上げる
        返り値は
        Needle 
        Broad
        Shrub
        の低中高
        """
        res = [[0 for _ in range(3)] for _ in range(3)]
        size = [10, 30, 9999]
        for row in self.field:
            for px in row:
                if px == None:
                    continue
                elif px.get_class() == "Needle":
                    for i, s in enumerate(size):
                        if px.diameter < s:
                            res[0][i] += 1
                            break
                elif px.get_class() == "Broad":
                    for i, s in enumerate(size):
                        if px.diameter < s:
                            res[1][i] += 1
                            break
                elif px.get_class() == "Shrub":
                    for i, s in enumerate(size):
                        if px.diameter < s:
                            res[2][i] += 1
                            break
                else:
                    print("error!!")
        return res


    #木にその設定を一括で埋め込む関数
    def set_gene(self, gene):
        for i in range(len(self.field)):
            for l in range(len(self.field[i])):
                if self.field[i][l] == None:
                    continue
                else:
                    self.field[i][l].get_gene(gene)

    #木の年数で枯れる判定を回す関数
    def is_blast(self):
        for i in range(len(self.field)):
            for l in range(len(self.field[i])):
                #パス
                if self.field[i][l] == None:
                    continue
                if self.field[i][l].blast():
                    #枯れた場合いつ土に返す？？
                    self.field[i][l] = None


    #木が病気かの判定を回す関数
    def is_disease(self):
        for i in range(len(self.field)):
            for l in range(len(self.field[i])):
                #パス
                if self.field[i][l] == None:
                    continue
                if self.field[i][l].desease():
                    #枯れた場合いつ土に返す？？
                    self.field[i][l] = None
    
    #木の成長判定回す関数
    def grouwth(self):
        for i in range(len(self.field)):
            for l in range(len(self.field[i])):
                #パス
                if self.field[i][l] == None:
                    continue
                else:
                    self.field[i][l].grow()

    def set_new_tree(self):
        dx_lis = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy_lis = [-1, 0, 1, -1, 1, -1, 0, 1]
        for i in range(len(self.field)):
            for l in range(len(self.field[i])):
                if self.field[i][l] == None:
                    for dx, dy in zip(dx_lis, dy_lis):
                        #画面外判定
                        if (i + dx < 0) or (l + dy < 0) or (i + dx >= len(self.field)) or (l + dy >= len(self.field[0])):
                            continue
                        if self.field[i+dx][l+dy] == None:
                            continue
                        else:
                            #木を生やす判定
                            if self.field[i+dx][l+dy].breed():
                                if self.field[i+dx][l+dy].get_class() == "Needle":
                                    self.field[i][l] = Needle_Leaf(1)
                                    gene = self.field[i+dx][l+dy].gene
                                    self.field[i][l].get_gene(gene)
                                elif self.field[i+dx][l+dy].get_class() == "Broad":
                                    self.field[i][l] = Broad_Leaf(1)
                                    gene = self.field[i+dx][l+dy].gene
                                    self.field[i][l].get_gene(gene)
                                elif self.field[i+dx][l+dy].get_class() == "Shrub":
                                    self.field[i][l] = Shrub(1)
                                    gene = self.field[i+dx][l+dy].gene
                                    self.field[i][l].get_gene(gene)
                                else:
                                    print("error!!!")