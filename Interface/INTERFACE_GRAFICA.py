import customtkinter as ctk
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from MACHINE_LEARNING.IA import IA
from AUTOMACAO.AUTOMAÇÃO import Controller
from AUDIO.AUDIO import Listener
from COMPONENT_MANAGER import ComponentManager, ComponentManagerTelaSugestoes
from PIL import Image
from FUNCOES_DO_SISTEMA.SUPORT_FUNCTIONS import *
from MACHINE_LEARNING.DATA import map_mensagem_comando

ctk.set_appearance_mode("dark")

class InterfaceGrafica:
    def __init__(self, largura, altura, titulo):
        self.largura = largura
        self.altura = altura
        self.titulo = titulo
        self.agente_inteligente = IA()
        self.controler = Controller()
        self.listener = Listener()
        self.component_manager = ComponentManager()
        self.modo_light_dark_atual = "dark"

    def enviar(self):
        mensagem_usuario = self.caixa_texto_usuario.get("1.0", "end-1c")
        print(f"Texto do usuário: {mensagem_usuario}")
        nome_da_pasta = extrair_nome_pasta(mensagem_usuario)
        nome_do_arquivo, nome_da_pasta_onde_o_arquivo_sera_inserido = extrair_nome_da_pasta_e_do_arquivo_que_sera_criado_nela(mensagem_usuario)
        if (nome_da_pasta):
            reposta_do_modelo = self.agente_inteligente.previsao(mensagem_usuario)
            print(reposta_do_modelo)
            self.monstrarRespostaDoModeloNaTela(reposta_do_modelo)
            self.controler.criarPasta(nome_da_pasta)
        elif (nome_do_arquivo and nome_da_pasta_onde_o_arquivo_sera_inserido):
            resposta_do_modelo = self.agente_inteligente.previsao(mensagem_usuario)
            print(resposta_do_modelo)
            self.monstrarRespostaDoModeloNaTela(resposta_do_modelo)
            self.controler.criaArquivoDentroDePastaNaAreaDeTrabalho(nome_da_pasta_onde_o_arquivo_sera_inserido, nome_do_arquivo)
        else:
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

        self.component_manager.tela_principal = self.root
        
        self.lbl_ia = self.component_manager.criaLabel(0,0,"IA - OMEGA","#fd7f64")
        self.criaCaixaDeTextoIA(self.largura//2 - 30, self.altura//2 - 30, 1, 0)

        self.lbl_usu = self.component_manager.criaLabel(0,1,"PROMPT DO USUÁRIO", "yellow")
        self.criaCaixaDeTextoUsuario(self.largura//2 - 30, self.altura//2 - 30, 1, 1)

        self.component_manager.criaBotao(linha=2,coluna=0,texto="ENVIAR",comando=self.enviar)

        self.component_manager.criaBotao(linha=3,coluna=0,texto="AUDIO MODE",comando=self.enviarMensagemPorAudio)

        self.btn_toogle_light_dark_mode = self.component_manager.criaBotaoComImagem('./Interface/imagens/sol.png',0,2 ,self.toogleLightDark)

        self.btn_janela_sugestoes_prompts = self.component_manager.criaBotao(linha=0,coluna=3,texto="? Sugestões de Prompts ?",comando=self.criarJanelaDeSugestoesDePrompts)

    def toogleLightDark(self):
        if(self.modo_light_dark_atual == "dark"):
            ctk.set_appearance_mode("light")
            imagem = ctk.CTkImage(Image.open('./Interface/imagens/lua.png'), size=(32,32))
            self.btn_toogle_light_dark_mode.configure(image=imagem)
            self.modo_light_dark_atual = "light"
            self.lbl_ia.configure(text_color = "black")
            self.lbl_usu.configure(text_color = "black")
        else:
            ctk.set_appearance_mode("dark")
            imagem = ctk.CTkImage(Image.open('./Interface/imagens/sol.png'), size=(32,32))
            self.btn_toogle_light_dark_mode.configure(image=imagem)
            self.modo_light_dark_atual = "dark"
            self.lbl_ia.configure(text_color = "#fd7f64")
            self.lbl_usu.configure(text_color = "yellow")

    def enviarMensagemPorAudio(self):
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


    def criaCaixaDeTextoUsuario(self, largura, altura, linha, coluna):
        self.caixa_texto_usuario = self.component_manager.criaCaixaDeTexto(largura, altura, linha, coluna)

    def criaCaixaDeTextoIA(self, largura, altura, linha, coluna):
        self.caixa_texto_ia = self.component_manager.criaCaixaDeTexto(largura, altura, linha, coluna)
        self.caixa_texto_ia.configure(state="disabled")

    def criaLabel(self, linha, coluna, texto, cor_do_texto):
        novo_label = ctk.CTkLabel(self.root, text=texto, font=("Helvetica", 20), text_color = cor_do_texto)
        novo_label.grid(row=linha,column=coluna, padx=20, pady=20)

    def criarJanelaDeSugestoesDePrompts(self):
        self.janela_sugestoes = ctk.CTkToplevel(self.root)
        self.janela_sugestoes.title("Sugestões de Prompts")
        self.janela_sugestoes.geometry("600x500")

        self.component_manager_tela_sugestoes = ComponentManagerTelaSugestoes(self.janela_sugestoes)
        
        self.component_manager_tela_sugestoes.criaLabel(0, 0, "Sugestões de Prompts", "orange")

        self.scrollable_frame_janela_sugestoes = self.component_manager_tela_sugestoes.criaScrolableFrame(1, 0, 700, 500, "Sugestões")

        def gerenciaTextoDoItem(msg):
            self.caixa_texto_usuario.delete("1.0", "end")
            self.caixa_texto_usuario.insert("1.0", msg)

        for k, mensagem in enumerate(map_mensagem_comando.keys()):
            print(f"Adicionando sugestão: {mensagem}")
            self.component_manager_tela_sugestoes.criaItemDeSugestao(k, 0, mensagem, lambda msg=mensagem: gerenciaTextoDoItem(msg), self.scrollable_frame_janela_sugestoes)



if __name__ == "__main__":
    interface = InterfaceGrafica(850, 550, "Interface Gráfica")
    interface.plot()
    interface.root.mainloop()
