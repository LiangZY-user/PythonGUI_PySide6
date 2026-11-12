import random
import sys
from random import choice

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize

windows_title = [
    "标题1",
    "标题2",
    "标题3",
    "标题4",
    "标题5",
    "标题6"
]

class MainWindow(QMainWindow):
    def __init__(self):
        """
        要在类中不受作用域的访问，添加self
        """
        super().__init__()

        self.is_clicked = False
        self.setWindowTitle("Button Test")
        self.setFixedSize(QSize(400, 300))
        self.button = QPushButton("点击我")

        self.setCentralWidget(self.button)
        self.button.setCheckable(self.is_clicked) #设置按钮是否拥有可切换选中的能力。
        self.button.clicked.connect(self.mysetWindowstitle) # 按钮绑定信号槽
        self.windowTitleChanged.connect(self.checksetWindowstitle) #把新标题字符串传给这个槽

    def mysetWindowstitle(self):
        print("设置窗口标题")
        newwindow = choice(windows_title) # choice() 方法从序列中随机返回一个元素
        print(f"新的标题是{newwindow}")
        self.setWindowTitle(newwindow) # 设置窗口标题

    def checksetWindowstitle(self,newwindowtitle):
        print(f"当前标题是：{newwindowtitle}")
        if newwindowtitle == "标题3":
            self.button.setText("push me")
            # 以下两行代码功能一致
            self.button.setDisabled(True)
            #self.button.setEnabled(False)

    # 与构造函数同级
    def the_clicked(self, checked): # checked 内部变量，默认是False
        self.is_clicked = checked
        print("this is clicked",checked)

    def button_setText(self):
        self.button.setText("push me")
        self.button.setEnabled(False) # 设置按钮不可点击
        self.setWindowTitle("按钮已不可点击")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()