from syntax_highlighter import KeywordHighlighter
from project_creator import Create_Action
import sys
import os
import time
import subprocess
from PyQt5 import Qt, QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QTimer
from PyQt5.QtWidgets import QGridLayout, QPlainTextEdit, QMessageBox, QApplication, QWidget, QPushButton, QFileDialog, QTextEdit, QVBoxLayout, QTabWidget, QHBoxLayout
from PyQt5.QtWidgets import QListView, QComboBox, QLabel, QMainWindow, QSplitter, QListWidget, QFileSystemModel, QTreeView, QLineEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.array_terminal_and_consloe = []

        self.setWindowTitle("New Epoch")

        # Create the main widget
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        # Create the main layout
        main_layout = QVBoxLayout()
        self.main_widget.setLayout(main_layout)

        self.pushButton = QPushButton('Create')
        self.pushButton.setGeometry(10, 30, 50, 25)
        self.pushButton.clicked.connect(self.Create)
        self.Create_UI = Create_Action()
        
        self.pushButton_2 = QPushButton('Open')
        self.pushButton_2.setGeometry(65, 30, 50, 25)
        self.pushButton_2.clicked.connect(self.open_files)

        self.pushButton_3 = QPushButton('Save')
        self.pushButton_3.setGeometry(115, 30, 50, 25)
        self.pushButton_3.clicked.connect(self.save)

        self.pushButton_4 = QPushButton('Run')
        self.pushButton_4.setGeometry(170, 30, 50, 25)
        self.pushButton_4.clicked.connect(self.Run)

        self.pushButton_5 = QPushButton('Bulid')
        self.pushButton_5.setGeometry(225, 30, 50, 25)
        self.pushButton_5.clicked.connect(self.Bulid)

        self.pushButton_6 = QPushButton('Clean')
        self.pushButton_6.setGeometry(275, 30, 50, 25)
        self.pushButton_6.clicked.connect(self.clean)

        self.pushButton_7 = QPushButton('Console')
        self.pushButton_7.setGeometry(330, 30, 50, 25)
        self.pushButton_7.clicked.connect(self.open_Console)

        self.pushButton_8 = QPushButton('Terminal')
        self.pushButton_8.setGeometry(370, 30, 50, 25)
        self.pushButton_8.clicked.connect(self.open_terminal)

        self.pushButton_9 = QPushButton('Exit')
        self.pushButton_9.setGeometry(425, 30, 50, 25)
        self.pushButton_9.clicked.connect(lambda: sys.exit())


        self.listView = QTreeView()
        self.model = QFileSystemModel()
        self.relative_envir_path = None
        #self.model.setRootPath(relative_envir_path)
        #self.model.setRootPath("E:\\Own_IDE\\tests\\Environment")
        self.listView.setModel(self.model)
        # hide all columns except the first one
        for i in range(1, self.listView.model().columnCount()):
            self.listView.hideColumn(i)
        #self.listView.setRootIndex(self.model.index("E:\\Own_IDE\\tests\\Environment"))
        self.listView.doubleClicked.connect(self.do_action)
        self.listView.setGeometry(10, 80, 71, 261)
        self.listView.setObjectName("listView")


        self.comboBox = QComboBox()
        self.comboBox.setGeometry(10, 370, 60, 20)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Light")
        self.comboBox.addItem("Dark")
        self.comboBox.activated.connect(self.Mode_Selection)


        self.label = QLabel('Mode Selection')
        self.label.setGeometry(10, 350, 47, 13)
        self.label.setObjectName("label")

        
        self.Terminal_text = QTextEdit()
        self.line_edit = QLineEdit()
        # Set the placeholder text
        self.line_edit.setPlaceholderText("Write Your Command Here")
        self.terminal_contaniter = QWidget()
        self.Terminal_layout = QVBoxLayout()
        self.Terminal_layout.addWidget(self.line_edit)
        self.Terminal_layout.addWidget(self.Terminal_text)
        self.terminal_contaniter.setLayout(self.Terminal_layout)

        self.Console_text = QTextEdit()

        
        self.tab_widget = QTabWidget()
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.close_tab)
        #self.font_details = KeywordHighlighter(self.tab_widget.document())

        self.terminal_text_open = False # initialize the flag as False
        self.Console_text_open = False  # initialize the flag as False
        self.Terminal = QTabWidget()
        self.Terminal.setTabsClosable(True)
        self.Terminal.tabCloseRequested.connect(self.close_Terminal_and_Console)


        # Create the top layout for the buttons
        top_layout = QHBoxLayout()
        # Add some buttons to the top layout
        top_layout.addWidget(self.pushButton)
        top_layout.addWidget(self.pushButton_2)
        top_layout.addWidget(self.pushButton_3)
        top_layout.addWidget(self.pushButton_4)
        top_layout.addWidget(self.pushButton_5)
        top_layout.addWidget(self.pushButton_6)
        top_layout.addWidget(self.pushButton_7)
        top_layout.addWidget(self.pushButton_8)
        top_layout.addWidget(self.pushButton_9)


        self.mode_layout_Widget = QWidget()
        mode_layout = QVBoxLayout(self.mode_layout_Widget)
        mode_layout.addWidget(self.label)
        mode_layout.addWidget(self.comboBox)
        mode_layout.addWidget(QLabel(''))
        mode_layout.addWidget(QLabel(''))
        mode_layout.addWidget(QLabel(''))


        left_splitter = QSplitter()
        #left_splitter.setSizes([1,4])
        left_splitter.setOrientation(QtCore.Qt.Vertical)
        left_splitter.addWidget(self.listView)
        left_splitter.addWidget(self.mode_layout_Widget)


        # Create the bottom splitter for the list view and the text edits
        bottom_splitter = QSplitter()
        # Add a list widget to the bottom splitter
        bottom_splitter.addWidget(left_splitter)
        # Create another splitter for the text edits
        text_splitter = QSplitter()
        text_splitter.setOrientation(QtCore.Qt.Vertical)
        # Add two text edits to the text splitter
        text_splitter.addWidget(self.tab_widget)
        text_splitter.addWidget(self.Terminal)
        # Add the text splitter to the bottom splitter
        bottom_splitter.addWidget(text_splitter)


        bottom_splitter.setSizes([100,800])
        bottom_splitter.setStretchFactor(0, 1) # Set the stretch factor of the left part to 1
        bottom_splitter.setStretchFactor(1, 4) # Set the stretch factor of the right part to 4
        text_splitter.setSizes([400,100])
        text_splitter.setStretchFactor(0, 1) # Set the stretch factor of the left part to 1
        text_splitter.setStretchFactor(1, 4) # Set the stretch factor of the right part to 4
        left_splitter.setSizes([465,100])
        left_splitter.setStretchFactor(0, 1) # Set the stretch factor of the left part to 1
        left_splitter.setStretchFactor(1, 4) # Set the stretch factor of the right part to 4


        # Add the sub-layouts and widgets to the main layout
        main_layout.addLayout(top_layout)
        main_layout.addWidget(bottom_splitter)


    def window_show(self, real_path):
            self.relative_envir_path = real_path
            self.model.setRootPath(self.relative_envir_path)
            self.listView.setRootIndex(self.model.index(self.relative_envir_path))
            self.show()


    def Create(self):
        self.Create_UI.show_create(self.relative_envir_path)


    def do_action(self,index):
        # get the file path from the model index
        file_path = self.model.filePath(index)
        # do something with the file path
        try:
            self.open_file(file_path)    
        except:
            pass    


    def Mode_Selection(self):
        if self.comboBox.currentText() == 'Dark':
            self.main_widget.setStyleSheet("background-color: rgb(26,26,26); color: white;")
        else:
            self.main_widget.setStyleSheet('')
        


    #file_names, types = QFileDialog.getSaveFileName(self, 'Save Files', '', '*.c;; *.h')
    def save(self):
        self.open_Console()
        index = self.tab_widget.currentIndex()   # get the current tab index
        name = self.tab_widget.tabText(index)    # get the current tab
        data = self.tab_widget.widget(index)     # get the current tab
        if name != '':
            direc = os.path.dirname(name)
            if direc != '':
                with open(name, 'w') as file:
                    file.write(data.toPlainText())
                    #QMessageBox.information(self, "Information", "Save Done", QMessageBox.Ok)
                    self.Console_text.setText("The file is saved")
            else: #This Else Need to Be Tested
                file_name, types = QFileDialog.getSaveFileName(self, 'Save File', '', '*.c;; *.h')
                if file_name != '':
                    with open(name, 'w') as file:
                        file.write(data.toPlainText())
                        self.Console_text.setText("The file is saved")
                    #QMessageBox.information(self, "Information", "Save Done", QMessageBox.Ok)
                else:
                    self.Console_text.setText("File Save Canceled")
                    return 0
        else:
            self.Console_text.setText("File Save Error")
            return 0
        


    def clean(self):
        self.open_Console()
        index = self.tab_widget.currentIndex() # get the current tab index
        name = self.tab_widget.tabText(index) # get the current tab name
        if name != '': 
            direc = os.path.dirname(name)
            os.chdir(direc)
            try:
                output = subprocess.check_output(["make", "clean"])
                Data = output.decode("utf-8")
                self.Console_text.setText(Data)
            except subprocess.CalledProcessError as e:
                self.Console_text.setText("Project already is cleaned")
        else:
            #consloe error
            self.Console_text.setText("Clean Process is faild")
            return 0



    def Bulid(self):
        self.open_Console()
        if self.clean() == 0:
            self.Console_text.setText("Bulid Process is faild")
            return 0
        if self.save() == 0:
            self.Console_text.setText("Bulid Process is faild")
            return 0
        index = self.tab_widget.currentIndex() # get the current tab index
        name = self.tab_widget.tabText(index) # get the current tab name
        if name != '': 
            direc = os.path.dirname(name)
            os.chdir(direc)
            try:
                output = subprocess.check_output(["make", "all"])
                Data = output.decode("utf-8")
                self.Console_text.setText(Data)
            except subprocess.CalledProcessError as e:
                self.Console_text.setText("Project already is Built")
        else:
            #consloe error
            self.Console_text.setText("Bulid Process is faild")
            return 0



    def Run(self):
        self.open_Console()
        if self.Bulid() == 0:
            self.Console_text.setText("Run Process is faild")
        else:
            # Run a command and raise an exception if it fails
            try:
                if os.path.exists("Output.exe"): 
                    result = subprocess.run (["Output.exe"], capture_output=True, check=True)
                    # The command was successful, print the output
                    self.Console_text.setText(result.stdout.decode())
                else:
                    # Print an error message
                    self.Console_text.setText("Output.exe not found")    
            except subprocess.CalledProcessError as e:
                # The command failed, print the error
                self.Console_text.setText(e.stderr.decode())

    
    def open_files(self):
        file_names, types = QFileDialog.getOpenFileNames(self, 'Open Files', '', '*')
        if file_names:
            for file_name in file_names:
                self.open_file(file_name)


    def open_file(self, file_name):
        with open(file_name, 'r') as f:
            content = f.read()
            text_edit = QTextEdit()
            text_edit.setReadOnly(False)
            text_edit.setText(content)
            self.font_details = KeywordHighlighter(text_edit.document())
            font = text_edit.font() # get current font
            font.setPointSize(12) # change its size
            text_edit.setFont(font) # set font
            index = self.tab_widget.addTab(text_edit, file_name)
            icon = QIcon('file_icon.png') # replace with your own icon file
            self.tab_widget.setTabIcon(index,icon)
            self.tab_widget.setCurrentIndex (index)


    def close_tab(self, index):
        self.tab_widget.removeTab(index)



    # Define a function to run commands and print their output
    def Terminal_DOne(self,command):
        # Use os.popen() to execute the command and get a file object
        output = os.popen(command)
        # Read the output from the file object and print it
        self.Terminal_text.append(output.read())
        # Close the file object
        output.close()
            
   
    #Define a function to run commands and print their output
    #@pyqtSlot()
    def open_terminal(self):
        if not self.terminal_text_open:
            self.Terminal_text.setReadOnly(True)
            self.Terminal_text.setText(">>> "+os.getcwd()+"\n")
            font = self.Terminal_text.font() # get current font
            font.setPointSize(12) # change its size
            self.Terminal_text.setFont(font) # set fon
            font_line = self.line_edit.font() # get current font
            font_line.setPointSize(12) # change its size
            self.line_edit.setFont(font_line) # set fon
            # Connect the returnPressed signal of the QLineEdit object to the read_text slot function
            self.line_edit.returnPressed.connect(self.read_text)
            index = self.Terminal.addTab(self.terminal_contaniter, "Run Terminal")
            icon = QIcon('file_icon.png') # replace with your own icon file
            self.Terminal.setTabIcon(index, icon)
            self.terminal_text_open = True
            self.Terminal.setCurrentIndex(index)
            self.array_terminal_and_consloe.append('terminal')
        else:
            if self.array_terminal_and_consloe[0] == 'terminal':
                self.Terminal.setCurrentIndex(0)
            else:
                self.Terminal.setCurrentIndex(1)

    # Define a custom slot function that will read the text from the QLineEdit widget and run it as a command
    @pyqtSlot()
    def read_text(self):
        # Prompt the user for a command
        self.Terminal_text.clear()
        self.Terminal_text.setText(">>> "+os.getcwd()+"\n")
        command = self.line_edit.text()
        # Check if the command is 'exit'
        if command == "cls":
            # Break the loop and end the program
            self.Terminal_text.clear()
            self.Terminal_text.setText(">>> "+os.getcwd()+"\n")
        # Check if the command starts with 'cd'
        elif command.startswith("cd"):
            # Get the path after 'cd'
            path = command[3:]
            # Try to change the working directory to that path
            try:
                os.chdir(path)
                self.Terminal_text.clear()
                self.Terminal_text.setText(">>> "+os.getcwd()+"\n")
            # Handle any errors
            except Exception as e:
                self.Terminal_text.append(str(e))
        # Otherwise, run the command and print the output
        else:
            self.Terminal_DOne(command)
        # Add a delay of 1 second between each command
        #time.sleep(0.1)
        self.line_edit.clear()             



    def open_Console(self):
        if not self.Console_text_open:
            self.Console_text.setReadOnly(True)
            self.Console_text.setText("")
            font = self.Console_text.font() # get current font
            font.setPointSize(12) # change its size
            self.Console_text.setFont(font) # set fon
            index = self.Terminal.addTab(self.Console_text, "Run Console")
            icon = QIcon('file_icon.png') # replace with your own icon file
            self.Terminal.setTabIcon(index, icon)
            self.Console_text_open = True
            self.Terminal.setCurrentIndex(index)
            self.array_terminal_and_consloe.append('console')
        else:
            if self.array_terminal_and_consloe[0] == 'console':
                self.Terminal.setCurrentIndex(0)
            else:
                self.Terminal.setCurrentIndex(1)


    def close_Terminal_and_Console(self, index):
        if self.Terminal.tabText(index) == "Run Terminal": # check if the closed tab is the terminal text tab
            self.terminal_text_open = False # reset the flag to False when closing the tab
            self.Terminal.removeTab(index)
        if self.Terminal.tabText(index) == "Run Console": # check if the closed tab is the terminal text tab
            self.Console_text_open = False # reset the flag to False when closing the tab
            self.Terminal.removeTab(index)


if __name__ == "__main__":
    app = QApplication([])
    app.setStyle('Fusion')
    #print(PyQt5.QtWidgets.QStyleFactory.keys())                          
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())



'''
# Create an application instance
app = QApplication([])

# Create and show the main window
window = MainWindow()
window.show()

# Run the application loop
app.exec_()
'''