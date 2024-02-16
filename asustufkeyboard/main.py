import subprocess
import sys

from buttons import BrightnessButtons, ModeButtons, SpeedButtons, StateButtons
from color_chooser import ColorChooser
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget


class CommandMixin:
    def set_state(self):
        boot, awake, sleep = [int(b.isChecked()) for b in self.state_buttons]
        command = f"echo '1 {boot} {awake} {sleep} 1' > /sys/class/leds/asus::kbd_backlight/kbd_rgb_state"
        subprocess.run(command, shell=True)

    def set_brightness(self):
        brightness = self.brightness_buttons.index(
            next(button for button in self.brightness_buttons if button.isChecked())
        )
        command = f"echo {brightness} > /sys/class/leds/asus::kbd_backlight/brightness"
        subprocess.run(command, shell=True)

    def set_mode_color_speed(self, *args, **kwargs):
        mode = self.mode_buttons.index(next(button for button in self.mode_buttons if button.isChecked()))
        red = self.color_chooser.color_dialog.currentColor().red()
        green = self.color_chooser.color_dialog.currentColor().green()
        blue = self.color_chooser.color_dialog.currentColor().blue()
        speed = self.speed_buttons.index(next(button for button in self.speed_buttons if button.isChecked()))
        command = f"echo '1 {mode} {red} {green} {blue} {speed}' > /sys/class/leds/asus::kbd_backlight/kbd_rgb_mode"
        subprocess.run(command, shell=True)


class MainWindow(QWidget, CommandMixin, StateButtons, BrightnessButtons, ModeButtons, SpeedButtons):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Asus TUF Keyboard Backlight")

        main_layout = QVBoxLayout()

        # Command label

        label_command = QLabel("Grant write permissions in terminal:")
        main_layout.addWidget(label_command)

        text_command = QLabel(
            "sudo chmod 222 /sys/class/leds/asus::kbd_backlight/kbd_rgb_state"
            " /sys/class/leds/asus::kbd_backlight/kbd_rgb_mode"
            " /sys/class/leds/asus::kbd_backlight/brightness"
        )
        text_command.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        text_command.setFrameStyle(True)
        text_command.setWordWrap(True)
        main_layout.addWidget(text_command)

        # State buttons

        state_group = self.state_button_group()
        main_layout.addWidget(state_group)
        for button in self.state_buttons:
            button.clicked.connect(self.set_state)

        # Brightness buttons

        brightness_group = self.brightness_button_group()
        for button in self.brightness_buttons:
            button.clicked.connect(self.set_brightness)

        main_layout.addWidget(brightness_group)

        # Mode buttons

        mode_group = self.mode_button_group()
        for button in self.mode_buttons:
            button.clicked.connect(self.set_mode_color_speed)

        main_layout.addWidget(mode_group)

        # Speed buttons

        speed_group = self.speed_button_group()
        for button in self.speed_buttons:
            button.clicked.connect(self.set_mode_color_speed)

        main_layout.addWidget(speed_group)

        # Color chooser

        self.color_chooser = ColorChooser()
        self.color_chooser.color_dialog.currentColorChanged.connect(self.set_mode_color_speed)
        main_layout.addWidget(self.color_chooser)

        # Set layout

        self.setLayout(main_layout)
        self.set_mode_color_speed()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
