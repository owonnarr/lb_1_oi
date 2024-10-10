import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from math import exp

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Обчислення рівняння')
        self.setGeometry(500, 300, 600, 400)

        mainLayout = QVBoxLayout()

        self.label_x = QLabel('Введіть значення x:')
        mainLayout.addWidget(self.label_x)

        self.entry_x = QLineEdit(self)
        mainLayout.addWidget(self.entry_x)

        self.button_calculate = QPushButton('Обчислити', self)
        self.button_calculate.clicked.connect(self.do_calculate)
        mainLayout.addWidget(self.button_calculate)

        self.label_result = QLabel('')
        mainLayout.addWidget(self.label_result)

        self.setLayout(mainLayout)

    def do_calculate(self):
        try:
            x = int(self.entry_x.text())
            a = 1.25  # Середнє між 0.8 та 1.7
            y = (x + 1) * exp(a / (x + 1))
            self.label_result.setText(f'y({x}) = {y:.4f}')
        except ValueError:
            self.label_result.setText("Будь ласка, введіть коректне число")

app = QApplication(sys.argv)
ex = App()
ex.show()
sys.exit(app.exec_())