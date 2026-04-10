# =============================================================================
# 04_str.py — Tipo Primitivo: str (String)
# Imutabilidade, encoding, métodos essenciais e f-strings.
# =============================================================================

# -----------------------------------------------------------------------------
# 1. Declaração — aspas simples, duplas ou triplas (sem diferença semântica)
# -----------------------------------------------------------------------------

nome        = 'Yvan'
mensagem    = "Olá, mundo!"
multilinhas = """Linha 1
Linha 2
Linha 3"""

print(type(nome))   # <class 'str'>

# -----------------------------------------------------------------------------
# 2. Strings são IMUTÁVEIS e SEQUÊNCIAS de caracteres Unicode (UTF-8 por padrão)
# -----------------------------------------------------------------------------

palavra = "Python"
print(palavra[0])      # 'P'   — indexação (base 0)
print(palavra[-1])     # 'n'   — indexação reversa
print(palavra[1:4])    # 'yth' — slicing [start:stop] (stop exclusivo)
print(palavra[::-1])   # 'nohtyP' — inversão via slicing

# Imutabilidade: não é possível alterar um caractere
# palavra[0] = "J"  ← TypeError: 'str' object does not support item assignment

# -----------------------------------------------------------------------------
# 3. Concatenação e repetição
# -----------------------------------------------------------------------------

saudacao = "Olá, " + nome    # concatenação (cria novo objeto)
linha     = "-" * 40          # repetição

print(saudacao)
print(linha)

# ⚠️ Concatenar em loop com + é O(n²) — use "".join() para listas de strings

palavras = ["Python", "é", "eficiente"]
print(" ".join(palavras))   # O(n) — correto

# -----------------------------------------------------------------------------
# 4. f-strings (Python 3.6+) — forma padrão e mais eficiente de interpolação
# -----------------------------------------------------------------------------

idade   = 16
altura  = 1.75

print(f"Nome: {nome}, Idade: {idade}")
print(f"Altura formatada: {altura:.2f}")        # 2 casas decimais
print(f"Em maiúsculo: {nome.upper()}")          # expressões dentro de {}
print(f"{'centralizado':^20}")                  # alinhamento
print(f"{1_000_000:,}")                         # separador de milhar → 1,000,000

# -----------------------------------------------------------------------------
# 5. Métodos essenciais
# -----------------------------------------------------------------------------

texto = "  Olá, Python!  "

print(texto.strip())            # remove espaços nas bordas
print(texto.strip().lower())    # normalização → "olá, python!"
print(texto.strip().upper())    # "OLÁ, PYTHON!"

frase = "back-end,front-end,devops"
print(frase.split(","))         # ['back-end', 'front-end', 'devops']
print(frase.replace("-", "_"))  # "back_end,front_end,devops"
print(frase.count("end"))       # 2
print(frase.find("front"))      # 9 (índice) / -1 se não encontrar
print("Python" in "Python é top")  # True — operador 'in'

# -----------------------------------------------------------------------------
# 6. Verificações de conteúdo
# -----------------------------------------------------------------------------

print("123".isdigit())      # True
print("abc".isalpha())      # True
print("abc123".isalnum())   # True
print("  ".isspace())       # True
print("Yvan".startswith("Y"))  # True
print("Yvan".endswith("n"))    # True

# -----------------------------------------------------------------------------
# 7. len() e iteração
# -----------------------------------------------------------------------------

palavra = "Python"
print(len(palavra))         # 6

for char in palavra:
    print(char, end=" ")    # P y t h o n
print()

# -----------------------------------------------------------------------------
# 8. Escape sequences
# -----------------------------------------------------------------------------

print("Linha 1\nLinha 2")   # \n = nova linha
print("Tab\taqui")          # \t = tabulação
print("Aspas: \"citação\"") # \" = aspas dentro de string
print(r"C:\nova\pasta")     # raw string — ignora escapes (útil para paths/regex)
