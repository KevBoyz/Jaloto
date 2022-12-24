from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
import qdarktheme


def send_message():
    if message.text():
        text_area.append(f'Kevin: {message.text()}')
        message.clear()
        # message.clearFocus()


app = QApplication([])
qdarktheme.setup_theme()

text_area = QTextEdit()
text_area.setFocusPolicy(Qt.FocusPolicy.NoFocus)

message = QLineEdit()
message.setFocusPolicy(Qt.FocusPolicy.WheelFocus)

layout = QVBoxLayout()
layout.addWidget(text_area)
layout.addWidget(message)

window = QWidget()
window.setWindowTitle(' ')
window.setLayout(layout)
window.setWindowIcon(QIcon('../assets/icons8-chatbot-302.png'))
window.show()

# Signals
message.returnPressed.connect(send_message)

app.exec()
