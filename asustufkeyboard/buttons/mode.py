from typing import List

from PyQt6.QtWidgets import QGroupBox, QHBoxLayout, QRadioButton


class ModeButtons:
    mode_buttons: List[QRadioButton]

    def mode_button_group(self) -> QGroupBox:
        mode_buttons = []

        mode_group = QGroupBox("Mode")
        mode_layout = QHBoxLayout()
        mode_group.setLayout(mode_layout)

        mode_button_static = QRadioButton("Static")
        mode_layout.addWidget(mode_button_static)
        mode_buttons.append(mode_button_static)

        mode_button_breathing = QRadioButton("Breathing")
        mode_layout.addWidget(mode_button_breathing)
        mode_buttons.append(mode_button_breathing)

        mode_button_color_cycle = QRadioButton("Color Cycle")
        mode_button_color_cycle.setChecked(True)
        mode_layout.addWidget(mode_button_color_cycle)
        mode_buttons.append(mode_button_color_cycle)

        self.mode_buttons = mode_buttons
        return mode_group
