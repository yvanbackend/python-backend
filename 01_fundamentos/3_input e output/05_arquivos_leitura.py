# =============================================================================
# 05_arquivos_leitura.py — Leitura de Arquivos com open()
# read()  |  readline()  |  readlines()  |  for linha in arquivo
# Como Python lê dados do disco.
# =============================================================================

# Setup: cria o arquivo que vamos usar nos exemplos abaixo.
with open("/tmp/texto.txt", "w", encoding="utf-8") as f:
    f.write("Python é uma linguagem de alto nível\n")
    f.write("Criada por Guido van Rossum em 1991\n")
    f.write("Usada em web, dados, IA e automação\n")
    f.write("Filosofia: legibilidade conta\n")
    f.write("Zen of Python: import this\n")

caminho = "/tmp/texto.txt"

# -----------------------------------------------------------------------------
# 1. Modo 'r' — leitura de texto
# Padrão do open() — você pode omitir o 'r', mas é melhor deixar explícito.
# -----------------------------------------------------------------------------

with open(caminho, "r", encoding="utf-8") as f:
    print("Arquivo aberto no modo leitura.")

# -----------------------------------------------------------------------------
# 2. .read() — lê o arquivo inteiro como uma única string
# -----------------------------------------------------------------------------

with open(caminho, "r", encoding="utf-8") as f:
    conteudo = f.read()

print(type(conteudo))    # <class 'str'>
print(conteudo)          # exibe tudo de uma vez

# Use quando: o arquivo é pequeno e você precisa do conteúdo todo.
# Evite quando: o arquivo pode ser grande (logs com milhões de linhas, etc).
# Por quê? .read() carrega TODO o arquivo na memória de uma vez.
# Um arquivo de 2GB vai consumir 2GB de RAM.

# .read(n) — lê apenas N caracteres:
with open(caminho, "r", encoding="utf-8") as f:
    primeiros = f.read(10)
    print(repr(primeiros))   # 'Python é ' — os 10 primeiros caracteres

# O cursor avança conforme você lê. Na próxima chamada, continua de onde parou:
with open(caminho, "r", encoding="utf-8") as f:
    parte1 = f.read(6)    # 'Python'
    parte2 = f.read(4)    # ' é u'
    print(parte1, parte2)

# -----------------------------------------------------------------------------
# 3. .readline() — lê uma linha por vez
# Cada chamada avança o cursor uma linha.
# -----------------------------------------------------------------------------

with open(caminho, "r", encoding="utf-8") as f:
    primeira = f.readline()   # lê a primeira linha
    segunda  = f.readline()   # lê a segunda linha

print(repr(primeira))    # 'Python é uma linguagem de alto nível\n'  ← note o \n
print(primeira.strip())  # 'Python é uma linguagem de alto nível'    ← sem o \n
print(segunda.strip())

# Quando readline() chega no final do arquivo, retorna string vazia "":
with open(caminho, "r", encoding="utf-8") as f:
    linha = f.readline()
    while linha != "":         # string vazia = fim do arquivo
        print(linha.strip())
        linha = f.readline()

# Use quando: você quer processar uma linha por vez com lógica entre elas.

# -----------------------------------------------------------------------------
# 4. for linha in arquivo — o jeito mais Pythônico para ler linha por linha
# Python lê uma linha por vez sem carregar o arquivo inteiro na memória.
# É mais eficiente que readline() e mais simples de escrever.
# -----------------------------------------------------------------------------

with open(caminho, "r", encoding="utf-8") as f:
    for linha in f:
        print(linha.strip())

# Por que é mais eficiente que .read() para arquivos grandes:
# .read()          → carrega TUDO na memória antes de processar
# for linha in f   → carrega uma linha, processa, descarta, carrega a próxima

# Exemplo prático: exibir só as linhas que contêm uma palavra específica
print("--- Linhas com 'Python' ---")
with open(caminho, "r", encoding="utf-8") as f:
    for linha in f:
        if "Python" in linha:
            print(linha.strip())

# Numerando as linhas:
print("--- Com número de linha ---")
numero = 1
with open(caminho, "r", encoding="utf-8") as f:
    for linha in f:
        print(numero, linha.strip())
        numero = numero + 1

# -----------------------------------------------------------------------------
# 5. .readlines() — lê todas as linhas e retorna uma lista
# ⚠ NOVO: lista é uma estrutura que você vai ver no Bloco 02.
# Por enquanto: pense como uma coleção de itens numerados a partir do 0.
# -----------------------------------------------------------------------------

with open(caminho, "r", encoding="utf-8") as f:
    linhas = f.readlines()   # ⚠ retorna uma lista de strings

# Cada item da lista é uma linha do arquivo (com \n no final):
print(linhas[0])    # primeira linha
print(linhas[1])    # segunda linha
print(linhas[-1])   # última linha

# Total de linhas:
print("Total de linhas:", len(linhas))

# Quando usar .readlines():
# Quando você precisa acessar linhas por posição (linha[0], linha[3]).
# Quando precisa saber o total antes de processar.
# Quando vai iterar mais de uma vez pelo arquivo.
# Desvantagem: igual ao .read(), carrega tudo na memória.

# -----------------------------------------------------------------------------
# 6. Quando usar cada método — resumo prático
# -----------------------------------------------------------------------------

# .read()          → arquivo pequeno, conteúdo todo como uma string
# .read(n)         → ler pedaços (chunk), útil para arquivos grandes
# .readline()      → uma linha por vez com lógica entre cada linha
# for linha in f   → PADRÃO para arquivos médios e grandes (mais eficiente)
# .readlines()     → precisa de acesso por posição ou contar linhas

# Regra simples para agora:
# Arquivo pequeno e quer tudo → .read()
# Quer processar linha por linha → for linha in f

# -----------------------------------------------------------------------------
# 7. Lendo arquivo gerado pelo usuário
# Combina input() com open() para ler o arquivo que o usuário indicar.
# -----------------------------------------------------------------------------

nome_arquivo = input("Digite o caminho do arquivo: ").strip()

# Verificação simples antes de tentar abrir:
# ⚠ NOVO: import os e os.path.exists() — vem do módulo 'os' do Python.
# Você vai entender módulos melhor mais à frente. Por enquanto, saiba que
# os.path.exists(caminho) retorna True se o arquivo existir.

import os

if os.path.exists(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as f:
        conteudo = f.read()
    print("Conteúdo do arquivo:")
    print(conteudo)
else:
    print("Arquivo não encontrado:", nome_arquivo)

# -----------------------------------------------------------------------------
# 8. Regras de ouro
# -----------------------------------------------------------------------------

# 1. SEMPRE use 'with' — fechamento garantido
# 2. SEMPRE especifique encoding='utf-8'
# 3. Para arquivos grandes: for linha in f (não carrega tudo na memória)
# 4. .readline() retorna "" no fim do arquivo — use como condição de parada
# 5. .strip() em cada linha remove o \n do final
# 6. Verifique se o arquivo existe antes de tentar abrir (os.path.exists)
