import speech_recognition as sr
import pyttsx3

class Listener:
    def __init__(self):
        pass

    def ouvirAudio(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
        try:
            texto = recognizer.recognize_google(audio, language='pt-BR')
            return texto
        except Exception as e:
            return e

class Speaker:
    def __init__(self):
        self.engine = pyttsx3.init()

    def falar(self, texto):
        self.engine.say(texto)
        self.engine.runAndWait()

if __name__ == "__main__":
    print("Ouvindo")
    listener = Listener()
    audio_captado = listener.ouvirAudio()
    print(audio_captado)

