# 学习QLineEdit和QLabel

import sys
from PySide6.QtWidgets import (QApplication,
                                QWidget, 
                                QMainWindow,
                                QLineEdit,
                                QLabel,
                                QVBoxLayout,
                                QWidget)
from PySide6.QtCore import QSize
    

class MainWindwo(QMainWindow):
    def __init__(self):
        """
        初始化函数
        调用父类的初始化方法，设置窗口标题和大小，
        创建标签和行编辑器控件，并设置布局
        """
        # 调用父类的初始化方法
        super().__init__()

        # 设置窗口标题为'QLineEdit and QLabel'
        self.setWindowTitle('QLineEdit and QLabel')
        # 设置窗口固定大小为300x200像素
        self.setFixedSize(QSize(300, 200))

        # 创建一个显示'Hello World'的标签控件
        self.label = QLabel('Hello World')
        # 创建一个行编辑器控件
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("请输入文本") # 设置行编辑器的占位符文本
        self.line_edit.textChanged.connect(self.label.setText) # 将line_edit的文本变化信号与label的setText槽函数连接

        # 创建一个垂直布局，并将标签和行编辑器添加到布局中
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)    
      

        # 创建一个容器控件，并将布局设置为其layout布局
        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindwo()
    window.show()
    app.exec()