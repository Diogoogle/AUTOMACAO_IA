import customtkinter as ctk
from IA import IA

ctk.set_appearance_mode("dark")

class InterfaceGrafica:
    def __init__(self, largura, altura, titulo):
        self.largura = largura
        self.altura = altura
        self.titulo = titulo
        self.agente_inteligente = IA()

    def enviar(self):
        mensagem_usuario = self.caixa_texto_usuario.get("1.0", "end-1c")
        print(f"Texto do usuário: {mensagem_usuario}")
        reposta_do_modelo = self.agente_inteligente.previsao(mensagem_usuario)
        print(reposta_do_modelo)
        self.monstrarRespostaDoModeloNaTela(reposta_do_modelo)

    def monstrarRespostaDoModeloNaTela(self, reposta_do_modelo):
        self.caixa_texto_ia.delete("1.0", "end")  # Limpa o texto anterior
        self.caixa_texto_ia.insert("1.0", reposta_do_modelo)  # Insere o novo texto

    def plot(self):
        self.root = ctk.CTk()
        self.root.geometry(f"{self.largura}x{self.altura}")
        self.root.title(self.titulo)
        self.criaCaixaDeTextoIA(self.largura//2 - 30, self.altura//2 - 30,0,0)
        self.criaCaixaDeTextoUsuario(self.largura//2 - 30, self.altura//2 - 30,0,1)
        self.criaBotao("Enviar", self.enviar, 1, 0)

    def criaCaixaDeTexto(self, largura, altura, linha, coluna):
        text_box = ctk.CTkTextbox(self.root, width=largura, height=altura, wrap='word')
        text_box.grid(row=linha, column=coluna, pady=20, padx=20)
        return text_box

    def criaBotao(self,texto, comando, linha, coluna):
        botao = ctk.CTkButton(self.root, text=texto, command=comando)
        botao.grid(row=linha, column=coluna, padx=10, columnspan=2, pady=10)


    def criaCaixaDeTextoUsuario(self, largura, altura, linha, coluna):
        self.caixa_texto_usuario = self.criaCaixaDeTexto(largura, altura, linha, coluna)

    def criaCaixaDeTextoIA(self, largura, altura, linha, coluna):
        self.caixa_texto_ia = self.criaCaixaDeTexto(largura, altura, linha, coluna)


if __name__ == "__main__":
    interface = InterfaceGrafica(800, 500, "Interface Gráfica")
    interface.plot()
    interface.root.mainloop()
