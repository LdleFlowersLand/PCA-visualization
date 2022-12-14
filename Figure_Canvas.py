import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PCA import myPCA


class Figure_Canvas(FigureCanvas):   # 通过继承FigureCanvas类，使得该类既是一个PyQt5的Qwidget，又是一个matplotlib的FigureCanvas，这是连接pyqt5与matplot lib的关键
    def __init__(self, parent=None, width=5, height=2.5, dpi=100):
        super().__init__(parent)
        self.fig = Figure(figsize=(width, height), dpi=100)  # 创建一个Figure，注意：该Figure为matplotlib下的figure，不是matplotlib.pyplot下面的figure
        FigureCanvas.__init__(self, self.fig) # 初始化父类
        self.axes = self.fig.add_subplot(111) # 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法

    def test(self):
        pca1 = myPCA()

        self.axes.scatter(pca1.red_x,pca1.red_y,c='r',marker='.')
        self.axes.scatter(pca1.blue_x, pca1.blue_y, c='b', marker='.')
        self.axes.scatter(pca1.green_x, pca1.green_y, c='g', marker='.')
        # pca1.pltPCA()

        # x = [1,2,3,4,5,6,7,8,9]
        # y = [23,21,32,13,3,132,13,3,1]
        # self.axes.plot(x, y)
