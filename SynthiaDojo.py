from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtCore import Qt
from qt_material import apply_stylesheet
from PyQt6.QtWidgets import QStyleOptionSlider
import tensorflow as tf
from tensorflow import keras

import sys

"""
NOTES:
# This is a link to update arc drawings when values change: 
https://forum.qt.io/topic/90341/change-dial-cosmetics-in-python/8
"""

class Dojo(QMainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super(Dojo, self).__init__(*args, **kwargs)

        # Set the window title:
        self.setWindowTitle("Synthia Dojo")

        # Create the layouts:
        main_layout = QHBoxLayout()
        left_layout = QVBoxLayout()
        right_layout = QVBoxLayout()
        types_layout = QHBoxLayout()

        # Create the main widgets:
        main_widget = QWidget()
        left_widget = QWidget() # Holds the main title, buttons and create button.
        right_widget = QWidget()
        types_widget = QWidget()

        # Create the title:
        main_title = QLabel("Synthia Dojo")
        main_title.setStyleSheet("font-size: 38px; padding: 16px; font-weight: bold")

        # Create the buttons:
        pluck_button = QPushButton("Pluck")
        lead_button = QPushButton("Lead")
        bass_button = QPushButton("Bass")
        eight08_button = QPushButton("808")
        create_button = QPushButton("Create")

        # Create the sliders:
        consistency_slider = QSlider(Qt.Orientation.Horizontal)
        brightness_slider = QSlider(Qt.Orientation.Horizontal)
        evolution_slider = QSlider(Qt.Orientation.Horizontal)
        dynamics_slider = QSlider(Qt.Orientation.Horizontal)

        # Create the slider titles:
        consistency_slider_title = QLabel("Consistency")
        consistency_slider_title.setStyleSheet("font-size: 26px; padding: 7px;")
        brightness_slider_title = QLabel("Brightness")
        brightness_slider_title.setStyleSheet("font-size: 26px; padding: 7px;")
        evolution_slider_title = QLabel("Evolution")
        evolution_slider_title.setStyleSheet("font-size: 26px; padding: 7px;")
        dynamics_slider_title = QLabel("Dynamics")
        dynamics_slider_title.setStyleSheet("font-size: 26px; padding: 7px;")

        """Checkbox's"""
        # Create the widgets:
        pluck_wid = QWidget()
        lead_wid = QWidget()
        eight08_wid = QWidget()
        bass_wid = QWidget() 

        # Create the layouts:
        pluck_lay = QVBoxLayout()
        lead_lay = QVBoxLayout()
        eight08_lay = QVBoxLayout()
        bass_lay = QVBoxLayout()

        # Create the labels:
        pluck_title = QLabel("Pluck")
        lead_title = QLabel("Lead")
        eight08_title = QLabel("808")
        bass_title = QLabel("Bass")

        # Create the CheckBox's:
        self.pluck_check = QCheckBox()
        self.lead_check = QCheckBox()
        self.eightOeight_check = QCheckBox()
        self.bass_check = QCheckBox()

        # Connect to functions:
        self.pluck_check.toggled.connect(self.type_toggle)
        self.lead_check.toggled.connect(self.type_toggle)
        self.eightOeight_check.toggled.connect(self.type_toggle)
        self.bass_check.toggled.connect(self.type_toggle)

        # Setup Layouts:
        pluck_lay.addWidget(pluck_title)
        pluck_lay.addWidget(self.pluck_check)
        lead_lay.addWidget(lead_title)
        lead_lay.addWidget(self.lead_check)
        eight08_lay.addWidget(eight08_title)
        eight08_lay.addWidget(self.eightOeight_check)
        bass_lay.addWidget(bass_title)
        bass_lay.addWidget(self.bass_check)

        # Set the layouts:
        pluck_wid.setLayout(pluck_lay)
        lead_wid.setLayout(lead_lay)
        eight08_wid.setLayout(eight08_lay)
        bass_wid.setLayout(bass_lay) 

        # Set the buttons to the layout:
        left_layout.addWidget(main_title)
        # left_layout.addWidget(pluck_button)
        # left_layout.addWidget(lead_button)
        # left_layout.addWidget(bass_button)
        # left_layout.addWidget(eight08_button)
        left_layout.addWidget(create_button)

        # Add layouts to widget:
        left_widget.setLayout(left_layout)
        right_widget.setLayout(right_layout)
        types_widget.setLayout(types_layout)

        # Types Layout:
        types_layout.addWidget(pluck_wid)
        types_layout.addWidget(lead_wid)
        types_layout.addWidget(eight08_wid)
        types_layout.addWidget(bass_wid)

        # Right Layout:
        right_layout.addWidget(types_widget)
        right_layout.addWidget(consistency_slider_title)
        right_layout.addWidget(consistency_slider)
        right_layout.addWidget(brightness_slider_title)
        right_layout.addWidget(brightness_slider)
        right_layout.addWidget(evolution_slider_title)
        right_layout.addWidget(evolution_slider)
        right_layout.addWidget(dynamics_slider_title)
        right_layout.addWidget(dynamics_slider)

        # Types Layout:
        types_layout.addWidget(self.pluck_check)
        types_layout.addWidget(self.lead_check)
        types_layout.addWidget(self.eightOeight_check)
        types_layout.addWidget(self.bass_check)
        
        # Add Widgets to the Layout:
        main_layout.addWidget(left_widget, 1)
        main_layout.addWidget(right_widget, 2)

        # Set the layout on the application's window:
        main_widget.setLayout(main_layout)

        # Set main widget:
        self.setCentralWidget(main_widget)

    def check_widget(self, title):
        w_title = QLabel(title)
        w_title.setStyleSheet("font-size: 26px; padding: 7px;")
        w_checkbox = QCheckBox()
        w_checkbox.toggled.connect(self.hello)
        wid = QWidget()
        lay = QVBoxLayout()
        lay.addWidget(w_title)
        lay.addWidget(w_checkbox)
        wid.setLayout(lay)
        return wid
    
    def type_toggle(self):
        print('Hello')


    def hello(self):
        print('Hello')

if __name__=="__main__":
    app = QApplication(sys.argv)
    app.setStyle('Material-Style')
    window = Dojo()
    apply_stylesheet(app, theme='color_palette.xml')
    window.show()
    sys.exit(app.exec())
        
