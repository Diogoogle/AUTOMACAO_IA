import pyautogui as pa
import webbrowser as web
from time import sleep
import os

class Controller:
    def __init__(self):
        pass

    def direcionar(self, comando_de_direcionamento):
        match(comando_de_direcionamento):
            case ("Acessando o ChatGPT"):
                self.acessarChatGPT()
            case ("Abrindo VsCode"):
                self.abrirVsCode()
            case ("Abrindo o Google"):
                self.abrirGoogle()
            case ("Acessando o Notion"):
                self.abrirNotion()
            case ("Fazendo login no AVA"):
                self.fazerLoginNoAVA()
            case ("Abrindo pasta da Unesc"):
                self.abrirPastaUnesc()
            case ("Abrindo espaço de atividades"):
                self.inicializaEspacoDeAtividades()
            case ("Acessando o google Drive"):
                self.acessandoOGoogleDrive()
            case ("Acessando o Youtube..."):
                self.acessarOYoutbe()
            case ("Criando pasta na area de trabalho"):
                self.criarPastaNaAreaDeTrabalho()
    
    def acessarOYoutbe(self):
        web.open('https://www.youtube.com/')

    def criarPastaNaAreaDeTrabalho(self):
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        nova_pasta = os.path.join(desktop, "Nova Pasta")
        if not os.path.exists(nova_pasta):
            os.makedirs(nova_pasta)

    def acessarChatGPT(self):
        web.open('https://chatgpt.com/')

    def abrirVsCode(self):
        pa.press('win')
        sleep(2)
        pa.write("VsCode")
        sleep(2)
        pa.press('enter')

    def abrirGoogle(self):
        web.open('https://www.google.com')

    def abrirNotion(self):
        web.open('https://www.notion.so/MASTER-VIEW-c895f29bdb7c4cd7aabfcb2bf8361790')

    def fazerLoginNoAVA(self):
        web.open('https://ava.unesc.net/login/index.php')
        sleep(7)
        pa.press('tab')
        pa.press('tab')
        sleep(2)
        pa.write('140804')
        sleep(2)
        pa.press('tab')
        sleep(2)
        pa.write('Botafogo123')
        sleep(2)
        pa.press('enter')

    def abrirPastaUnesc(self):
        pa.press('win')
        sleep(2)
        pa.write("Unesc")
        sleep(4)
        pa.press('enter')

    def inicializaEspacoDeAtividades(self):
        self.fazerLoginNoAVA()
        sleep(3)
        self.abrirNotion()
        sleep(1)
        self.abrirPastaUnesc()
        sleep(1)
        self.acessarChatGPT()
    
    def acessandoOGoogleDrive(self):
        web.open('https://drive.google.com/drive/u/0/home')
