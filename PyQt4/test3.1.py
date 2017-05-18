# -*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
'''
多文档窗体:
实现分割窗体
'''
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))


class MainWidget(QMainWindow):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        font = QFont(self.tr("黑体"), 12)
        QApplication.setFont(font)

        mainSplitter = QSplitter(Qt.Horizontal, self)
        leftText = QTextEdit(self.tr("左窗口"), mainSplitter)
        leftText.setAlignment(Qt.AlignCenter)
        rightSplitter = QSplitter(Qt.Vertical, mainSplitter)
        rightSplitter.setOpaqueResize(False)
        upText = QTextEdit(self.tr("上窗口"), rightSplitter)
        upText.setAlignment(Qt.AlignCenter)
        bottomText = QTextEdit(self.tr("下窗口"), rightSplitter)
        bottomText.setAlignment(Qt.AlignCenter)
        mainSplitter.setStretchFactor(1, 1)
        mainSplitter.setWindowTitle(self.tr("分割窗口"))

        self.setCentralWidget(mainSplitter)


app = QApplication(sys.argv)
main = MainWidget()
main.show()
app.exec_()