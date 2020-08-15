import sys
import time
import webbrowser

from time import ctime
from PyQt5.QtCore import  QThread, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QMainWindow,
                             QApplication,
                             QAction,
                             qApp)

class StatusBarThread(QThread):
    trigger = pyqtSignal()
    def __init__(self):
        super(StatusBarThread, self).__init__()

    def run(self) -> None:
        while True:
            self.trigger.emit()
            time.sleep(1)


class Rogue(QMainWindow):
    def __init__(self):
        super(Rogue, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(50,50,800,1000)
        self.setWindowTitle("Rogue Eyesight Protector")
        self.setWindowIcon(QIcon("rogue.jpg"))
        self.setToolTip("听蛋蛋扯淡总有种扯到蛋蛋的忧伤")

        # status bar
        self.statusBar_show()
        # exit short cut
        self.fileMenu_edit()

        self.show()

    def fileMenu_edit(self):
        exitAct = QAction(QIcon("exit.jpg"), "&Exit", self)
        exitAct.setShortcut("Ctrl+C")
#        exitAct.setStatusTip("PlaceTaker")
        exitAct.triggered.connect(qApp.quit)

        gitAct = QAction(QIcon("github.jpg"),"&GitHub star", self)
        gitAct.setShortcut("Ctrl+G")
        gitAct.triggered.connect()

        eggAct = QAction(QIcon("egg.jpg"),"&Egg", self)
        eggAct.setShortcut("Ctrl+E")
        #eggAct.triggered.connect()

        menubar = self.menuBar()
        filemenu = menubar.addMenu("关于作者")
        filemenu.addAction(gitAct)
        filemenu.addAction(eggAct)
        filemenu.addAction(exitAct)
        #self.addAction(exitAct)

    def githubUrl(self):
        webbrowser.open("")

    def statusBar_show(self):
        self.status = StatusBarThread() # 为啥一定要写self, 不然无法关联么...
        self.status.trigger.connect(self.updateStatusBar)
        self.status.start()  # 我是不是调用错了.....得调用Start...?

    def updateStatusBar(self):
        self.statusBar().showMessage(ctime()+"    已工作: "+""+"h "+""+"min "\
                              +"休息:"+"h "+""+"min ")

app = QApplication(sys.argv)
config = Rogue()
sys.exit(app.exec_())