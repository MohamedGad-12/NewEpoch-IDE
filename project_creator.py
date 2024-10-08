from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFormLayout, QLineEdit, QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt
import os
import sys


class Create_Action(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Project and File Name")
        self.setFixedSize(450,130)
        self.form = QFormLayout(self)
        self.form.setVerticalSpacing(20) # set the vertical spacing to 20 pixels
        self.project_name = QLineEdit()
        self.file_name = QLineEdit()
        self.hbox = QHBoxLayout()
        self.create_btn = QPushButton("Create")
        self.create_btn.clicked.connect(self.createProject)
        self.close_btn = QPushButton("Close")
        self.close_btn.clicked.connect(self.close)
        self.hbox.addWidget(QWidget())
        self.hbox.addWidget(self.create_btn)
        self.hbox.addWidget(QWidget())
        self.hbox.addWidget(self.close_btn)
        self.form.addRow("Project Name:", self.project_name)
        self.form.addRow("File Name:", self.file_name)
        self.form.addRow(self.hbox)
        self.relative_path = None
        #self.show()

     
    def show_create(self, real_path):
         self.show()
         self.relative_path = real_path
         
    def Create_Makefile(self,project_name):
        f = open(self.relative_path+"\\"+project_name+"\\"+"Makefile", "x") # create a new file
        f.write("#Eng. Mohamed Gamal\n")
        f.write("CC=gcc\nCFLAGS=-w -Werror -Wall\nDeg=-g\nINCS=-I .\nLIBS=\nSRC = $(wildcard *.c)\nOBJ = $(SRC:.c=.o)\nAs = $(wildcard *.s)\nAsOBJ = $(As:.s=.o)\nFile=Output\n\n\n")
        f.write("all: $(File) \n%.o: %.c\n\t$(CC).exe -c $(Deg) $(INCS) $(CFLAGS) $< -o $@ \n \n \n$(File): $(OBJ) $(AsOBJ)\n\t$(CC) $(LIBS) $< -o $@ \n\t@echo '============Bulid_Done============' \n")
        f.write("\n\ndebug: $(File).elf\n\t$(CC)strip.exe -g -S -d $<\n\t@echo '============rm_degig_Done============' \n ")
        f.write("\n\nclean:\n\trm *.o *.exe\n\t@echo @echo '============rm_all============' \n ")
        f.close() # close the fil
             

    def createProject(self):
        # get the project name and file name from the line edits
        project_name = self.project_name.text()
        
        if project_name == '':
            QMessageBox(QMessageBox.Critical, "Error", "Invalid Project Name", QMessageBox.Ok, self).exec()
        else:
            file_name = self.file_name.text()

            if file_name == '':
                QMessageBox(QMessageBox.Critical, "Message", "Invalid File Name", QMessageBox.Ok, self).exec()
            else:    
                name, ext = os.path.splitext(file_name)
                if ext != '.c':
                    QMessageBox(QMessageBox.Critical, "Message", "Invalid File Extension ", QMessageBox.Ok, self).exec()
                else:
                    os.mkdir(self.relative_path+"\\"+project_name)
                    f = open(self.relative_path+"\\"+project_name+"\\"+file_name, "x") # create a new file
                    self.Create_Makefile(project_name)
                    f.close() # close the fil

                    self.close()
                




    '''
if __name__ == "__main__":
    app = QApplication([])
    ex = Create_Action()
    app.setStyle('Fusion')
    app.exec()
    '''