# =============================================================================
# 01_aritmeticos.py — Operadores Aritméticos
# O comportamento real de cada operador, incluindo os casos que travam junior.
# =============================================================================

# -----------------------------------------------------------------------------
# Operadores: +  -  *  /  //  %  **
# -----------------------------------------------------------------------------

a, b = 17, 5

# -----------------------------------------------------------------------------
# 1. Adição (+)
# -----------------------------------------------------------------------------

print(a + b)           # 22
print(1.5 + 2)         # 3.5  — int + float → float (promoção de tipo)
print("Olá" + " mundo") # concatenação de strings
print([1, 2] + [3, 4]) # [1, 2, 3, 4] — concatenação de listas

# -----------------------------------------------------------------------------
# 2. Subtração (-)
# -----------------------------------------------------------------------------

print(a - b)    # 12
print(5 - 8)    # -3

# -----------------------------------------------------------------------------
# 3. Multiplicação (*)
# -----------------------------------------------------------------------------

print(a * b)         # 85
print(3 * "ab")      # 'ababab' — repetição de string
print(2 * [0, 1])    # [0, 1, 0, 1] — repetição de lista

# -----------------------------------------------------------------------------
# 4. Divisão real (/)
# Sempre retorna float — mesmo que o resultado seja inteiro exato.
# -----------------------------------------------------------------------------

print(10 / 2)    # 5.0  ← float, não int
print(7  / 2)    # 3.5
print(type(10 / 2))  # <class 'float'>

# -----------------------------------------------------------------------------
# 5. Divisão inteira // (floor division)
# Trunca em direção ao -∞, não ao zero.
# Essa distinção é crítica com números negativos.
# -----------------------------------------------------------------------------

print(17 // 5)    #  3   — 17 / 5 = 3.4 → floor = 3
print(-17 // 5)   # -4   — -17 / 5 = -3.4 → floor = -4  (NÃO -3!)
print(17 // -5)   # -4   — mesma lógica
print(-17 // -5)  #  3   — negativo / negativo → floor positivo

# Comparação com int() que trunca em direção ao zero:
print(int(-17 / 5))   # -3  ← trunca para zero
print(-17 // 5)       # -4  ← floor, para -∞

# -----------------------------------------------------------------------------
# 6. Módulo % (resto da divisão inteira)
# Em Python: resultado tem o mesmo sinal do DIVISOR (não do dividendo).
# Consequência direta do floor division.
# -----------------------------------------------------------------------------

print(17 % 5)     #  2   — 17 = 5*3 + 2
print(-17 % 5)    #  3   — -17 = 5*(-4) + 3
print(17 % -5)    # -3   — 17 = -5*(-4) + (-3)
print(-17 % -5)   # -2   — -17 = -5*(3) + (-2)

# Aplicações comuns do módulo:
print(10 % 2 == 0)    # True  — verificar par/ímpar
print(7  % 2 == 0)    # False
print(100 % 7)        # 2  — dia da semana em algoritmos de calendário

# Relação entre //, % e /:
# a == (a // b) * b + (a % b)  ← sempre verdadeiro
print((-17 // 5) * 5 + (-17 % 5))   # -17 ✓

# -----------------------------------------------------------------------------
# 7. Exponenciação ** (potência)
# -----------------------------------------------------------------------------

print(2 ** 10)     # 1024
print(2 ** -2)     # 0.25  — expoente negativo → fração (retorna float)
print(9 ** 0.5)    # 3.0   — raiz quadrada via expoente fracionário
print((-1) ** 0.5) # nan em alguns contextos, (6.123e-17+1j) com complex

# Para raízes de forma explícita:
import math
print(math.sqrt(9))     # 3.0
print(math.isqrt(9))    # 3   — raiz quadrada inteira (Python 3.8+)
print(math.isqrt(10))   # 3   — trunca, não arredonda

# pow() com três argumentos: pow(base, exp, mod) — eficiente para criptografia
print(pow(2, 10, 100))  # (2**10) % 100 = 24 — sem criar o número inteiro gigante

# -----------------------------------------------------------------------------
# 8. Precedência de operadores (ordem de avaliação)
# PEMDAS: Parênteses → Exponenciação → Mul/Div → Add/Sub
# -----------------------------------------------------------------------------

print(2 + 3 * 4)        # 14  — multiplicação antes da soma
print((2 + 3) * 4)      # 20  — parênteses forçam a soma primeiro
print(2 ** 3 ** 2)      # 512 — ** associa à DIREITA: 2 ** (3**2) = 2**9
print((2 ** 3) ** 2)    # 64  — explicitando associação à esquerda

# Precedência completa (maior → menor):
# **
# + - (unários)
# * / // %
# + -
# (comparadores, lógicos... vistos nos outros arquivos)
