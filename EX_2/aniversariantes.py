import datetime

def obter_mes_atual():
    return datetime.datetime.now().month

def encontrar_aniversariantes():
    mes_atual = obter_mes_atual()
    aniversariantes = []

    try:
        with open("consultores.txt", "r") as arquivo_consultores:
            for linha in arquivo_consultores:
                # Quebrar a linha em uma lista usando Pipeline como separador:
                dados = linha.strip().split("|")
                if dados:
                    nome_completo = dados[0]
                    email = dados[1]
                    data_nascimento = datetime.datetime.strptime(dados[2], "%d/%m/%Y")
                    if data_nascimento.month == mes_atual:
                        # Adicionar o nome completo e a data de nascimento do consultor na lista de aniversariantes:
                        aniversariantes.append(f"{nome_completo} - {data_nascimento.strftime('%d/%m/%Y')}")
    except FileNotFoundError as e:
        print(f"Erro ao abrir o arquivo: {e}")

    return aniversariantes

def criar_arquivo_aniversariantes(aniversariantes):
    with open("aniversariantes.txt", "w") as arquivo_aniversariantes:
        arquivo_aniversariantes.write("Aniversariantes do Mês:\n")
        for aniversariante in aniversariantes:
            arquivo_aniversariantes.write(f"{aniversariante}\n")

aniversariantes = encontrar_aniversariantes()

if aniversariantes:
    criar_arquivo_aniversariantes(aniversariantes)
    print("Arquivo de aniversariantes do mês foi criado com sucesso!")
else:
    print("Não há aniversariantes neste mês.")
