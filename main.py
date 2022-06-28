from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QPlainTextEdit,
                                QVBoxLayout, QWidget)
from PySide6.QtCore import QProcess
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.btn = QPushButton("Execute")
        self.btn.pressed.connect(self.start_process)
        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)

        l = QVBoxLayout()
        l.addWidget(self.btn)
        l.addWidget(self.text)

        w = QWidget()
        w.setLayout(l)

        self.setCentralWidget(w)

    def message(self, s):
        self.text.appendPlainText(s)

    def start_process(self):
        self.message("Executing process.")
        p =QProcess()
        p.start("python3, ['dummy_script.py']")
        # p.start("pythpon3, ['fibonacci.py']")
        pass

app = QApplication(sys.argv)

w = MainWindow()
w.show()

app.exec_()