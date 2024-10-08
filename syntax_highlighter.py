import sys
from PyQt5.QtWidgets import QApplication, QTextEdit
from PyQt5.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor

class KeywordHighlighter(QSyntaxHighlighter):
    # A custom syntax highlighter class that highlights keywords in a QTextEdit

    def __init__(self, parent=None):
        # Initialize the base class and define the keywords and format
        super().__init__(parent)
        self.c_keywords = ["restrict","case","goto","inline","auto","register", "signed","unsigned","static","volatile","typedef","void","const","extern"]
        self.keywords_round = ["main","if", "else","for", "while", "sizeof","switch","printf","scanf"]
        self.keywords_ciruly = ["union", "struct","do","else","enum"]
        self.keywords_data = ["char", "float","int","double","long","short"]
        self.keywords_preprocessing = ["#define", "#undef", "#include", "#ifdef", "#ifndef","#if", "#else", "#elif", "#endif", "#line","#error", "#pragma"]
        self.keywords_special = ["default","continue","break","return"]
        self.format = QTextCharFormat()
        self.format.setFontPointSize(12) # set font size to 14
        self.format.setForeground(QColor(230,100,100))
        self.format_0 = QTextCharFormat() 
        self.format_0.setFontPointSize(12) # set font size to 14
        self.format_0.setForeground(QColor("blue"))

    def highlightBlock(self, text):
        # Override the highlightBlock method to apply the format to the keywords
        for word in self.keywords_data:
            index = text.find(word)
            while index >= 0:
                length = len(word)
                if (index == 0 or text[index-1] in " ({" ) and (index + length == len(text) or text[index + length] in ' *'):
                    self.setFormat(index, length, self.format)
                index = text.find(word, index + length)

        for word in self.keywords_preprocessing:
            index = text.find(word)
            while index >= 0:
                length = len(word)
                if word == "#include":
                    if (index == 0 or text[index-1] in ' ({' ) and (index + length == len(text) or text[index + length] in ' "<'):
                        self.setFormat(index, length, self.format_0)
                    index = text.find(word, index + length)
                else:
                    if (index == 0 or text[index-1] in " ({" ) and (index + length == len(text) or text[index + length].isspace()):
                        self.setFormat(index, length, self.format_0)
                    index = text.find(word, index + length)

        for word in self.keywords_round:
            index = text.find(word)
            while index >= 0:
                length = len(word)
                if word == "main":
                    if (index == 0 or text[index-1] in " ({" ) and (index + length == len(text) or text[index + length] in ' ('):
                        self.setFormat(index, length, self.format_0)
                    index = text.find(word, index + length)
                else:
                    if (index == 0 or text[index-1] in " ({" ) and (index + length == len(text) or text[index + length] in ' ('):
                        self.setFormat(index, length, self.format)
                    index = text.find(word, index + length)

        for word in self.keywords_ciruly:
            index = text.find(word)
            while index >= 0:
                length = len(word)
                if (index == 0 or text[index-1] in " ({" ) and (index + length == len(text) or text[index + length] in ' {'):
                    self.setFormat(index, length, self.format)
                index = text.find(word, index + length)

        for word in self.keywords_special:
            index = text.find(word)
            while index >= 0:
                length = len(word)
                if word == "default":
                    if (index == 0 or text[index-1] in ' ({' ) and (index + length == len(text) or text[index + length] in ' :'):
                        self.setFormat(index, length, self.format)
                    index = text.find(word, index + length)
                else:
                    if (index == 0 or text[index-1] in " ({" ) and (index + length == len(text) or text[index + length] in ' ;'):
                        self.setFormat(index, length, self.format)
                    index = text.find(word, index + length)

        for word in self.c_keywords:
            index = text.find(word)
            while index >= 0:
                length = len(word)
                if word == "restrict":
                    if (index == 0 or text[index-1] in ' ({*' ) and (index + length == len(text) or text[index + length] in ' '):
                        self.setFormat(index, length, self.format)
                    index = text.find(word, index + length)
                else:
                    if (index == 0 or text[index-1] in " ({" ) and (index + length == len(text) or text[index + length] in ' '):
                        self.setFormat(index, length, self.format)
                    index = text.find(word, index + length)

                



