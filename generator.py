import string
from  PyQt5.QtWidgets import  QMainWindow, QApplication,QLabel,QPushButton,QLineEdit,QCheckBox,QMessageBox
from PyQt5 import uic
import sys
import random
from PyQt5.QtCore import *
from PyQt5.QtGui import *
class UI(QMainWindow):
    def __init__(self,settings):
        super(UI,self).__init__()
        uic.loadUi('generator.ui',self)
        self.label = self.findChild(QLabel,"label")
        self.length_label = self.findChild(QLabel,"label_2")
        self.upper_label = self.findChild(QLabel, "label_3")
        self.lower_label = self.findChild(QLabel, "label_4")
        self.number_label = self.findChild(QLabel, "label_5")
        self.symbol_label = self.findChild(QLabel, "label_6")
        self.pass_text = self.findChild(QLineEdit, "pass_generate")
        self.length_text = self.findChild(QLineEdit, "length")
        self.copy_btn = self.findChild(QPushButton, "copy_btn")
        self.generate_btn = self.findChild(QPushButton, "generate_btn")
        self.upper_check = self.findChild(QCheckBox, "upper_check")
        self.lower_check = self.findChild(QCheckBox, "lower_check")
        self.number_check = self.findChild(QCheckBox, "number_check")
        self.symbol_check = self.findChild(QCheckBox, "symbol_check")
        self.settings = settings
        self.PASSWORD_MIN_LENGTH = 4
        self.PASSWORD_MAX_LENGTH = 30
        self.show()

        self.generate_btn.clicked.connect(self.generator)
        self.copy_btn.clicked.connect(self.clipboard)

    def clipboard(self):
        cb=QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(self.pass_text.text(),mode=cb.Clipboard)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle('Copy to clipboard')
        msg.setText('Your password Has Been copied')
        x = msg.exec_()
    def get_settings(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle('Warning')
        if self.length_text.text() == "":
            msg.setText('Please enter  length of password')
            x = msg.exec_()
        elif (self.PASSWORD_MIN_LENGTH <= int(self.length_text.text()) <= self.PASSWORD_MAX_LENGTH):
            self.settings['length'] = self.length_text.text()
        else:
            msg.setText('password length should be between 4 and 30')
            x = msg.exec_()
        self.settings['upper'] = self.upper_check.isChecked()
        self.settings['lower'] = self.lower_check.isChecked()
        self.settings['number'] = self.number_check.isChecked()
        self.settings['symbol'] = self.symbol_check.isChecked()
        choices = list(filter(lambda x: self.settings[x], ['upper', 'lower', 'number', 'symbol']))


    def get_upper_letter(self):
        """Return random uppercase letter"""
        return random.choice(string.ascii_uppercase)

    def get_lower_letter(self):
        """Return random lowercase letter"""
        return random.choice(string.ascii_lowercase)

    def get_number_letter(self):
        """Return random number"""
        return random.choice(string.digits)

    def get_symbol_letter(self):
        """Return random symbol"""
        return random.choice(string.punctuation)

    def get_random_char(self,choices):
        choice = random.choice(choices)
        if choice == 'upper':
            return self.get_upper_letter()
        if choice == 'lower':
            return  self.get_lower_letter()
        if choice == 'number':
            return  self.get_number_letter()
        if choice == 'symbol':
            return  self.get_symbol_letter()

    def generator(self):
        """Return new password"""
        new_password = ''
        #Get settings
        self.get_settings()
        # Select True settings
        choices = list(filter(lambda x:self.settings[x], ['upper', 'lower', 'number','symbol']))
        for i in range(int(self.settings['length'])):
            new_password += self.get_random_char(choices)
        self.pass_text.setText(new_password)
        self.length_text.setText("")
        self.upper_check.setChecked(False)
        self.lower_check.setChecked(False)
        self.number_check.setChecked(False)
        self.symbol_check.setChecked(False)
        self.settings['upper'], self.settings['lower'], self.settings['number'], self.settings['symbol'] = False, False, True, False


if __name__ == '__main__':
    settings = {
        'upper' : False,
        'lower': False,
        'number': True,
        'symbol': False,
        'length': 0
    }
    app=QApplication(sys.argv)
    UIWindow = UI(settings)
    app.exec_()

