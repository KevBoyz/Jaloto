from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
import qdarktheme


from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('Jaloto')

conversation = ['Já luto', 'Olá, mestre supremo',
                'Jaloto', 'Olá, divinidade cosmica',
                'bote', 'Diga arquiteto do universo',
                'o que é o natal', 'É a comemoração do nascimento de Machado98',
                'pra você o que é a humanidade', 'Um bando de macacos que usam blues',
                'reze a oração machado nosso', 'Machado nosso que estais nas trevas, santificado seja o vosso cabo, venha a nós a vosso server, seja feita a vossa vontade assim no overworld como no nether. O pão nosso de cada 24 minutos nos dai hoje, não deixeis explodir a casa do amigo, mas livrai-nos dos que não sabem brincar. Rororororororororororo',
                'qual é o seu nome', 'Jaloto',
                'o que você faz', 'Retorno texto apartir de um input, e falo por meio da voz de Microsoft Daniel',
                'o que você acha de raparigas', 'Para mim são nota dez',
                'recomende-me um artista', 'Zé Cabaré',
                'quanto você pesa', 'Eu sou tão magro, que se fosse médium, meu corpo não tinha espaço para conceber o espírito',
                'confirme o ataque a residência de vulgo cambito seco', 'Mísseis mirados para lá nesse exato momento',
                'me informe a localização do agente sete', 'Segundo meus contatos, Gildênjajaja Eiro está passando suas férias, no deserto do Caárae'
                ]

trainer = ListTrainer(bot)
trainer.train(conversation)


def send_message():
    if message.text():
        text_area.append(f'Kevin: {message.text()}')
        text_area.append(f'Jaloto: {bot.get_response(message.text())}')
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

