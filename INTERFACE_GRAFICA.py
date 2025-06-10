import customtkinter as ctk
from IA import IA
from AUTOMAÇÃO import Controller
from AUDIO import Listener

ctk.set_appearance_mode("dark")

class InterfaceGrafica:
    def __init__(self, largura, altura, titulo):
        self.largura = largura
        self.altura = altura
        self.titulo = titulo
        self.agente_inteligente = IA()
        self.controler = Controller()
        self.listener = Listener()

    def enviar(self):
        mensagem_usuario = self.caixa_texto_usuario.get("1.0", "end-1c")
        print(f"Texto do usuário: {mensagem_usuario}")
        reposta_do_modelo = self.agente_inteligente.previsao(mensagem_usuario)
        print(reposta_do_modelo)
        self.monstrarRespostaDoModeloNaTela(reposta_do_modelo)
        self.controler.direcionar(reposta_do_modelo)

    def monstrarRespostaDoModeloNaTela(self, reposta_do_modelo):
        self.caixa_texto_ia.configure(state="normal")
        self.caixa_texto_ia.delete("1.0", "end")  # Limpa o texto anterior
        self.caixa_texto_ia.insert("1.0", reposta_do_modelo)  # Insere o novo texto
        self.caixa_texto_ia.configure(state="disabled")

    def plot(self):
        self.root = ctk.CTk()
        self.root.geometry(f"{self.largura}x{self.altura}")
        self.root.title(self.titulo)
        
        self.criaLabel(0,0,"IA - OMEGA","#fd7f64")
        self.criaCaixaDeTextoIA(self.largura//2 - 30, self.altura//2 - 30, 1, 0)

        self.criaLabel(0,1,"PROMPT DO USUÁRIO", "yellow")
        self.criaCaixaDeTextoUsuario(self.largura//2 - 30, self.altura//2 - 30, 1, 1)

        self.criaBotao("ENVIAR", self.enviar, 2, 0)

        self.criaSwitchAudio(3, 0)

    def enviarMensagemPorAudio(self):
        if(self.switch_audio.get() == "on"):
            self.monstrarRespostaDoModeloNaTela("Ouvindo...")
            mensagem_usuario = self.listener.ouvirAudio()
            self.caixa_texto_usuario.delete("1.0", "end")  # Limpa o texto anterior
            self.caixa_texto_usuario.insert("1.0", mensagem_usuario) 
            reposta_do_modelo = self.agente_inteligente.previsao(mensagem_usuario)
            self.agente_inteligente.speaker.falar(reposta_do_modelo)
            self.caixa_texto_ia.configure(state="normal")
            self.caixa_texto_ia.delete("1.0", "end")  # Limpa o texto anterior
            self.caixa_texto_ia.insert("1.0", reposta_do_modelo)  # Insere o novo texto
            self.caixa_texto_ia.configure(state="disabled")
            self.controler.direcionar(reposta_do_modelo)

    
    def criaSwitchAudio(self, linha, coluna):
        self.modo_de_audio = ctk.StringVar(value="on")
        self.switch_audio = ctk.CTkSwitch(self.root, text="AUDIO MODE", command=self.enviarMensagemPorAudio,
            variable=self.modo_de_audio, onvalue="on", offvalue="off")
        self.switch_audio.grid(row=linha, column=coluna, padx=20, pady=20)

    def criaCaixaDeTexto(self, largura, altura, linha, coluna):
        text_box = ctk.CTkTextbox(self.root, width=largura, height=altura, wrap='word', font=('Helvetica', 17))
        text_box.grid(row=linha, column=coluna, pady=20, padx=20)
        return text_box

    def criaBotao(self,texto, comando, linha, coluna):
        botao = ctk.CTkButton(self.root, text=texto, command=comando)
        botao.grid(row=linha, column=coluna, padx=10, columnspan=2, pady=10)

    def criaCaixaDeTextoUsuario(self, largura, altura, linha, coluna):
        self.caixa_texto_usuario = self.criaCaixaDeTexto(largura, altura, linha, coluna)

    def criaCaixaDeTextoIA(self, largura, altura, linha, coluna):
        self.caixa_texto_ia = self.criaCaixaDeTexto(largura, altura, linha, coluna)
        self.caixa_texto_ia.configure(state="disabled")

    def criaLabel(self, linha, coluna, texto, cor_do_texto):
        novo_label = ctk.CTkLabel(self.root, text=texto, font=("Helvetica", 20), text_color = cor_do_texto)
        novo_label.grid(row=linha,column=coluna, padx=20, pady=20)

if __name__ == "__main__":
    interface = InterfaceGrafica(850, 550, "Interface Gráfica")
    interface.plot()
    interface.root.mainloop()
