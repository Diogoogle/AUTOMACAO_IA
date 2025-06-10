import joblib
from AUDIO import Speaker 

class IA:
    def __init__(self):
        self.modelo = joblib.load('modelo_nb.joblib')
        self.vetorizador = joblib.load('vetorizador.joblib')
        self.speaker = Speaker()

    def previsao(self, mensagem_do_usuario):    
        mensagem_vect = self.vetorizador.transform([mensagem_do_usuario]).toarray()  # ✅ Vetorizado
        previsao = self.modelo.predict(mensagem_vect)
        return previsao[0]


if __name__ == "__main__":
    agente_de_ia = IA()
    agente_de_ia.previsao("Calculadora")

