# =============================================================================
# 01_print.py — Saída de Dados com print()
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# Não é apenas print(valor). Tem parâmetros que mudam o comportamento.
# =============================================================================

# -----------------------------------------------------------------------------
# 1. Uso básico — imprimindo tipos diferentes
# print() converte qualquer tipo para str automaticamente antes de exibir.
# -----------------------------------------------------------------------------

print("Olá, Yvan")      # str
print(42)               # int   → exibe '42'
print(3.14)             # float → exibe '3.14'
print(True)             # bool  → exibe 'True'
print(None)             # NoneType → exibe 'None'

# Múltiplos valores separados por vírgula:
print("Nome:", "Yvan", "Idade:", 16)   # Nome: Yvan Idade: 16

# -----------------------------------------------------------------------------
# 2. sep= — define o separador entre os valores
# Padrão: sep=' '  (um espaço)
# -----------------------------------------------------------------------------

print(1, 2, 3)              # 1 2 3      (espaço entre cada valor)
print(1, 2, 3, sep="-")     # 1-2-3
print(1, 2, 3, sep="")      # 123        (sem separador)
print(1, 2, 3, sep=" | ")   # 1 | 2 | 3

# Exemplo prático: exibir data formatada
dia = 12
mes = 4
ano = 2026
print(dia, mes, ano, sep="/")   # 12/4/2026

# -----------------------------------------------------------------------------
# 3. end= — define o que vem depois do último valor
# Padrão: end='\n'  (quebra de linha)
# -----------------------------------------------------------------------------

print("Linha 1")          # imprime e pula para a próxima linha (padrão)
print("Linha 2")

print("sem quebra", end="")
print(" — mesma linha")   # sem quebra — mesma linha

print("A", end=" → ")
print("B", end=" → ")
print("C")                # A → B → C

# Exemplo prático: exibir progresso na mesma linha
print("Carregando", end="")
print(".", end="")
print(".", end="")
print(".", end="")
print(" pronto!")          # Carregando... pronto!

# -----------------------------------------------------------------------------
# 4. sep e end juntos
# -----------------------------------------------------------------------------

print("Python", "3", "12", sep=".", end="!\n")   # Python.3.12!

# Tabela simples com alinhamento manual:
print("Nome    ", end="")
print("Idade")
print("--------", end="")
print("-----")
print("Yvan    ", end="")
print(16)

# -----------------------------------------------------------------------------
# 5. Inspecionando valores com type() e repr()
# Ferramentas essenciais para entender o que está dentro de uma variável.
# -----------------------------------------------------------------------------

# type() — mostra o tipo do objeto:
print(type(42))        # <class 'int'>
print(type("Yvan"))    # <class 'str'>
print(type(3.14))      # <class 'float'>
print(type(True))      # <class 'bool'>
print(type(None))      # <class 'NoneType'>

# repr() — mostra a representação "de programador":
# Útil para ver aspas em strings e caracteres especiais.
print(repr("Yvan"))    # 'Yvan'    ← mostra as aspas
print(repr("\n"))      # '\\n'     ← mostra o escape, não a quebra de linha
print(repr(42))        # 42
print(repr(None))      # None

# Diferença entre print() e repr():
texto = "olá\nmundo"
print(texto)           # imprime em duas linhas (interpreta o \n)
print(repr(texto))     # 'olá\nmundo'  (mostra o \n como texto)

# Use repr() sempre que quiser ver o valor EXATO sem interpretação.
# Muito útil para debugar strings com espaços, \n ou caracteres invisíveis.

# -----------------------------------------------------------------------------
# 6. Exibindo o resultado de expressões
# print() avalia a expressão antes de exibir.
# -----------------------------------------------------------------------------

print(10 + 5)           # 15
print(10 > 5)           # True
print(10 == 10)         # True
print("Py" + "thon")    # Python  (concatenação de str)
print("Yvan".upper())   # YVAN
print(len("Python"))    # 6

# -----------------------------------------------------------------------------
# 7. Caracteres especiais dentro de strings (sequências de escape)
# O \ muda o significado do próximo caractere.
# -----------------------------------------------------------------------------

print("linha 1\nlinha 2")       # \n = quebra de linha
print("col1\tcol2\tcol3")       # \t = tabulação
print("ela disse \"olá\"")      # \" = aspas dentro da string
print('ela disse \'olá\'')      # \' = aspas simples dentro da string
print("barra: \\")              # \\ = barra invertida literal

# Raw string — ignora os escapes (útil para caminhos no Windows):
print(r"C:\Users\Yvan\Desktop")   # r antes das aspas

# -----------------------------------------------------------------------------
# 8. Regras de ouro
# -----------------------------------------------------------------------------

# 1. sep= controla o que vai ENTRE os valores
# 2. end= controla o que vai DEPOIS de tudo (padrão é \n)
# 3. type() para descobrir o tipo de qualquer variável
# 4. repr() para ver o valor exato, sem interpretação de escapes
# 5. print() avalia expressões antes de exibir — use no debug
