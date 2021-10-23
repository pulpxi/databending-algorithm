import random
import string
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *

textareaG = QPlainTextEdit
picturelabel = QLabel

delay = 1
scale = 1

root = 0
pixels_x = 0
pixels_y = 0

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("loadui.ui", self)
        # Components
        global textareaG, picturelabel
        self.label = self.findChild(QLabel, "label")
        picturelabel = self.label
        self.textarea = self.findChild(QPlainTextEdit, "plainTextEdit")
        textareaG = self.textarea
        self.runbutton = self.findChild(QPushButton, "pushButton")
        self.runbutton.clicked.connect(self.createImage)
        self.glitchamountfield = self.findChild(QLineEdit, "lineEdit")
        self.glitchlengthfield = self.findChild(QLineEdit, "lineEdit_2")
        self.show()


    def setpictureonlabel(self):
        pixmap = QPixmap("glitchImage.jpg")
        picturelabel.setPixmap(pixmap)

    def createImage(self):
        self.createGlitch()

    def createGlitchImage(self, imagePrefabPath, newImageName):
        with open(imagePrefabPath, 'rb') as old:
            code = old.read()
            code_len = len(code)
            for x in range(int(self.glitchamountfield.text())):
                rand_index = random.randint(200, code_len)
                insert_into_code = ''.join(
                    random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in
                    range(int(self.glitchlengthfield.text())))
                split_code = code[:rand_index] + insert_into_code.encode() + code[rand_index + len(insert_into_code):]
                code = split_code
                code_len = len(code)
            with open(newImageName, 'wb') as new:
                new.write(split_code)
                textareaG.setPlainText(str(split_code))

    def createGlitch(self):
        global root, pixels_x, pixels_y
        global UIWindow
        self.createGlitchImage('orgImage.jpg', 'glitchImage.jpg')
        print("glitch created!")
        try:
            self.setpictureonlabel()
            print("image set")
        except:
            print("cant set image")







def main():
    app = QApplication(sys.argv)
    UIWindow = UI()
    app.exec_()

if __name__ == "__main__":
    main()
