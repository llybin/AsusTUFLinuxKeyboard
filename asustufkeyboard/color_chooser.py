from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QColorDialog, QVBoxLayout, QWidget


class ColorChooser(QWidget):
    def __init__(self):
        super().__init__()

        self.color_dialog = QColorDialog()
        self.color_dialog.setOption(QColorDialog.ColorDialogOption.DontUseNativeDialog, True)
        self.color_dialog.setCurrentColor(QColor(255, 255, 255))
        for child_widget in self.color_dialog.findChildren(QWidget):
            if child_widget.metaObject().className() not in [
                "QtPrivate::QColorPicker",
                "QtPrivate::QColorLuminancePicker",
            ]:
                child_widget.hide()

        layout = QVBoxLayout()
        layout.addWidget(self.color_dialog)
        self.setLayout(layout)
