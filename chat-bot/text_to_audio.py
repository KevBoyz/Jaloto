import pyttsx3
eng = pyttsx3.init()



def speak(text):
    eng.say(text)
    eng.runAndWait()


speak('Que Machado98 te aceite no Reino das Trevas')

