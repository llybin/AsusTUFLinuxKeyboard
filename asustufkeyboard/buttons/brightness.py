from typing import List

from PyQt6.QtWidgets import QGroupBox, QHBoxLayout, QRadioButton


class BrightnessButtons:
    brightness_buttons: List[QRadioButton]

    def brightness_button_group(self) -> QGroupBox:
        brightness_buttons = []

        brightness_group = QGroupBox("Brightness")
        brightness_layout = QHBoxLayout()
        brightness_group.setLayout(brightness_layout)

        brightness_button_off = QRadioButton("Off")
        brightness_layout.addWidget(brightness_button_off)
        brightness_buttons.append(brightness_button_off)

        brightness_button_low = QRadioButton("Low")
        brightness_button_low.setChecked(True)
        brightness_layout.addWidget(brightness_button_low)
        brightness_buttons.append(brightness_button_low)

        brightness_button_medium = QRadioButton("Medium")
        brightness_layout.addWidget(brightness_button_medium)
        brightness_buttons.append(brightness_button_medium)

        brightness_button_high = QRadioButton("High")
        brightness_layout.addWidget(brightness_button_high)
        brightness_buttons.append(brightness_button_high)

        self.brightness_buttons = brightness_buttons
        return brightness_group
