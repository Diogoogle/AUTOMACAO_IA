import customtkinter as ctk
from PIL import Image

class ComponentManager:
    def __init__(self):
        self.tela_principal = None

    def criaBotao(self, linha, coluna, texto, comando, tela = None):
        btn = ctk.CTkButton(self.tela_principal if tela == None else tela, text=texto, font=("Arial", 12), command=comando)
        btn.grid(row=linha, column=coluna, padx=10, pady=10, columnspan=2)

    def criaLabel(self, linha, coluna, texto, cor_do_texto, tela = None):
        novo_label = ctk.CTkLabel(self.tela_principal if tela == None else tela, text=texto, font=("Helvetica", 20), text_color = cor_do_texto)
        novo_label.grid(row=linha,column=coluna, padx=20, pady=20)
        return novo_label
    
    def criaCaixaDeTexto(self, largura, altura, linha, coluna, tela = None):
        text_box = ctk.CTkTextbox(self.tela_principal if tela == None else tela, width=largura, height=altura, wrap='word', font=('Helvetica', 17))
        text_box.grid(row=linha, column=coluna, pady=20, padx=20)
        return text_box

    def criaBotaoComImagem(self, caminho_img, linha, coluna, comando) -> ctk.CTkButton:
        imagem = ctk.CTkImage(Image.open(caminho_img), size=(32,32))
        btn = ctk.CTkButton(master=self.tela_principal, text="", image=imagem, width=30, height=30, command=comando, bg_color="white", hover_color="white", fg_color="white", border_width=0, corner_radius=10)
        btn.grid(row=linha, column=coluna, padx=10, pady=10)
        return btn

    def criaScrolableFrame(self, linha, coluna, largura, altura, texto_label):
        scrollable_frame = ctk.CTkScrollableFrame(self.tela_principal, width=largura, height=altura, label_text=texto_label)
        scrollable_frame.grid(row=linha, column=coluna, padx=20, pady=20, sticky="w")
        return scrollable_frame


class ComponentManagerTelaSugestoes(ComponentManager):
    def __init__(self, tela_principal):
        super().__init__()
        self.tela_principal = tela_principal

    def criaLabel(self, linha, coluna, texto, cor_do_texto, frame=None):
        novo_label = ctk.CTkLabel(self.tela_principal if frame==None else frame, text=texto, font=("Helvetica", 20), text_color = cor_do_texto, anchor="w")
        novo_label.grid(row=linha,column=coluna, padx=20, pady=20, sticky="w")
        return novo_label

    def criaBotao(self, linha, coluna, texto, comando, frame):
        return super().criaBotao(linha, coluna, texto, comando, frame)
    
    def criaItemDeSugestao(self, linha, coluna, texto, comando, frame):
        label = self.criaLabel(linha, coluna, texto, "white", frame)
        btn = self.criaBotao(linha, coluna + 1, "+", comando, frame)
        return (label, btn)