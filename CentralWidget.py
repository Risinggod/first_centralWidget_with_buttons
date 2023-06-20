from PyQt6.QtWidgets import QWidget, QSlider, QTextBrowser, QGridLayout, QPushButton, QApplication, QLabel
from PyQt6.QtCore import pyqtSlot, Qt





class CentralWidget(QWidget):
    def __init__(self, parent=None, QT=None):
        super(CentralWidget, self).__init__(parent)

        self.text_edit = QTextBrowser(self)
        self.text_edit.setText("Started app")


        self.slider = QSlider(self)
        self.slider.setRange(50, 75)
        self.slider.setValue(60)
        self.slider.valueChanged.connect(self.append_text)
        self.slider.setOrientation(Qt.Orientation.Horizontal)

        self.pushbutton = QPushButton(self)
        self.pushbutton.show()
        self.pushbutton.setText("Schließen")
        self.pushbutton.clicked.connect(QApplication.instance().quit)

        layout = QGridLayout(self)
        layout.addWidget(self.pushbutton, 1, 1)
        layout.addWidget(self.slider, 4, 2)
        layout.addWidget(self.text_edit, 3, 2)
        layout.addWidget(QLabel("Slider"),4, 1)
        layout.addWidget(QLabel("Textbrowser"),2,1, Qt.AlignmentFlag.AlignTop)
        self.setLayout(layout)

    @pyqtSlot(int)
    def append_text(self, value_as_int: int):
        text = "Value changed: " + str(value_as_int)
        self.text_edit.append(text)
