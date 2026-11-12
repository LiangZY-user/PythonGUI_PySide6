
# 检查鼠标状态
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel,QApplication,QMainWindow

class MouseButton(QMainWindow):
    def __init__(self):
        super().__init__()

        self.lab = QLabel("检测鼠标状态")
        self.setCentralWidget(self.lab)

    def mousePressEvent(self, event):
        """
        检测鼠标单击状态
        :param 当鼠标在窗口区域按下按键，QMouseEvent会自动调用这个函数，把（对象事件包）传进来用event接住
        :return:
        """
        # event.button() 读出这次是哪个按键触发的按下
        if event.button() == Qt.MouseButton.LeftButton:
            self.lab.setText("鼠标左键按下")
        elif event.button() == Qt.MouseButton.RightButton:
            self.lab.setText("鼠标右键按下")
        elif event.button() == Qt.MouseButton.MiddleButton:
            self.lab.setText("鼠标中键按下")

    def mouseReleaseEvent(self, event):
        """
        :param event: 当鼠标在窗口区域按下按键并释放按键，QMouseEvent会自动调用这个函数，把（对象事件包）传进来用event接住
        :return:
        """
        if Qt.MouseButton.LeftButton == event.button():
            self.lab.setText("鼠标左键已释放")
        elif Qt.MouseButton.RightButton == event.button():
            self.lab.setText("鼠标右键已释放")
        elif Qt.MouseButton.MiddleButton == event.button():
            self.lab.setText("鼠标中键已释放")

    def mouseDoubleClickEvent(self, event):
        """
        :param event: 当鼠标在窗口区域双击按键，QMouseEvent会自动调用这个函数，把（对象事件包）传进来用event接住
        :return:
        """
        if Qt.MouseButton.LeftButton == event.button():
            self.lab.setText("鼠标左键双击")
        elif Qt.MouseButton.RightButton == event.button():
            self.lab.setText("鼠标右键双击")
        elif Qt.MouseButton.MiddleButton == event.button():
            self.lab.setText("鼠标中键双击")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MouseButton()
    window.show()
    app.exec()