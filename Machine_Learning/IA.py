import joblib
from Audio.AUDIO import Speaker 
import os

class IA:
    def __init__(self):
        caminho = os.path.join(os.path.dirname(__file__), 'modelo_nb.joblib')
        self.modelo = joblib.load(caminho)
        caminho_vetorizador = os.path.join(os.path.dirname(__file__), 'vetorizador.joblib')
        self.vetorizador = joblib.load(caminho_vetorizador)
        self.speaker = Speaker()

    def previsao(self, mensagem_do_usuario):    
        mensagem_vect = self.vetorizador.transform([mensagem_do_usuario]).toarray()  # ✅ Vetorizado
        previsao = self.modelo.predict(mensagem_vect)
        return previsao[0]


if __name__ == "__main__":
    agente_de_ia = IA()
    agente_de_ia.previsao("Calculadora")

