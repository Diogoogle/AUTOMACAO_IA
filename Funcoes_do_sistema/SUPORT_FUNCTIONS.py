import re

def extrair_nome_pasta(mensagem):
    padroes = [
        r'Crie uma pasta na area de trabalho chamada (.+)',
        r'Crie uma nova pasta na area de trabalho chamada (.+)',
        r'Crie uma pasta nova na area de trabalho chamada (.+)',
        r'Crie um novo diretorio na area de trabalho chamado (.+)',
        r'Crie um diretorio novo na area de trabalho chamado (.+)',
        r'Crie um diretorio na area de trabalho chamado (.+)'
    ]
    for padrao in padroes:
        match = re.search(padrao, mensagem, re.IGNORECASE)
        if match:
            return match.group(1).strip()
    return None 

def verificaSeAPastaVeioAntesDoNomeDoArquivo(mensagem):
    for palavra in mensagem.split(" "):
        if ("pasta" in palavra.lower() or "diretorio" in palavra.lower()):
            return True
        elif "arquivo" in palavra.lower():
            return False
    

def extrair_nome_da_pasta_e_do_arquivo_que_sera_criado_nela(mensagem):
    print("Opa")
    padroes = [
        r'dentro da (?:pasta|diretorio) ([\w\-. ]+) (?:crie|criar) (?:um |o )?arquivo (?:chamado )?([\w\-. ]+)',
        r'(?:na|no|dentro do|dentro da) (?:pasta|diretorio) ([\w\-. ]+) (?:crie|criar) (?:um |o )?arquivo (?:chamado )?([\w\-. ]+)',
        r'(?:crie|criar) (?:um |o )?arquivo (?:chamado )?([\w\-. ]+) (?:na|no|dentro do|dentro da) (?:pasta|diretorio) ([\w\-. ]+)',
    ]
    for padrao in padroes:
        match = re.search(padrao, mensagem, re.IGNORECASE)
        print(match)
        if match:
            if verificaSeAPastaVeioAntesDoNomeDoArquivo(mensagem):
                pasta = match.group(1).strip()
                arquivo = match.group(2).strip()
                print(f"Arquivo: {arquivo}, Pasta: {pasta}")
            else:
                arquivo = match.group(1).strip()
                pasta = match.group(2).strip()
                print(f"Arquivo: {arquivo}, Pasta: {pasta}")
            return arquivo, pasta
    print("Está retornando None")
    return None, None



