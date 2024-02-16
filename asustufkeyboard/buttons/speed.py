from typing import List

from PyQt6.QtWidgets import QGroupBox, QHBoxLayout, QRadioButton


class SpeedButtons:
    speed_buttons: List[QRadioButton]

    def speed_button_group(self) -> QGroupBox:
        speed_buttons = []

        speed_group = QGroupBox("Speed")
        speed_layout = QHBoxLayout()
        speed_group.setLayout(speed_layout)

        speed_button_slow = QRadioButton("Slow")
        speed_button_slow.setChecked(True)
        speed_layout.addWidget(speed_button_slow)
        speed_buttons.append(speed_button_slow)

        speed_button_medium = QRadioButton("Medium")
        speed_layout.addWidget(speed_button_medium)
        speed_buttons.append(speed_button_medium)

        speed_button_fast = QRadioButton("Fast")
        speed_layout.addWidget(speed_button_fast)
        speed_buttons.append(speed_button_fast)

        self.speed_buttons = speed_buttons
        return speed_group
