mensagens_do_usuario = [
        "Por favor, acesse o Youtube",
        "Abra o Youtube",
        "Quero acessar o Youtube",
        "Inicie o Youtube",
        "Abra o Google",
        "Acesse o Google",
        "Quero abrir o Google",
        "Abra o VsCode",
        "Inicie o VsCode",
        "Abrir o Visual Studio Code",
        "Desligue o computador",
        "Desligar computador",
        "Quero desligar o PC",
        "Reinicie o computador",
        "Reiniciar computador",
        "Quero reiniciar o PC",
        "Abra o Word",
        "Inicie o Word",
        "Abrir o Microsoft Word",
        "Abra o Excel",
        "Inicie o Excel",
        "Abrir o Microsoft Excel",
        "Envie um e-mail",
        "Mandar um e-mail",
        "Quero enviar um e-mail",
        "Leia meus e-mails",
        "Ver meus e-mails",
        "Quero ler meus e-mails",
        "Mostre o calendário",
        "Abrir calendário",
        "Quero ver o calendário",
        "Abra a calculadora",
        "Inicie a calculadora",
        "Abrir calculadora",
        "Abra o painel de controle",
        "Abrir painel de controle",
        "Acesse o painel de controle",
        "Abra as configurações do sistema",
        "Abrir configurações do sistema",
        "Acesse as configurações do sistema",
        "Inicialize espaço de atividades",
        "Abra espaço de atividades",
        "Por favor, quero usar o espaço de atividades",
        "Acesse o chatgpt",
        "Abra o chatgpt",
        "Quero usar a IA gpt",
        "Por favor, abra o Chat GPT",
        "Gostaria de usar o ChatGPT",
        "Inteligencia Artificial do ChatGPT, acessa-la",
        "Abrir Notion",
        "Acesse o Notion",
        "Por favor, acessar Notion",
        "Acesse o AVA",
        "Abra o AVA",
        "Faça login na minha conta do AVA",
        "Abra a pasta da Unesc",
        "Acesse o diretório da Unesc",
        "Gostaria de ir para a pasta da Unesc"
    ]

comandos_a_serem_executados = [
        "Acessando o Youtube...",
        "Acessando o Youtube...",
        "Acessando o Youtube...",
        "Acessando o Youtube...",
        "Abrindo o Google",
        "Abrindo o Google",
        "Abrindo o Google",
        "Abrindo VsCode",
        "Abrindo VsCode",
        "Abrindo VsCode",
        "Desligando o computador",
        "Desligando o computador",
        "Desligando o computador",
        "Reiniciando o computador",
        "Reiniciando o computador",
        "Reiniciando o computador",
        "Abrindo o Word",
        "Abrindo o Word",
        "Abrindo o Word",
        "Abrindo o Excel",
        "Abrindo o Excel",
        "Abrindo o Excel",
        "Enviando um e-mail",
        "Enviando um e-mail",
        "Enviando um e-mail",
        "Lendo seus e-mails",
        "Lendo seus e-mails",
        "Lendo seus e-mails",
        "Mostrando o calendário",
        "Mostrando o calendário",
        "Mostrando o calendário",
        "Abrindo a calculadora",
        "Abrindo a calculadora",
        "Abrindo a calculadora",
        "Abrindo o painel de controle",
        "Abrindo o painel de controle",
        "Abrindo o painel de controle",
        "Abrindo as configurações do sistema",
        "Abrindo as configurações do sistema",
        "Abrindo as configurações do sistema",
        "Abrindo espaço de atividades",
        "Abrindo espaço de atividades",
        "Abrindo espaço de atividades",
        "Acessando o ChatGPT",
        "Acessando o ChatGPT",
        "Acessando o ChatGPT",
        "Acessando o ChatGPT",
        "Acessando o ChatGPT",
        "Acessando o ChatGPT",
        "Acessando o Notion",
        "Acessando o Notion",
        "Acessando o Notion",
        "Fazendo login no AVA",
        "Fazendo login no AVA",
        "Fazendo login no AVA",
        "Abrindo pasta da Unesc",
        "Abrindo pasta da Unesc",
        "Abrindo pasta da Unesc"
    ]

map_mensagem_comando = {}
for mensagem, comando in zip(mensagens_do_usuario, comandos_a_serem_executados):
    map_mensagem_comando[mensagem] = comando

map_mensagem_comando["Abra o google Drive"] = "Acessando o google Drive"
map_mensagem_comando["Acesse o google Drive"] = "Acessando o google Drive"
map_mensagem_comando["Encaminhe para o google Drive, por favor"] = "Acessando o google Drive"


dados_treino = {
    'Mensagem_do_usuario': map_mensagem_comando.keys(),
    'Comando_a_ser_executado': map_mensagem_comando.values()
}











