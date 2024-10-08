from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFormLayout, QLineEdit, QHBoxLayout, QMessageBox, QComboBox, QFileDialog
from PyQt5.QtCore import Qt
import os
import sys
from ide_application import MainWindow


class Create_Action(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle("Environment WorkSpace")
        self.setFixedSize(450,90)

        self.form = QFormLayout(self)
        self.form.setVerticalSpacing(20) # set the vertical spacing to 20 pixels
        
        self.WorkSpace = QComboBox()
        self.WorkSpace_arr = []
        self.WorkSpace.addItem(os.getcwd())
        self.WorkSpace_arr.append(os.getcwd())
        #self.comboBox.activated.connect(self.Mode_Selection)

        self.hbox = QHBoxLayout()

        self.create_btn = QPushButton("OK")
        self.create_btn.clicked.connect(self.BuildEnvir)

        self.close_btn = QPushButton("Close")
        self.close_btn.clicked.connect(lambda: sys.exit())

        self.select_btn = QPushButton("Select")
        self.select_btn.clicked.connect(self.SelectEnv)

        self.hbox.addWidget(QWidget())
        self.hbox.addWidget(self.create_btn)
        self.hbox.addWidget(QWidget())
        self.hbox.addWidget(self.select_btn)
        self.hbox.addWidget(QWidget())
        self.hbox.addWidget(self.close_btn)


        self.IDE = MainWindow()

        self.form.addRow("WorkSpace:", self.WorkSpace)
        self.form.addRow(self.hbox)
        self.show()


    def SelectEnv(self):
        flag = 1
        path = os.path.join(os.getcwd(), "")
        Selected_path = str(QFileDialog.getExistingDirectory())
        Correct_Selected_Path = Selected_path.replace("/","\\") #chr(92)
        if Correct_Selected_Path != "":
            for i in range(len(self.WorkSpace_arr)):
                if Correct_Selected_Path == str(self.WorkSpace_arr[i]):
                    flag = 0
                    self.WorkSpace.setCurrentText(Correct_Selected_Path)
            if flag == 1:
                self.WorkSpace_arr.append(Correct_Selected_Path)
                self.WorkSpace.insertItem(0,Correct_Selected_Path)
                self.WorkSpace.setCurrentText(Correct_Selected_Path)


    def BuildEnvir(self):
        # get the project name and file name from the line edits
        WorkSpace = self.WorkSpace.currentText()
        if not(os.path.exists(WorkSpace)): # check if the path exists
            QMessageBox(QMessageBox.Critical, "Error", "Invalid Path", QMessageBox.Ok, self).exec()
        else:
            if not(os.path.exists(WorkSpace+"\\"+"NE_Environment")):
                os.mkdir(WorkSpace+"\\"+"NE_Environment")
                if not(os.path.exists(WorkSpace+"\\"+"NE_Environment\\"+"NE_MetaData")):
                    os.mkdir(WorkSpace+"\\"+"NE_Environment\\"+"NE_MetaData")
                if not(os.path.exists(WorkSpace+"\\"+"NE_Environment\\"+"NE_WorkSpace")):
                    os.mkdir(WorkSpace+"\\"+"NE_Environment\\"+"NE_WorkSpace")
            else:
                if not(os.path.exists(WorkSpace+"\\"+"NE_Environment\\"+"NE_MetaData")):
                    os.mkdir(WorkSpace+"\\"+"NE_Environment\\"+"NE_MetaData")
                if not(os.path.exists(WorkSpace+"\\"+"NE_Environment\\"+"NE_WorkSpace")):
                    os.mkdir(WorkSpace+"\\"+"NE_Environment\\"+"NE_WorkSpace")
                        
        self.close()
        self.IDE.window_show(WorkSpace+"\\"+"NE_Environment\\"+"NE_WorkSpace")



if __name__ == "__main__":
    app = QApplication([])
    ex = Create_Action()
    app.setStyle('Fusion')
    app.exec()