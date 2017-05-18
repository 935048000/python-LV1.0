# -*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
#import qrc_resource

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))
'''本实例实现一个基本主窗口程序，包含一个菜单条，一个工具栏，中央可编辑窗体及状态栏。'''

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("QMainWindow")
        self.text = QTextEdit()
        self.setCentralWidget(self.text)

        self.createActions()
        self.createMenus()
        self.createToolBars()

    def createActions(self):
        self.fileOpenAction = QAction(QIcon(":/fileopen.png"), self.tr("打开"), self)
        self.fileOpenAction.setShortcut("Ctrl+O")
        self.fileOpenAction.setStatusTip(self.tr("打开一个文件"))
        self.connect(self.fileOpenAction, SIGNAL("triggered()"), self.slotOpenFile)

        self.fileNewAction = QAction(QIcon(":/filenew.png"), self.tr("新建"), self)
        self.fileNewAction.setShortcut("Ctrl+N")
        self.fileNewAction.setStatusTip(self.tr("新建一个文件"))
        self.connect(self.fileNewAction, SIGNAL("triggered()"), self.slotNewFile)

        self.fileSaveAction = QAction(QIcon(":/filesave.png"), self.tr("保存"), self)
        self.fileSaveAction.setShortcut("Ctrl+S")
        self.fileSaveAction.setStatusTip(self.tr("保存文件"))
        self.connect(self.fileSaveAction, SIGNAL("triggered()"), self.slotSaveFile)

        self.exitAction = QAction(QIcon(":/filequit.png"), self.tr("退出"), self)
        self.exitAction.setShortcut("Ctrl+Q")
        self.setStatusTip(self.tr("退出"))
        self.connect(self.exitAction, SIGNAL("triggered()"), self.close)

        self.cutAction = QAction(QIcon(":/editcut.png"), self.tr("剪切"), self)
        self.cutAction.setShortcut("Ctrl+X")
        self.cutAction.setStatusTip(self.tr("剪切到粘贴板"))
        self.connect(self.cutAction, SIGNAL("triggered()"), self.text.cut)

        self.copyAction = QAction(QIcon(":/editcopy.png"), self.tr("复制"), self)
        self.copyAction.setShortcut("Ctrl+C")
        self.copyAction.setStatusTip(self.tr("复制到粘贴板"))
        self.connect(self.copyAction, SIGNAL("triggered()"), self.text.copy)

        self.pasteAction = QAction(QIcon(":/editpaste.png"), self.tr("粘贴"), self)
        self.pasteAction.setShortcut("Ctrl+V")
        self.pasteAction.setStatusTip(self.tr("粘贴内容到当前处"))
        self.connect(self.pasteAction, SIGNAL("triggered()"), self.text.paste)

        self.aboutAction = QAction(self.tr("关于"), self)
        self.connect(self.aboutAction, SIGNAL("triggered()"), self.slotAbout)

    def createMenus(self):
        fileMenu = self.menuBar().addMenu(self.tr("文件"))
        fileMenu.addAction(self.fileNewAction)
        fileMenu.addAction(self.fileOpenAction)
        fileMenu.addAction(self.fileSaveAction)
        fileMenu.addAction(self.exitAction)

        editMenu = self.menuBar().addMenu(self.tr("编辑"))
        editMenu.addAction(self.copyAction)
        editMenu.addAction(self.cutAction)
        editMenu.addAction(self.pasteAction)

        aboutMenu = self.menuBar().addMenu(self.tr("帮助"))
        aboutMenu.addAction(self.aboutAction)

    def createToolBars(self):
        fileToolBar = self.addToolBar("File")
        fileToolBar.addAction(self.fileNewAction)
        fileToolBar.addAction(self.fileOpenAction)
        fileToolBar.addAction(self.fileSaveAction)

        editTool = self.addToolBar("Edit")
        editTool.addAction(self.copyAction)
        editTool.addAction(self.cutAction)
        editTool.addAction(self.pasteAction)

    def slotNewFile(self):
        newWin = MainWindow()
        newWin.show()

    def slotOpenFile(self):
        fileName = QFileDialog.getOpenFileName(self)
        if fileName.isEmpty() == False:
            if self.text.document().isEmpty():
                self.loadFile(fileName)
            else:
                newWin = MainWindow()
                newWin.show()
                newWin.loadFile(fileName)

    def loadFile(self, fileName):
        file = QFile(fileName)
        if file.open(QIODevice.ReadOnly | QIODevice.Text):
            textStream = QTextStream(file)
            while textStream.atEnd() == False:
                self.text.append(textStream.readLine())

    def slotSaveFile(self):
        pass

    def slotAbout(self):
        QMessageBox.about("about me", self.tr("这是我们的第一个例子"))


#class MainWidget(QMainWindow):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        self.setWindowTitle(self.tr("依靠窗口"))

        te = QTextEdit(self.tr("主窗口"))
        te.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(te)

        # 停靠窗口1
        dock1 = QDockWidget(self.tr("停靠窗口1"), self)
        dock1.setFeatures(QDockWidget.DockWidgetMovable)
        dock1.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        te1 = QTextEdit(self.tr("窗口1,可在Main Window的左部和右部停靠，不可浮动，不可关闭"))
        dock1.setWidget(te1)
        self.addDockWidget(Qt.RightDockWidgetArea, dock1)

        # 停靠窗口2
        dock2 = QDockWidget(self.tr("停靠窗口2"), self)
        dock2.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetClosable)
        te2 = QTextEdit(self.tr("窗口2,只可浮动"))
        dock2.setWidget(te2)
        self.addDockWidget(Qt.RightDockWidgetArea, dock2)

        # 停靠窗口3
        dock3 = QDockWidget(self.tr("停靠窗口3"), self)
        dock3.setFeatures(QDockWidget.AllDockWidgetFeatures)
        te3 = QTextEdit(self.tr("窗口3,可在Main Window任意位置停靠，可浮动，可关闭"))
        dock3.setWidget(te3)
        self.addDockWidget(Qt.BottomDockWidgetArea, dock3)


app = QApplication(sys.argv)
main = MainWidget()
main.show()
#app.exec_()

app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec_()