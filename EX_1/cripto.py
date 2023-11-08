# Chave secreta:
chave_secreta = "#modalGR#GPTW#top#maiorEmpresaTecnologia#baixadaSantista"

# Função para criptografar a primeira senha (em binário):
def criptografar_em_binario(senha, chave):
    senha_cifrada = ""
    chave_idx = 0
    for caractere in senha:
        # O operador ^ realiza a operação XOR (OU exclusivo) bit a bit entre dois números.
        # O format() é usado para converter o resultado em uma string de 8 bits.
        # O ord() retorna o código ASCII do caractere.
        # O 08b significa que o resultado deve ser formatado como um número binário com 8 dígitos.
        binario = format(ord(caractere) ^ ord(chave[chave_idx]), '08b')
        senha_cifrada += binario
        chave_idx = (chave_idx + 1) % len(chave)
    return senha_cifrada

# Função para criptografar a segunda senha (em hexadecimal):
def criptografar_em_hexadecimal(senha, chave):
    senha_cifrada = ""
    chave_idx = 0
    for caractere in senha:
        hexadecimal = format(ord(caractere) ^ ord(chave[chave_idx]), '02x')
        senha_cifrada += hexadecimal
        chave_idx = (chave_idx + 1) % len(chave)
    return senha_cifrada

# Função para criptografar a terceira senha (em octal):
def criptografar_em_octal(senha, chave):
    senha_cifrada = ""
    chave_idx = 0
    for caractere in senha:
        octal = format(ord(caractere) ^ ord(chave[chave_idx]), '03o')
        senha_cifrada += octal
        chave_idx = (chave_idx + 1) % len(chave)
    return senha_cifrada

# Exemplo de uso:
senha_original_binario = "AmoModalGR"
senha_cifrada_binario = criptografar_em_binario(senha_original_binario, chave_secreta)

senha_original_hexadecimal = "ModalGR2024"
senha_cifrada_hexadecimal = criptografar_em_hexadecimal(senha_original_hexadecimal, chave_secreta)

senha_original_octal = "ProcessoFormacao"
senha_cifrada_octal = criptografar_em_octal(senha_original_octal, chave_secreta)

print("Senha original (Binário):", senha_original_binario)
print("Senha criptografada (Binário):", senha_cifrada_binario, "\n")
print("Senha original (Hexadecimal):", senha_original_hexadecimal)
print("Senha criptografada (Hexadecimal):", senha_cifrada_hexadecimal, "\n")
print("Senha original (Octal):", senha_original_octal)
print("Senha criptografada (Octal):", senha_cifrada_octal, "\n")
