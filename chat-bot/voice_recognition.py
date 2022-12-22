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
    while True:
        data = stream.read(4096, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            text = eval(recognizer.Result())['text']
            if len(text) > 0:
                return text


def handler():
    print('Recording....')
    while True:
        msg = read()
        if msg:
            break

    print(msg)


handler()
