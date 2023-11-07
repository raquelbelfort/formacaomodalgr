# Biblioteca para manipulação de datas:
from datetime import datetime

def calcular_notas(valor, notas):
    resultado = []
    for nota in notas:
        quantidade = valor // nota
        # Se a quantidade de notas for maior que zero, 
        # adiciona a nota e a quantidade na lista de resultado:
        if quantidade > 0:
            resultado.append(f"{quantidade} x {nota} reais")
            valor -= quantidade * nota
    return resultado

# Solicita os dados do colaborador:
nome_colaborador = input("Digite o nome do colaborador: ")
data_admissao = input("Digite a data de admissão (no formato dd/mm/aaaa): ")
salario_atual = float(input("Digite o salário atual do colaborador (sem pontos ou vírgulas): "))
valor_emprestimo = float(input("Digite o valor de empréstimo desejado (sem pontos ou vírgulas): "))

# Verifica se o colaborador atende aos requisitos mínimos:
# Ano de admissao representa o último elemento da lista de datas.
# Exemplo: "01/01/2019" -> ["01", "01", "2019"] -> 2019
# Ano de trabalho é a diferença entre o ano atual e o ano de admissão.
ano_admissao = int(data_admissao.split("/")[-1])
anos_trabalho = datetime.now().year - ano_admissao

if anos_trabalho <= 5:
    print("Agradecemos seu interesse, mas você não atende os requisitos mínimos do programa.")
elif valor_emprestimo > 2 * salario_atual:
    print("O valor do empréstimo não pode exceder duas vezes o valor do salário.")
elif valor_emprestimo % 2 != 0:
    print("Insira um valor válido!")
else:
    print(f"Valor empréstimo: {int(valor_emprestimo)} reais")
    
    print("Notas de maior valor:")
    # As notas são calculadas a partir do valor do empréstimo e da lista de notas.
    for nota in calcular_notas(int(valor_emprestimo), [100, 50]):
        print(f"➢ {nota}", "\n")
    
    print("Notas de menor valor:")
    for nota in calcular_notas(int(valor_emprestimo), [20, 10, 5, 2]):
        print(f"➢ {nota}", "\n")

    meio_valor = int(valor_emprestimo) // 2
    print(f"{meio_valor} reais em notas de maior valor:")
    for nota in calcular_notas(meio_valor, [100, 50]):
        print(f"➢ {nota}", "\n")

    print(f"{meio_valor} reais em notas de menor valor:")
    for nota in calcular_notas(meio_valor, [20, 10, 5, 2]):
        print(f"➢ {nota}", "\n")
