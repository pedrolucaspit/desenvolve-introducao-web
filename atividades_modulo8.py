# Q1
def contagem_caracteres(frase):
    contagem = {}
    for char in frase:
        if char in contagem:
            contagem[char] += 1
        else:
            contagem[char] = 1
    return contagem

# Exemplo de uso:
frase = "python programming"
resultado = contagem_caracteres(frase)
print(resultado)

# Q2
def contar_palavras_arquivo(nome_arquivo):
    contagem_palavras = {}
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            palavras = linha.split()
            for palavra in palavras:
                palavra = palavra.strip('.,!?;:()[]{}')  # Remover pontuações
                if palavra:
                    if palavra in contagem_palavras:
                        contagem_palavras[palavra] += 1
                    else:
                        contagem_palavras[palavra] = 1
    return contagem_palavras

nome_arquivo = "estomago.txt"
resultado = contar_palavras_arquivo(nome_arquivo)
resultado_ordenado = sorted(resultado.items(), key=lambda x: x[1], reverse=True)
print(resultado_ordenado)

# Q3
def mesclar_dicionarios(dicionario1, dicionario2):
    novo_dicionario = dicionario1.copy()
    for chave, valor in dicionario2.items():
        if chave in novo_dicionario:
            novo_dicionario[chave] = max(novo_dicionario[chave], valor)
        else:
            novo_dicionario[chave] = valor
    return novo_dicionario

# Exemplo de uso:
dicionario1 = {'a': 1, 'b': 2, 'c': 3}
dicionario2 = {'b': 4, 'd': 5}
resultado = mesclar_dicionarios(dicionario1, dicionario2)
print(resultado)

# Q4
def filtrar_dicionario(dados, chaves_filtradas):
    return {chave: dados[chave] for chave in chaves_filtradas if chave in dados}

# Exemplo de uso:
dados = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
chaves_filtradas = ['a', 'c', 'e']
resultado = filtrar_dicionario(dados, chaves_filtradas)
print(resultado)

# Q5
def resultado_votacao(lista_votos):
    total_votos = sum(voto.values() for voto in lista_votos[0])
    resultado = {}
    for voto in lista_votos:
        for candidato, votos in voto.items():
            percentual = (votos / total_votos) * 100
            if candidato in resultado:
                total, _ = resultado[candidato]
                resultado[candidato] = (total + votos, percentual)
            else:
                resultado[candidato] = (votos, percentual)
    return resultado

# Exemplo de uso:
votos = [
    {'candidato_A': 120, 'candidato_B': 85, 'candidato_C': 90},
    {'candidato_A': 110, 'candidato_B': 95, 'candidato_C': 80},
    {'candidato_A': 130, 'candidato_B': 78, 'candidato_C': 105},
]
resultado = resultado_votacao(votos)
print(resultado)
