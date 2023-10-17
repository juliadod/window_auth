import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QGridLayout, QSizePolicy
from PyQt6.QtGui import QIcon


class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        label = QLabel('Main App', parent=self)


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')
        self.setWindowIcon(QIcon(''))
        self.window_width, self.window_height = 600, 180
        self.setFixedSize(self.window_width, self.window_height)

        layout = QGridLayout()
        self.setLayout(layout)

        labels = {}
        self.lineEdits = {}

        labels['Username'] = QLabel('Username')
        labels['Password'] = QLabel('Password')
        labels['Username'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        labels['Password'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.lineEdits['Username'] = QLineEdit()
        self.lineEdits['Password'] = QLineEdit()
        self.lineEdits['Password'].setEchoMode(QLineEdit.EchoMode.Password)

        layout.addWidget(labels['Username'], 0, 0, 1, 1)
        layout.addWidget(self.lineEdits['Username'], 0, 1, 1, 3)

        layout.addWidget(labels['Password'], 1, 0, 1, 1)
        layout.addWidget(self.lineEdits['Password'], 1, 1, 1, 3)

        button_login = QPushButton('&Log In')
        layout.addWidget(button_login, 2, 3, 1, 1)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 25px;
        }
        QLineEdit {
            height: 200px;
        }
    ''')

    loginWindow = LoginWindow()
    loginWindow.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window...')