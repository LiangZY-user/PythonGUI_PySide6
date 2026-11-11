import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("这是一个标题")

        # 设置窗口大小
        self.setFixedSize(QSize(400, 300)) # 固定尺寸400x300
        #self.setMinimumSize(QSize(10,10))# 设置最小尺寸
        #self.setMaximumSize(QSize(600, 600))


        button = QPushButton("按钮")
        self.setCentralWidget(button)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()