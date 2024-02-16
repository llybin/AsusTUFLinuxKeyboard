from typing import List

from PyQt6.QtWidgets import QCheckBox, QGroupBox, QHBoxLayout


class StateButtons:
    state_buttons: List[QCheckBox]

    def state_button_group(self) -> QGroupBox:
        state_buttons = []

        state_group = QGroupBox("State")
        state_layout = QHBoxLayout()
        state_group.setLayout(state_layout)

        state_button_boot = QCheckBox("Boot")
        state_button_boot.setChecked(True)
        state_layout.addWidget(state_button_boot)
        state_buttons.append(state_button_boot)

        state_button_awake = QCheckBox("Awake")
        state_button_awake.setChecked(True)
        state_layout.addWidget(state_button_awake)
        state_buttons.append(state_button_awake)

        state_button_sleep = QCheckBox("Sleep")
        state_layout.addWidget(state_button_sleep)
        state_buttons.append(state_button_sleep)

        self.state_buttons = state_buttons
        return state_group
