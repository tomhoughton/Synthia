from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtCore import Qt

import sys

class Dojo(QMainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super(Dojo, self).__init__(*args, **kwargs)

        # Set the window title:
        self.setWindowTitle("Synthia Dojo")

        # Create the layouts:
        main_layout = QHBoxLayout()
        left_layout = QVBoxLayout()
        right_layout = QVBoxLayout()

        # Create the main widgets:
        main_widget = QWidget()
        left_widget = QWidget() # Holds the main title, buttons and create button.
        right_widget = QWidget()

        # Create the title:
        main_title = QLabel("Synthia Dojo")

        # Create the buttons:
        pluck_button = QPushButton("Pluck")
        lead_button = QPushButton("Lead")
        bass_button = QPushButton("Bass")
        eight08_button = QPushButton("808")
        create_button = QPushButton("Create")

        # Set the buttons to the layout:
        left_layout.addWidget(main_title)
        left_layout.addWidget(pluck_button)
        left_layout.addWidget(lead_button)
        left_layout.addWidget(bass_button)
        left_layout.addWidget(eight08_button)
        left_layout.addWidget(create_button)

        # Add layouts to widget:
        left_widget.setLayout(left_layout)

        # Add Widgets to the Layout:
        main_layout.addWidget(left_widget, 1)
        main_layout.addWidget(right_widget, 2)

        # Set the layout on the application's window:
        main_widget.setLayout(main_layout)

        # Set main widget:
        self.setCentralWidget(main_widget)


if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Dojo()
    window.show()
    sys.exit(app.exec())
        
