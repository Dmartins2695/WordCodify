from random import shuffle
import random
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap,QImage
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.uic import loadUi
import sys, getopt




class ExampleApp(QtWidgets.QMainWindow,):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)

class MainPage(QMainWindow):
    def __init__(self):
        super(MainPage, self).__init__()
        loadUi('WordCodify.ui', self)
        self.btnGen.clicked.connect(self.generate_password)

    def shuffle_alphabet():
        word = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890#$%&abcdefghijklmnopqrstuvwxyz1234567890#$%&'
        word = list(word)
        shuffle(word)
        result = ','.join(word)
        result = list(result)
        i = 1
        while i < len(result):
            result.pop(i)
            i=i+3
        result=''.join(result)
        return result.split(',')

    def get_word_map(result):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890#$%&"
        alphabet = list(alphabet)
        myMap= dict.fromkeys(alphabet)
        j=0
        for str in myMap.keys():
            myMap[str] = result[j]
            j=j+1    
        return myMap

    def get_new_pass(password,myMap):
        passArray = [char for char in password]
        shuffle(passArray)
        count=len(password)
        if(count<8):
            while count<8:
                char=random.randint(65, 90)
                passArray.append(chr(char))
                count+=1
        k=0
        count=len(password)
        while k < count:
            password=password.replace(passArray[k],myMap.get(passArray[k]))
            k=k+1

        return password

    def generate_password(self):
        charToStrip=" !\"\'()[]{\}*+´-./:;=,><?@^~_`|"
        password = self.inputWord.text()
        password=password.upper()
        password=password.strip(charToStrip)
        newpassword= MainPage.get_new_pass(password,MainPage.get_word_map(MainPage.shuffle_alphabet()))
        self.showNewPass.setText("Your Password: "+newpassword)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainPage()
    widget.show()
    sys.exit(app.exec_())