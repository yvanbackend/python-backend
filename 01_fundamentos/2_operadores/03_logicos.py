# =============================================================================
# 03_logicos.py — Operadores Lógicos
# and  or  not — curto-circuito, retorno real e padrões idiomáticos.
# =============================================================================

# -----------------------------------------------------------------------------
# CONCEITO CENTRAL: and/or NÃO retornam True/False.
# Eles retornam UM DOS OPERANDOS — aquele que determinou o resultado.
# Isso é o que torna esses operadores poderosos além de condicionais.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# 1. and — retorna o primeiro valor FALSY, ou o último se todos forem truthy
# -----------------------------------------------------------------------------

print(True  and True)    # True
print(True  and False)   # False
print(False and True)    # False
print(False and False)   # False

# Retorno real (não apenas bool):
print(1   and 2)         # 2     — 1 é truthy, avalia e retorna 2
print(0   and 2)         # 0     — 0 é falsy, para aqui e retorna 0
print("a" and "b")       # 'b'   — 'a' é truthy, retorna 'b'
print(""  and "b")       # ''    — '' é falsy, retorna ''
print([]  and [1, 2])    # []    — [] é falsy, retorna []

# Regra: and retorna o primeiro operando falsy encontrado,
# ou o último operando se todos forem truthy.

# -----------------------------------------------------------------------------
# 2. or — retorna o primeiro valor TRUTHY, ou o último se todos forem falsy
# -----------------------------------------------------------------------------

print(True  or False)    # True
print(False or True)     # True
print(False or False)    # False

# Retorno real:
print(1   or  2)         # 1     — 1 é truthy, para aqui e retorna 1
print(0   or  2)         # 2     — 0 é falsy, avalia e retorna 2
print(""  or  "default") # 'default'
print([]  or  [1, 2])    # [1, 2]
print(0   or  0.0)       # 0.0   — todos falsy, retorna o último

# -----------------------------------------------------------------------------
# 3. not — inverte o valor de verdade, SEMPRE retorna bool
# -----------------------------------------------------------------------------

print(not True)     # False
print(not False)    # True
print(not 0)        # True  — 0 é falsy, not 0 = True
print(not 1)        # False
print(not "")       # True
print(not "texto")  # False
print(not [])       # True
print(not [1])      # False

print(type(not 42)) # <class 'bool'> — not sempre retorna bool puro

# -----------------------------------------------------------------------------
# 4. CURTO-CIRCUITO — nenhuma avaliação desnecessária
# and: se o 1º é falsy → o 2º nunca é avaliado
# or : se o 1º é truthy → o 2º nunca é avaliado
# -----------------------------------------------------------------------------

def com_efeito_colateral(valor):
    print(f"  [função chamada, retornando {valor}]")
    return valor

print("\n--- and com curto-circuito ---")
resultado = False and com_efeito_colateral(True)
# [função NÃO é chamada]
print(resultado)   # False

print("\n--- or com curto-circuito ---")
resultado = True or com_efeito_colateral(True)
# [função NÃO é chamada]
print(resultado)   # True

# Uso prático: evitar exceções
dados = None
tamanho = dados and len(dados)   # se dados for None, len() não é chamado
print(tamanho)   # None — sem AttributeError

divisor = 0
resultado = divisor != 0 and 100 / divisor
print(resultado)   # False — sem ZeroDivisionError

# -----------------------------------------------------------------------------
# 5. Padrões idiomáticos que exploram o retorno real de and/or
# -----------------------------------------------------------------------------

# Padrão 1: valor padrão (fallback)
nome = ""
exibir = nome or "Anônimo"
print(exibir)   # 'Anônimo'

config = {"timeout": 30}
limite = config.get("limite") or 100
print(limite)   # 100 — chave ausente retorna None, que é falsy

# Padrão 2: execução condicional compacta (use com moderação)
debug = True
debug and print("modo debug ativo")   # imprime se debug for True

# Padrão 3: seleção condicional (substituído pelo ternário em Python 3)
# Forma antiga (Python 2 era):
x = 10
maior = x > 0 and x or 0   # frágil — quebra se x for falsy

# Forma moderna: expressão ternária (preferida)
maior = x if x > 0 else 0
print(maior)   # 10

# -----------------------------------------------------------------------------
# 6. Tabela verdade completa com tipos mistos
# -----------------------------------------------------------------------------

combinacoes = [
    (1,    2),
    (0,    2),
    (1,    0),
    (0,    0),
    ("a",  "b"),
    ("",   "b"),
    ([1],  []),
    ([],   []),
]

print(f"\n{'A':<8} {'B':<8} {'A and B':<12} {'A or B':<12} {'not A'}")
print("-" * 52)
for a, b in combinacoes:
    print(f"{repr(a):<8} {repr(b):<8} {repr(a and b):<12} {repr(a or b):<12} {repr(not a)}")

# -----------------------------------------------------------------------------
# 7. Precedência: not > and > or
# -----------------------------------------------------------------------------

print(True or False and False)      # True  — and avalia primeiro
print((True or False) and False)    # False — parênteses mudam a ordem
print(not True or True)             # True  — not avalia antes do or
print(not (True or True))           # False — parênteses forçam or primeiro

# Regra prática: use parênteses sempre que a intenção não for óbvia.
# Clareza > esperteza.
