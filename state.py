import config
from setting import Needle_Leaf, Broad_Leaf, Shrub

class State:
    def __init__(self):
        self.field = [[None for _ in range(config.WIDTH)] for l in range(config.HEIGHT)]
        self._init_field()
    
    #初期フィールドの作成，この時点ではgene渡さない
    def _init_field(self):
        print("TODO")

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
                                    self.field[i+dx][l+dy] = Needle_Leaf()
                                elif self.field[i+dx][l+dy].get_class() == "Broad":
                                    self.field[i+dx][l+dy] = Broad_Leaf()
                                elif self.field[i+dx][l+dy].get_class() == "Shrub":
                                    self.field[i+dx][l+dy] = Shrub()
                                else:
                                    print("error!!!")