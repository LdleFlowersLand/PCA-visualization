from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA


class myPCA():
    def __init__(self):
        self.n_components = None
        self.noise_variance = None
        self.explained_variance_ratio = None
        self.explained_variance = None

        self.reduced_x = None
        self.pca_1 = None
        self.y = None
        self.x = None
        self.setData()

    def setData(self):
        iris = datasets.load_iris()
        self.x = iris['data']  # 每个数据都有四个特征，分别是花萼长度，花萼宽度，花瓣长度，花瓣宽度
        self.y = iris['target'] # 红：class0，蓝：class1，绿：class2
        print(self.x)

    def refreshData(self, data_x, data_y):
        self.x = data_x
        self.y = data_y


    def doPCA(self):
        self.pca_1 = PCA(n_components=2)  # 指定主成分数量初始化
        self.reduced_x = self.pca_1.fit_transform(self.x)  # fit并直接得到降维结果
        self.explained_variance = self.pca_1.explained_variance_
        self.explained_variance_ratio = self.pca_1.explained_variance_ratio_
        self.noise_variance = self.pca_1.noise_variance_
        self.n_components = self.n_components

        self.class_dict_x = dict()
        self.class_dict_y = dict()

        self.green_y = []
        self.green_x = []
        self.blue_y = []
        self.blue_x = []
        self.red_y = []
        self.red_x = []


        for i in range(len(self.reduced_x)):
            if self.y[i] not in self.class_dict_x:
                self.class_dict_x[self.y[i]] = np.array([self.reduced_x[i][0]])
                self.class_dict_y[self.y[i]] = np.array([self.reduced_x[i][1]])
            else:
                self.class_dict_x[self.y[i]] = np.append(self.class_dict_x[self.y[i]], self.reduced_x[i][0])
                self.class_dict_y[self.y[i]] = np.append(self.class_dict_y[self.y[i]], self.reduced_x[i][1])


            if self.y[i] == 0:
                self.red_x.append(self.reduced_x[i][0])
                self.red_y.append(self.reduced_x[i][1])

            elif self.y[i] == 1:
                self.blue_x.append(self.reduced_x[i][0])
                self.blue_y.append(self.reduced_x[i][1])

            else:
                self.green_x.append(self.reduced_x[i][0])
                self.green_y.append(self.reduced_x[i][1])

