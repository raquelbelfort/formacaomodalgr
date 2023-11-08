# Chave secreta:
chave_secreta = "#modalGR#GPTW#top#maiorEmpresaTecnologia#baixadaSantista"

# Função para criptografar a primeira senha (cifra de César):
def cifra_de_cesar(texto):
    resultado = ""
    for caractere in texto:
        # Verifica se o caractere é uma letra do alfabeto:
        if caractere.isalpha():
            troca = len(chave_secreta) % 26
            # Verifica se o caractere é maiúsculo ou minúsculo:
            if caractere.islower():
                # Converte o caractere para o código ASCII e realiza a troca:
                codigo = ord('a') + (ord(caractere) - ord('a') + troca) % 26
            else:
                codigo = ord('A') + (ord(caractere) - ord('A') + troca) % 26
                # Converte o código ASCII para caractere:
            resultado += chr(codigo)
        else:
            resultado += caractere
    return resultado

# Função para criptografar a segunda senha (cifra de Vigenère):
def cifra_de_vigenere(texto, chave):
    resultado = []
    for i, caractere in enumerate(texto):
        if caractere.isalpha():
            troca = ord(chave[i % len(chave)]) - ord('A')
            if caractere.islower():
                codigo = ord('a') + (ord(caractere) - ord('a') + troca) % 26
            else:
                codigo = ord('A') + (ord(caractere) - ord('A') + troca) % 26
            resultado.append(chr(codigo))
        else:
            resultado.append(caractere)
    return ''.join(resultado)

# Função para criptografar a terceira senha (cifra de Beaufort):
def cifra_de_beaufort(texto, chave):
    resultado = []
    for i, caractere in enumerate(texto):
        if caractere.isalpha():
            troca = ord(chave[i % len(chave)]) - ord('A')
            if caractere.islower():
                codigo = ord('a') + (ord('z') - ord(caractere) + troca) % 26
            else:
                codigo = ord('A') + (ord('Z') - ord(caractere) + troca) % 26
            resultado.append(chr(codigo))
        else:
            resultado.append(caractere)
    return ''.join(resultado)

# Exemplo de uso:
senha_original_cesar = "AmoModalGR"
senha_original_vigenere = "ModalGR2024"
senha_original_beaufort = "ProcessoFormacao"

senha_cifrada_cesar = cifra_de_cesar(senha_original_cesar)
senha_cifrada_vigenere = cifra_de_vigenere(senha_original_vigenere, chave_secreta)
senha_cifrada_beaufort = cifra_de_beaufort(senha_original_beaufort, chave_secreta)

print("Senha original (Cifra de César):", senha_original_cesar)
print("Senha criptografada (Cifra de César):", senha_cifrada_cesar, "\n")
print("Senha original (Cifra de Vigenère):", senha_original_vigenere)
print("Senha criptografada (Cifra de Vigenère):", senha_cifrada_vigenere, "\n")
print("Senha original (Cifra de Beaufort):", senha_original_beaufort)
print("Senha criptografada (Cifra de Beaufort):", senha_cifrada_beaufort, "\n")
