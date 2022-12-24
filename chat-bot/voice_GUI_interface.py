# ChatBot

from chatterbot import ChatBot

bot = ChatBot('Jaloto')



# Vosk
from vosk import Model, KaldiRecognizer, SetLogLevel
import pyaudio

SetLogLevel(-1)
rate = 16000  # 16khz
model = Model(r'C:\Users\Kevin\Documents\GitHub\Jaloto\assets\vosk-model-small-pt-0.3')
recognizer = KaldiRecognizer(model, rate)

# Microphone
cap = pyaudio.PyAudio()
stream = cap.open(rate, 1, pyaudio.paInt16, frames_per_buffer=8192, input=True)
stream.start_stream()


def read():
    label.setPixmap(QPixmap.fromImage(robotOn))
    while True:
        data = stream.read(4096, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            text = eval(recognizer.Result())['text']
            if len(text) > 0:
                return text


def handler():
    while True:
        msg = read()
        print(msg)
        if len(msg) > 0:
            break
    speak(bot.get_response(msg))


# Text to voice
import pyttsx3

eng = pyttsx3.init()


def speak(text):
    eng.say(text)
    eng.runAndWait()


# interface
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QIcon, QPixmap, QImage
import qdarktheme
from sys import exit

robotOff = QImage('../assets/off-robot.png')
robotOn = QImage('../assets/on-robot.png')

app = QApplication([])
qdarktheme.setup_theme()

label = QLabel()
label.setPixmap(QPixmap.fromImage(robotOff))

layout = QVBoxLayout()
layout.addWidget(label)

window = QWidget()
window.setWindowTitle('Jaloto')
window.setWindowIcon(QIcon('../assets/icons8-chatbot-302.png'))

window.setLayout(layout)
window.show()

timer = QTimer()
timer.timeout.connect(handler)
milliseconds = 1000
timer.start(milliseconds)

exit(app.exec())
