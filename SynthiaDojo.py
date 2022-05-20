from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtCore import Qt
from qt_material import apply_stylesheet
from PyQt6.QtWidgets import QStyleOptionSlider
import tensorflow as tf
from tensorflow import keras
from SynthiaV2 import Synthia

import sys

"""
NOTES:
# This is a link to update arc drawings when values change: 
https://forum.qt.io/topic/90341/change-dial-cosmetics-in-python/8
"""

class Dojo(QMainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super(Dojo, self).__init__(*args, **kwargs)

        # Get the synthia class:
        self.synthia = Synthia(df=None)
        self.selected_type = 0
        self.preset_name = ""

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
        self.create_button = QPushButton("Create")
        self.create_button.clicked.connect(self.create_button_clicked)

        # Preset name input box:
        self.preset_name_input = QLineEdit()
        self.preset_name_input.textChanged.connect(self.preset_name_input_change)

        # Create the sliders:
        self.consistency_slider = QSlider(Qt.Orientation.Horizontal)
        self.brightness_slider = QSlider(Qt.Orientation.Horizontal)
        self.evolution_slider = QSlider(Qt.Orientation.Horizontal)
        self.dynamics_slider = QSlider(Qt.Orientation.Horizontal)

        # Set the minimum and maximum of the sliders:
        self.consistency_slider.setMinimum(0)
        self.consistency_slider.setMaximum(10)
        self.brightness_slider.setMinimum(0)
        self.brightness_slider.setMaximum(10)
        self.evolution_slider.setMinimum(0)
        self.evolution_slider.setMaximum(10)
        self.dynamics_slider.setMinimum(0)
        self.dynamics_slider.setMaximum(10)

        # Set the signals:
        self.consistency_slider.valueChanged.connect(self.consistency_change)
        self.brightness_slider.valueChanged.connect(self.brightness_change)
        self.evolution_slider.valueChanged.connect(self.evolution_change)
        self.dynamics_slider.valueChanged.connect(self.dynamics_change)
        
        # Create the slider titles:
        self.consistency_slider_title = QLabel("Consistency")
        self.consistency_slider_title.setStyleSheet("font-size: 26px; padding: 7px;")
        self.brightness_slider_title = QLabel("Brightness")
        self.brightness_slider_title.setStyleSheet("font-size: 26px; padding: 7px;")
        self.evolution_slider_title = QLabel("Evolution")
        self.evolution_slider_title.setStyleSheet("font-size: 26px; padding: 7px;")
        self.dynamics_slider_title = QLabel("Dynamics")
        self.dynamics_slider_title.setStyleSheet("font-size: 26px; padding: 7px;")

    
        # Create the labels:
        pluck_title = QLabel("Pluck")
        lead_title = QLabel("Lead")
        eight08_title = QLabel("808")
        bass_title = QLabel("Bass")

        # Create the CheckBox's:
        self.pluck_check = QCheckBox() # 0
        self.pluck_check.setChecked(True)
        self.lead_check = QCheckBox() # 1
        self.eightOeight_check = QCheckBox() # 2
        self.bass_check = QCheckBox() # 3

        # Connect to functions:
        self.pluck_check.toggled.connect(self.pluck_toggle)
        self.lead_check.toggled.connect(self.lead_toggle)
        self.eightOeight_check.toggled.connect(self.eight08_toggle)
        self.bass_check.toggled.connect(self.bass_toggle)

        # Set the buttons to the layout:
        left_layout.addWidget(main_title)
        left_layout.addWidget(self.preset_name_input)
        left_layout.addWidget(self.create_button)
        
        # Right Layout:
        right_layout.addWidget(pluck_title)
        right_layout.addWidget(self.pluck_check)
        right_layout.addWidget(lead_title)   
        right_layout.addWidget(self.lead_check)
        right_layout.addWidget(eight08_title)
        right_layout.addWidget(self.eightOeight_check)
        right_layout.addWidget(bass_title)
        right_layout.addWidget(self.bass_check)
        right_layout.addWidget(types_widget)
        right_layout.addWidget(self.consistency_slider_title)
        right_layout.addWidget(self.consistency_slider)
        right_layout.addWidget(self.brightness_slider_title)
        right_layout.addWidget(self.brightness_slider)
        right_layout.addWidget(self.evolution_slider_title)
        right_layout.addWidget(self.evolution_slider)
        right_layout.addWidget(self.dynamics_slider_title)
        right_layout.addWidget(self.dynamics_slider)

        # Add layouts to widget:
        left_widget.setLayout(left_layout)
        right_widget.setLayout(right_layout)

        # Add Widgets to the Layout:
        main_layout.addWidget(left_widget, 1)
        main_layout.addWidget(right_widget, 2)

        # Set the layout on the application's window:
        main_widget.setLayout(main_layout)

        # Set main widget:
        self.setCentralWidget(main_widget)


    def pluck_toggle(self):
        if self.pluck_check.isChecked():
            # Change the state for the others:
            self.lead_check.setChecked(False)
            self.eightOeight_check.setChecked(False)
            self.bass_check.setChecked(False)

            self.selected_type = 0

    def lead_toggle(self):
        if self.lead_check.isChecked():
            # Change the state for the others:
            self.pluck_check.setChecked(False)
            self.eightOeight_check.setChecked(False)
            self.bass_check.setChecked(False)

            self.selected_type = 1

    def bass_toggle(self):
        if self.bass_check.isChecked():
            # Change the state for the others:
            self.pluck_check.setChecked(False)
            self.eightOeight_check.setChecked(False)
            self.lead_check.setChecked(False)

            self.selected_type = 3

    def eight08_toggle(self):
        if self.eightOeight_check.isChecked():
            # Change the state for the others:
            self.pluck_check.setChecked(False)
            self.bass_check.setChecked(False)
            self.lead_check.setChecked(False)
            
            self.selected_type = 2


    def consistency_change(self):
        print('Value Changed')
        title_change = 'Consistency: ' + str(self.consistency_slider.value())
        self.consistency_slider_title.setText(title_change)


    def brightness_change(self):
        print('Value Changed')
        title_change = 'Brightness: ' + str(self.brightness_slider.value())
        self.brightness_slider_title.setText(title_change)


    def evolution_change(self):
        print('Value Changed')
        title_change = 'Evolution: ' + str(self.evolution_slider.value())
        self.evolution_slider_title.setText(title_change)


    def dynamics_change(self):
        print('Value Changed')
        title_change = 'Dynamics: ' + str(self.dynamics_slider.value())
        self.dynamics_slider_title.setText(title_change)


    def preset_name_input_change(self, text):
        self.preset_name = text


    def create_button_clicked(self):
        print('Create')

        # Matrix with one row for the input (needs to be a matrix for tensorflow).
        synthia_input = [[0, 0, 0, 0, 0, 0, 0, 0]]

        # Assemble the input data:
        
        # First the types:
        if (self.selected_type == 0):
            synthia_input[0][7] = 1
        elif (self.selected_type == 1):
            synthia_input[0][6] = 1
        elif (self.selected_type == 2):
            synthia_input[0][4] = 1
        elif (self.selected_type == 3):
            synthia_input[0][5] = 1

        # Now we need to normalise the input values:
        consistency = float(self.consistency_slider.value() / 10)
        brightness = float(self.brightness_slider.value() / 10)
        evolution = float(self.evolution_slider.value() / 10)
        dynamics = float(self.dynamics_slider.value() / 10)

        # Add the descriptors to the synthia input matrix:
        synthia_input[0][0] = consistency
        synthia_input[0][1] = brightness
        synthia_input[0][2] = evolution
        synthia_input[0][3] = dynamics

        print(synthia_input)
        predictions = self.synthia.predict(model=None, input=synthia_input)
        print(predictions)
        
        self.synthia.export_preset(synthia_output=predictions, preset_name=self.preset_name) 


    def hello(self):
        print('Hello')

if __name__=="__main__":
    app = QApplication(sys.argv)
    app.setStyle('Material-Style')
    window = Dojo()
    apply_stylesheet(app, theme='color_palette.xml')
    window.show()
    sys.exit(app.exec())
        
