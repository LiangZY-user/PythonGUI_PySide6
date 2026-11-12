# QMouseEvent   鼠标事件

import sys

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
from PySide6.QtCore import  QSize

class MainWindow(QMainWindow):
    def __init__(self):  # 初始化方法
        super().__init__()  # 调用父类的初始化方法
        # 设置窗口标题为'QMouseEvent'
        self.setWindowTitle('QMouseEvent')
        # 设置窗口固定大小为400x300像素
        self.setFixedSize(QSize(400, 300))

        # 创建一个标签，显示文本'请操作鼠标'
        self.label = QLabel('请操作鼠标', self)
        # 将标签设置为中心部件，使其占据窗口的主要区域
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, event):

        """鼠标移动事件处理函数
        
        当鼠标在控件上移动时触发此函数，更新标签显示鼠标的当前位置坐标
        
        参数:
            event: QMouseEvent对象，包含鼠标事件的相关信息
        """
        pos = event.position()
        self.label.setText(f'鼠标移动: {pos.x()}, {pos.y()}')  # 设置标签文本，显示鼠标的x和y坐标
    def mousePressEvent(self, event):  # 定义鼠标按下事件处理函数
        pos = event.position()
        self.label.setText(f'鼠标按下: {pos.x()}, {pos.y()}')
    def mouseReleaseEvent(self, event):  # 定义鼠标释放事件处理函数
        pos = event.position()
        self.label.setText(f'鼠标释放: {pos.x()}, {pos.y()}')  # 设置标签文本，显示鼠标释放时的坐标位置
    def mouseDoubleClickEvent(self, event):  # 定义一个处理鼠标双击事件的方法

        """
        处理鼠标双击事件的函数
        
        参数:
            event: 鼠标事件对象，包含鼠标点击的位置等信息
        """
        pos = event.position()
        self.label.setText(f'鼠标双击: {pos.x()}, {pos.y()}')  # 设置标签文本，显示鼠标双击的坐标位置

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
 