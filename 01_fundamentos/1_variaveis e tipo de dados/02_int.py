# =============================================================================
# 02_int.py — Tipo Primitivo: int (Inteiro)
# Precisão arbitrária, operações, bases numéricas e armadilhas.
# =============================================================================

# -----------------------------------------------------------------------------
# 1. Declaração básica
# -----------------------------------------------------------------------------

idade = 16
saldo_negativo = -500
zero = 0

print(type(idade))   # <class 'int'>

# -----------------------------------------------------------------------------
# 2. Python int tem PRECISÃO ARBITRÁRIA
# Diferente de C/Java (int 32-bit), Python não sofre overflow.
# O custo é memória — objetos int grandes alocam mais bytes.
# -----------------------------------------------------------------------------

numero_gigante = 10 ** 100   # Googol — sem problema algum
print(numero_gigante)

# -----------------------------------------------------------------------------
# 3. Operações aritméticas
# -----------------------------------------------------------------------------

a, b = 17, 5

print(a + b)    # 22  — soma
print(a - b)    # 12  — subtração
print(a * b)    # 85  — multiplicação
print(a / b)    # 3.4 — divisão SEMPRE retorna float
print(a // b)   # 3   — divisão inteira (floor division)
print(a % b)    # 2   — módulo (resto)
print(a ** b)   # 1419857 — exponenciação

# -----------------------------------------------------------------------------
# 4. Divisão inteira vs divisão real — diferença crítica
# a / b  → float (3.4)
# a // b → int   (3)  — trunca em direção ao -∞, não ao 0
# -----------------------------------------------------------------------------

print(-17 // 5)   # -4, não -3! Floor division arredonda para baixo
print(-17 % 5)    # 3  (não -2) — consequência do floor division

# -----------------------------------------------------------------------------
# 5. Bases numéricas — Python suporta literais em outras bases
# -----------------------------------------------------------------------------

binario     = 0b1010    # base 2  → 10
octal       = 0o12      # base 8  → 10
hexadecimal = 0xA       # base 16 → 10

print(binario, octal, hexadecimal)   # 10 10 10

# Convertendo para outras bases:
print(bin(255))    # '0b11111111'
print(oct(255))    # '0o377'
print(hex(255))    # '0xff'

# -----------------------------------------------------------------------------
# 6. int() — conversão explícita
# -----------------------------------------------------------------------------

print(int("42"))      # 42   — string numérica → int
print(int(3.99))      # 3    — trunca (NÃO arredonda)
print(int(True))      # 1
print(int(False))     # 0

# int("3.14") ← ValueError: não converte string float diretamente
print(int(float("3.14")))   # solução: dois passos

# -----------------------------------------------------------------------------
# 7. Underscore como separador visual (PEP 515)
# -----------------------------------------------------------------------------

populacao_brasil = 215_313_498   # mais legível que 215313498
print(populacao_brasil)
