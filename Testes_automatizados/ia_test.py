import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Machine_Learning.IA import IA

class TestAgenteInteligente(unittest.TestCase):
    def test_resposta_youtube(self):
        agente_inteligente = IA()
        self.assertEqual(agente_inteligente.previsao("Por favor, abra o youtube para mim"), "Acessando o Youtube...")

    def test_resposta_drive(self):
        agente_inteligente = IA()
        self.assertEqual(agente_inteligente.previsao("Quero usar o Google Drive, abra ele"), "Acessando o google Drive")

    def test_resposta_gpt(self):
        agente_inteligente = IA()
        self.assertEqual(agente_inteligente.previsao("Gostaria que você abrisse o ChatGPT"), "Acessando o ChatGPT")

    def test_resposta_vs_code(self):
        agente_inteligente = IA()
        self.assertEqual(agente_inteligente.previsao("Quero codar no VsCode"), "Abrindo VsCode")

    def test_resposta_ava(self):
        agente_inteligente = IA()
        self.assertEqual(agente_inteligente.previsao("Preciso acessar minha conta do AVA"), "Fazendo login no AVA")

    def test_resposta_espaco_atividades(self):
        agente_inteligente = IA()
        self.assertEqual(agente_inteligente.previsao("Quero inicializar meu espaço de atividades"), "Abrindo espaço de atividades")

    def test_resposta_notion(self):
        agente_inteligente = IA()
        self.assertEqual(agente_inteligente.previsao("Preciso usar o Notion, poderia ir até lá?"), "Acessando o Notion")


if __name__ == "__main__":
    unittest.main()

    