# =============================================================================
# 06_erros_arquivo.py — Erros Comuns em I/O e como evitá-los
# FileNotFoundError  |  UnicodeDecodeError  |  os.path.exists()
# Arquivos são dependências externas — coisas dão errado o tempo todo.
# ⚠ Tratamento completo de exceções (try/except) vem no Bloco 04.
#   Aqui você aprende a PREVENIR erros com verificações antes de abrir.
# =============================================================================

import os

# -----------------------------------------------------------------------------
# 1. O problema: abrir um arquivo que não existe
# -----------------------------------------------------------------------------

# Isso causa FileNotFoundError e para o programa:
# with open("nao_existe.txt", "r", encoding="utf-8") as f:
#     print(f.read())
# FileNotFoundError: [Errno 2] No such file or directory: 'nao_existe.txt'

# Solução com o que você já sabe: verificar antes de abrir.

# -----------------------------------------------------------------------------
# 2. os.path.exists() — verifica se o arquivo existe antes de abrir
# Retorna True se o arquivo existir, False se não existir.
# -----------------------------------------------------------------------------

caminho = "/tmp/meu_arquivo.txt"

if os.path.exists(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        print(f.read())
else:
    print("Arquivo não encontrado:", caminho)

# Criando o arquivo para os próximos exemplos:
with open(caminho, "w", encoding="utf-8") as f:
    f.write("Linha 1\nLinha 2\nLinha 3\n")

# Agora funciona:
if os.path.exists(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        print(f.read())
else:
    print("Arquivo não encontrado:", caminho)

# -----------------------------------------------------------------------------
# 3. Outros utilitários do os.path — informações sobre o arquivo
# -----------------------------------------------------------------------------

# Verificar se é um arquivo (não uma pasta):
print(os.path.isfile(caminho))      # True — é um arquivo
print(os.path.isdir(caminho))       # False — não é uma pasta
print(os.path.isdir("/tmp"))        # True — /tmp é uma pasta

# Tamanho em bytes:
tamanho = os.path.getsize(caminho)
print("Tamanho:", tamanho, "bytes")

# Nome do arquivo e pasta separados:
print(os.path.basename(caminho))    # meu_arquivo.txt
print(os.path.dirname(caminho))     # /tmp

# Verificar extensão:
nome, extensao = os.path.splitext(caminho)
print("Nome:", nome)                # /tmp/meu_arquivo
print("Extensão:", extensao)        # .txt

# Verificação completa antes de abrir:
if os.path.exists(caminho) and os.path.isfile(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        conteudo = f.read()
    print("Arquivo lido com sucesso.")
    print("Conteúdo:", conteudo)
else:
    print("Caminho inválido ou não é um arquivo.")

# -----------------------------------------------------------------------------
# 4. Erro de encoding — o arquivo usa uma codificação diferente
# Mais comum: arquivo criado no Windows (latin-1) sendo lido como utf-8.
# -----------------------------------------------------------------------------

# Criando um arquivo em latin-1 (simulando arquivo do Windows):
caminho_latin = "/tmp/windows.txt"
with open(caminho_latin, "wb") as f:   # 'wb' = modo binário
    f.write("Ação: café, coração\n".encode("latin-1"))

# Tentando ler como utf-8 — vai causar UnicodeDecodeError:
# with open(caminho_latin, "r", encoding="utf-8") as f:
#     print(f.read())
# UnicodeDecodeError: 'utf-8' codec can't decode byte...

# Solução 1: usar o encoding correto:
with open(caminho_latin, "r", encoding="latin-1") as f:
    print(f.read())   # lê corretamente

# Solução 2: usar errors='ignore' — descarta caracteres inválidos:
with open(caminho_latin, "r", encoding="utf-8", errors="ignore") as f:
    print("Com ignore:", f.read())   # perde alguns caracteres

# Solução 3: usar errors='replace' — substitui caracteres inválidos por ?:
with open(caminho_latin, "r", encoding="utf-8", errors="replace") as f:
    print("Com replace:", f.read())   # mostra ? onde não consegue ler

# Regra: se você não criou o arquivo, não assuma o encoding.
# Tente utf-8 primeiro. Se falhar, tente latin-1.

# -----------------------------------------------------------------------------
# 5. Erros comuns ao escrever
# -----------------------------------------------------------------------------

# Erro 1: esquecer o \n no write()
with open("/tmp/sem_newline.txt", "w", encoding="utf-8") as f:
    f.write("Linha 1")   # sem \n
    f.write("Linha 2")   # vai ficar na mesma linha que a 1

with open("/tmp/sem_newline.txt", "r", encoding="utf-8") as f:
    print(repr(f.read()))   # 'Linha 1Linha 2'  ← tudo junto

# Correto:
with open("/tmp/com_newline.txt", "w", encoding="utf-8") as f:
    f.write("Linha 1\n")
    f.write("Linha 2\n")

with open("/tmp/com_newline.txt", "r", encoding="utf-8") as f:
    print(repr(f.read()))   # 'Linha 1\nLinha 2\n'  ← correto

# Erro 2: usar 'w' quando queria 'a' (sobrescrever sem querer)
with open("/tmp/log.txt", "w", encoding="utf-8") as f:
    f.write("Entrada 1\n")

with open("/tmp/log.txt", "w", encoding="utf-8") as f:   # ← 'w' apaga tudo!
    f.write("Entrada 2\n")

with open("/tmp/log.txt", "r", encoding="utf-8") as f:
    print(f.read())   # só 'Entrada 2' — Entrada 1 sumiu!

# Correto para log (acumular):
with open("/tmp/log.txt", "w", encoding="utf-8") as f:
    f.write("Entrada 1\n")

with open("/tmp/log.txt", "a", encoding="utf-8") as f:   # ← 'a' não apaga
    f.write("Entrada 2\n")

with open("/tmp/log.txt", "r", encoding="utf-8") as f:
    print(f.read())   # 'Entrada 1\nEntrada 2\n'  ← ambas estão lá

# -----------------------------------------------------------------------------
# 6. Lendo arquivo informado pelo usuário — com validação
# -----------------------------------------------------------------------------

caminho_usuario = input("Caminho do arquivo: ").strip()

if not os.path.exists(caminho_usuario):
    print("Erro: arquivo não existe.")
elif not os.path.isfile(caminho_usuario):
    print("Erro: o caminho existe, mas é uma pasta, não um arquivo.")
else:
    nome_arquivo, ext = os.path.splitext(caminho_usuario)
    if ext != ".txt":
        print("Aviso: o arquivo não tem extensão .txt, mas tentaremos ler.")
    with open(caminho_usuario, "r", encoding="utf-8") as f:
        conteudo = f.read()
    print("Conteúdo:")
    print(conteudo)

# -----------------------------------------------------------------------------
# 7. O que vem depois — Bloco 04
# ⚠ Tudo aqui usa verificações (if/elif) para PREVENIR erros.
#   No Bloco 04 você aprenderá try/except para TRATAR erros que já aconteceram.
#   A diferença:
#   - if os.path.exists()  → você verifica ANTES de abrir (prevenção)
#   - try/except           → você tenta abrir e reage SE der errado (tratamento)
#   Em produção, os dois são usados juntos.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# 8. Regras de ouro
# -----------------------------------------------------------------------------

# 1. Verifique com os.path.exists() antes de abrir para leitura
# 2. Use os.path.isfile() para garantir que não é uma pasta
# 3. Sempre especifique encoding='utf-8' — encoding errado causa UnicodeDecodeError
# 4. Se suspeitar de encoding diferente, tente latin-1 como fallback
# 5. 'w' sobrescreve — verifique se era 'a' que você queria
# 6. write() não adiciona \n — strings grudadas são erro silencioso
