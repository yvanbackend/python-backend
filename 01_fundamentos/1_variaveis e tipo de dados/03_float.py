# =============================================================================
# 03_float.py — Tipo Primitivo: float
# IEEE 754, imprecisão de ponto flutuante e como lidar com ela.
# =============================================================================

# -----------------------------------------------------------------------------
# 1. Declaração básica
# -----------------------------------------------------------------------------

altura  = 1.75
pi      = 3.14159
negativo = -0.5

print(type(altura))   # <class 'float'>

# -----------------------------------------------------------------------------
# 2. Float em Python = IEEE 754 double precision (64 bits)
# Isso significa: 15–17 dígitos significativos de precisão.
# Mas também significa: nem todo número decimal é representável em binário.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# 3. O problema clássico de ponto flutuante
# -----------------------------------------------------------------------------

print(0.1 + 0.2)           # 0.30000000000000004 ← NÃO é 0.3!
print(0.1 + 0.2 == 0.3)    # False ← nunca compare floats com ==

# Por quê? 0.1 em binário é uma dízima periódica — impossível representar exato.

# -----------------------------------------------------------------------------
# 4. Como comparar floats corretamente
# -----------------------------------------------------------------------------

import math

a = 0.1 + 0.2
b = 0.3

# Opção 1: math.isclose (recomendado)
print(math.isclose(a, b))            # True
print(math.isclose(a, b, rel_tol=1e-9))  # True — tolerância relativa

# Opção 2: round() antes de comparar (menos robusto)
print(round(a, 10) == round(b, 10))  # True

# -----------------------------------------------------------------------------
# 5. Notação científica
# -----------------------------------------------------------------------------

muito_pequeno = 1.5e-10   # 0.00000000015
muito_grande  = 2.3e8     # 230000000.0

print(muito_pequeno)
print(muito_grande)

# -----------------------------------------------------------------------------
# 6. Valores especiais do float
# -----------------------------------------------------------------------------

infinito_pos = float('inf')
infinito_neg = float('-inf')
nao_numero   = float('nan')   # Not a Number

print(infinito_pos > 10**1000)     # True
print(math.isinf(infinito_pos))    # True
print(math.isnan(nao_numero))      # True
print(nao_numero == nao_numero)    # False ← nan não é igual a nada, nem a si mesmo

# -----------------------------------------------------------------------------
# 7. float() — conversão explícita
# -----------------------------------------------------------------------------

print(float("3.14"))   # 3.14
print(float(10))       # 10.0
print(float(True))     # 1.0
print(float("inf"))    # inf

# -----------------------------------------------------------------------------
# 8. Quando float não basta: decimal.Decimal
# Para cálculos financeiros, NUNCA use float. Use Decimal.
# -----------------------------------------------------------------------------

from decimal import Decimal

preco     = Decimal("0.10")
desconto  = Decimal("0.20")
total     = preco + desconto

print(total)             # 0.30 — exato
print(type(total))       # <class 'decimal.Decimal'>

# Custo: Decimal é ~50–100x mais lento que float.
# Use apenas quando precisão decimal é requisito de negócio.
