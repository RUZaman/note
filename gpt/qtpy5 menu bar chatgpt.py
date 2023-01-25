#this code work

import sys

from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("My Qtpy5 Program")
        self.setGeometry(100, 100, 600, 400)

        # Create a central widget and layout
        self.widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.widget)
        self.layout = QtWidgets.QVBoxLayout(self.widget)

        # Create input field
        self.input_field = QtWidgets.QLineEdit(self.widget)
        self.layout.addWidget(self.input_field)

        # Create buttons
        self.button1 = QtWidgets.QPushButton("Button 1", self.widget)
        self.button2 = QtWidgets.QPushButton("Button 2", self.widget)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)

        # Create drop-down menu bar
        self.menu_bar = QtWidgets.QMenuBar(self)
        self.menu = QtWidgets.QMenu("Menu", self.menu_bar)
        self.menu_bar.addMenu(self.menu)
        self.menu.addAction("Option 1")
        self.menu.addAction("Option 2")
        self.menu.addAction("Option 3")
        self.setMenuBar(self.menu_bar)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())