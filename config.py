import sys
import json

from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import  (QWidget,
                              QApplication,
                              QToolTip,
                              QPushButton,
                              )

class ConfigQWidget(QWidget):
    def __init__(self, app):
        super(ConfigQWidget, self).__init__()
        self.desktop = app.desktop()
        self.wid = 640 # width config
        self.hei = 480 # height config
        self.initUI()

    def save_configure(self):
        pass
        # self.check()
        # self.write()

    def bottomBtn(self):
        button_gap = 100
        # escape button
        escBtn = QPushButton('取消',self)
        #escBtn.resize(escBtn.sizeHint())
        escBtn.move((self.width()-button_gap)/2-escBtn.width(),self.height()-escBtn.height()-button_gap/2)
        escBtn.clicked.connect(self.close) # close current window
       # ensure button
        sureBtn = QPushButton('确定',self)
        sureBtn.move((self.width() + button_gap) / 2, self.height()-sureBtn.height()-button_gap/2)
        sureBtn.clicked.connect(self.save_configure) # write json file

    def initUI(self):
        # tooltip
        QToolTip.setFont(QFont("SansSerif", 10))
        self.setToolTip("<b>呼~~~呀~~~!</b>")
        # basic setip {title, icon, location-size}
        self.setWindowTitle("Config Window.")
        self.setWindowIcon(QIcon("config.jpg")) # application icon
        self.setGeometry((self.desktop.width()-self.wid)//2,\
                         (self.desktop.height()-self.hei)//2,\
                         640,480)
        #statusBar


        # button setup
        self.bottomBtn()

        self.show()

app = QApplication(sys.argv)
config = ConfigQWidget(app)
sys.exit(app.exec_())