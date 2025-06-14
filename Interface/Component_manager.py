import customtkinter as ctk
from PIL import Image

class Component_Manager:
    def __init__(self):
        self.tela_principal = None

    def criaBotao(self, linha, coluna, texto, comando):
        btn = ctk.CTkButton(self.tela_principal, text=texto, font=("Arial", 12), command=comando)
        btn.grid(row=linha, column=coluna, padx=10, pady=10, columnspan=2)

    def criaLabel(self, linha, coluna, texto, cor_do_texto):
        novo_label = ctk.CTkLabel(self.tela_principal, text=texto, font=("Helvetica", 20), text_color = cor_do_texto)
        novo_label.grid(row=linha,column=coluna, padx=20, pady=20)
        return novo_label
    
    def criaCaixaDeTexto(self, largura, altura, linha, coluna):
        text_box = ctk.CTkTextbox(self.tela_principal, width=largura, height=altura, wrap='word', font=('Helvetica', 17))
        text_box.grid(row=linha, column=coluna, pady=20, padx=20)
        return text_box

    def criaBotaoComImagem(self, caminho_img, linha, coluna, comando) -> ctk.CTkButton:
        imagem = ctk.CTkImage(Image.open(caminho_img), size=(32,32))
        btn = ctk.CTkButton(master=self.tela_principal, text="", image=imagem, width=30, height=30, command=comando)
        btn.grid(row=linha, column=coluna, padx=10, pady=10)
        return btn