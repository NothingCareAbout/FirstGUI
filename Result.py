import os
import sys
from typing_extensions import Self
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from calcuShear import *

class ShearKey(object):
    def __init__(self):
        super(ShearKey, self).__init__()
        
        def getDir():
            dir=os.getcwd()
            files=os.listdir(dir)
            for name in files:
                if name=="shear_key.ui":
                    return os.path.join(dir,name)
        
        uifile=getDir()#动态加载UI文件
        self.ui=uic.loadUi(uifile)
        
        pixmap=QPixmap("H形钢截面样式2.png")
        self.ui.pit_label.setPixmap(pixmap)
        self.ui.pit_label.setScaledContents(True) #自适应
        self.ui.setWindowIcon(QIcon("icon.ico"))
        self.ui.Button_h.clicked.connect(self.test)
        
    def test(self):
        B=int(self.ui.WidthValueEdit.text())
        H=int(self.ui.HeightValueEdit.text())
        t=int(self.ui.tValueEdit.text())
        tw=int(self.ui.twValueEdit.text())
        B1=int(self.ui.B1ValueEdit.text())
        self.sh=Shear(B,H,t,tw,B1)
        h=self.sh.cal_h()
        V=self.sh.cal_V()
        M=self.sh.cal_M()
        self.ui.hResultEdit.setText(str(h)+"mm")
        self.ui.ShearResultEdit.setText(str(V)+"Kn")
        self.ui.MResultEdit.setText(str(M)+"KN.m")
         
          

def main():
    app=QApplication(sys.argv)
    win=ShearKey()
    win.ui.show()
    app.exec_()
    
if __name__ == '__main__':
    main()
      
