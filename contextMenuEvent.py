# 右键菜单
import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow,QApplication,QMenu
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

# ====================方案1=============================
    def contextMenuEvent(self, event):
        right_menu = QMenu(self)
        right_menu.addAction(QAction("复制", self))
        right_menu.addAction(QAction("粘贴", self))
        right_menu.addAction(QAction("删除", self))
        right_menu.exec(self.mapToGlobal(event.pos()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())