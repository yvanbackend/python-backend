# =============================================================================
# 04_arquivos_escrita.py — Escrita de Arquivos com open()
# open(file, mode, encoding)  |  write()  |  with
# Como Python salva dados no disco — e por que o 'with' não é opcional.
# =============================================================================

# -----------------------------------------------------------------------------
# 1. Por que salvar em arquivo?
# Variáveis existem só enquanto o programa roda.
# Quando o programa fecha, os dados somem.
# Arquivos persistem os dados no disco.
# -----------------------------------------------------------------------------

# Sem arquivo:
nome = "Yvan"
# Quando o programa fechar, 'nome' deixa de existir.

# Com arquivo:
# O nome é salvo no disco e pode ser lido depois, por outro programa,
# ou pela próxima vez que esse mesmo programa rodar.

# -----------------------------------------------------------------------------
# 2. open() — abrindo um arquivo para escrita
# Assinatura: open(caminho, modo, encoding)
# -----------------------------------------------------------------------------

# Modos de escrita:
# 'w'  → cria o arquivo. Se já existir, APAGA o conteúdo e começa do zero.
# 'a'  → cria o arquivo. Se já existir, adiciona ao FINAL (não apaga).
# 'x'  → cria o arquivo. Se já existir, dá erro (proteção contra sobrescrita).

# SEMPRE especifique encoding='utf-8'.
# Sem isso, o comportamento muda entre Windows, Linux e Mac.

# -----------------------------------------------------------------------------
# 3. 'with' — o jeito correto de abrir arquivos
# -----------------------------------------------------------------------------

# ❌ Sem 'with' — você controla o fechamento manualmente:
f = open("/tmp/sem_with.txt", "w", encoding="utf-8")
f.write("linha 1\n")
f.close()   # se esquecer isso, o arquivo pode ficar corrompido

# ✅ Com 'with' — Python fecha o arquivo automaticamente:
with open("/tmp/com_with.txt", "w", encoding="utf-8") as f:
    f.write("linha 1\n")
# aqui o arquivo já foi fechado — você não precisa fazer nada

# 'with' garante o fechamento mesmo se algo der errado dentro do bloco.
# Sempre use 'with'. Sem exceção.

# -----------------------------------------------------------------------------
# 4. Modo 'w' — escrita (cria ou sobrescreve)
# -----------------------------------------------------------------------------

caminho = "/tmp/notas.txt"

with open(caminho, "w", encoding="utf-8") as f:
    f.write("Nota 1: Python I/O\n")
    f.write("Nota 2: open() com context manager\n")
    f.write("Nota 3: sempre use encoding='utf-8'\n")

# Importante: write() NÃO adiciona quebra de linha automaticamente.
# Você precisa colocar \n manualmente no final de cada linha.

# Verificando o resultado (leitura básica):
with open(caminho, "r", encoding="utf-8") as f:
    print(f.read())

# Sobrescrevendo — o conteúdo anterior desaparece:
with open(caminho, "w", encoding="utf-8") as f:
    f.write("Esse conteúdo substituiu tudo anterior.\n")

with open(caminho, "r", encoding="utf-8") as f:
    print(f.read())

# -----------------------------------------------------------------------------
# 5. Modo 'a' — append (adiciona sem apagar)
# -----------------------------------------------------------------------------

log = "/tmp/meu_log.txt"

# Primeira escrita — cria o arquivo:
with open(log, "w", encoding="utf-8") as f:
    f.write("Sistema iniciado\n")

# Adicionando ao final (não apaga o que já estava):
with open(log, "a", encoding="utf-8") as f:
    f.write("Usuário fez login\n")

with open(log, "a", encoding="utf-8") as f:
    f.write("Usuário fez logout\n")

# Verificando:
with open(log, "r", encoding="utf-8") as f:
    print(f.read())
# Sistema iniciado
# Usuário fez login
# Usuário fez logout

# Modo 'a' é ideal para logs — você acumula registros sem perder os anteriores.

# -----------------------------------------------------------------------------
# 6. Escrevendo dados do usuário em arquivo
# Combinando input() com open() para persistir informações.
# -----------------------------------------------------------------------------

print("--- Cadastro ---")
nome_usuario   = input("Nome: ").strip()
idade_usuario  = input("Idade: ").strip()
cidade_usuario = input("Cidade: ").strip()

with open("/tmp/cadastro.txt", "w", encoding="utf-8") as f:
    f.write(f"Nome: {nome_usuario}\n")
    f.write(f"Idade: {idade_usuario}\n")
    f.write(f"Cidade: {cidade_usuario}\n")

print("Cadastro salvo em /tmp/cadastro.txt")

# Verificando:
with open("/tmp/cadastro.txt", "r", encoding="utf-8") as f:
    print(f.read())

# -----------------------------------------------------------------------------
# 7. Escrevendo com print() em vez de write()
# print() também pode escrever em arquivo — e adiciona \n automaticamente.
# -----------------------------------------------------------------------------

with open("/tmp/via_print.txt", "w", encoding="utf-8") as f:
    print("Linha 1", file=f)      # file=f redireciona para o arquivo
    print("Linha 2", file=f)      # \n é adicionado automaticamente
    print(42, True, file=f)       # aceita qualquer tipo, igual ao print normal

with open("/tmp/via_print.txt", "r", encoding="utf-8") as f:
    print(f.read())

# Quando usar write() vs print(file=f):
# write()        → controle total, você gerencia o \n
# print(file=f)  → mais prático quando você tem tipos variados ou já usa sep/end

# -----------------------------------------------------------------------------
# 8. Modo 'x' — criação exclusiva (evita sobrescrever por acidente)
# -----------------------------------------------------------------------------

# 'x' só cria o arquivo se ele NÃO existir.
# Se já existir → FileExistsError.

# ⚠ NOVO: FileExistsError é uma exceção — você vai aprender a tratar
# exceções no Bloco 04. Por enquanto, só saiba que esse modo existe
# e que ele protege o arquivo de ser sobrescrito acidentalmente.

import os   # ⚠ NOVO: módulo para operações com o sistema de arquivos

arquivo_unico = "/tmp/unico.txt"

if os.path.exists(arquivo_unico):
    os.remove(arquivo_unico)   # remove para o exemplo funcionar

with open(arquivo_unico, "x", encoding="utf-8") as f:
    f.write("Criado com modo exclusivo\n")

print("Arquivo criado com sucesso.")

# Se tentar criar novamente → FileExistsError (você verá isso na execução).

# -----------------------------------------------------------------------------
# 9. Regras de ouro
# -----------------------------------------------------------------------------

# 1. SEMPRE use 'with' — Python fecha o arquivo automaticamente
# 2. SEMPRE especifique encoding='utf-8' — comportamento varia por SO
# 3. 'w' apaga o conteúdo existente — use 'a' se quiser acumular
# 4. 'a' é para logs e acumulação — não sobrescreve
# 5. write() NÃO adiciona \n — você coloca manualmente
# 6. print(file=f) adiciona \n automaticamente — mais conveniente para tipos variados
