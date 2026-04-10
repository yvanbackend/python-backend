# =============================================================================
# 05_bool.py — Tipo Primitivo: bool (Booleano)
# Subclasse de int, truthiness, operadores lógicos e curto-circuito.
# =============================================================================

# -----------------------------------------------------------------------------
# 1. Declaração — apenas dois valores possíveis
# -----------------------------------------------------------------------------

verdadeiro  = True
falso       = False

print(type(verdadeiro))   # <class 'bool'>

# -----------------------------------------------------------------------------
# 2. bool é SUBCLASSE de int — fato fundamental do Python
# -----------------------------------------------------------------------------

print(isinstance(True, int))   # True — bool herda de int
print(True  == 1)              # True
print(False == 0)              # True
print(True  + True)            # 2 — operação aritmética válida!
print(True  * 5)               # 5
print(sum([True, True, False, True]))  # 3 — conta Trues em uma lista

# -----------------------------------------------------------------------------
# 3. Operadores lógicos: and, or, not
# -----------------------------------------------------------------------------

print(True  and True)    # True
print(True  and False)   # False
print(False or  True)    # True
print(False or  False)   # False
print(not True)          # False
print(not False)         # True

# -----------------------------------------------------------------------------
# 4. CURTO-CIRCUITO (Short-Circuit Evaluation) — comportamento crítico
# and → para no primeiro False
# or  → para no primeiro True
# Nenhuma avaliação desnecessária é feita.
# -----------------------------------------------------------------------------

def pesada():
    print("  [função executada]")
    return True

# 'and': se o primeiro é False, o segundo NEM É avaliado
print(False and pesada())    # False — pesada() NÃO é chamada

# 'or': se o primeiro é True, o segundo NEM É avaliado
print(True  or  pesada())    # True  — pesada() NÃO é chamada

# Isso é usado para evitar erros (ex: divisão por zero)
divisor = 0
resultado = divisor != 0 and (10 / divisor)
print(resultado)   # False — sem ZeroDivisionError

# -----------------------------------------------------------------------------
# 5. Truthiness e Falsiness — o que Python considera True/False
# Qualquer objeto pode ser avaliado como bool em contexto condicional.
# -----------------------------------------------------------------------------

# FALSY (avaliados como False):
valores_falsy = [False, 0, 0.0, "", [], {}, set(), None, 0j]

for v in valores_falsy:
    if not v:
        print(f"  Falsy: {repr(v)}")

# TRUTHY (tudo o mais):
valores_truthy = [True, 1, -1, "texto", [0], {"a": 1}, (1,)]

for v in valores_truthy:
    if v:
        print(f"  Truthy: {repr(v)}")

# -----------------------------------------------------------------------------
# 6. bool() — conversão explícita
# -----------------------------------------------------------------------------

print(bool(0))        # False
print(bool(1))        # True
print(bool(""))       # False
print(bool("texto"))  # True
print(bool([]))       # False
print(bool([1]))      # True
print(bool(None))     # False

# -----------------------------------------------------------------------------
# 7. Operadores de comparação — sempre retornam bool
# -----------------------------------------------------------------------------

x = 10

print(x > 5)     # True
print(x < 5)     # False
print(x == 10)   # True
print(x != 10)   # False
print(x >= 10)   # True
print(x <= 9)    # False

# Encadeamento de comparações (Pythônico — evita and redundante)
print(1 < x < 20)          # True  — equivale a: 1 < x and x < 20
print(5 <= x <= 10)        # True

# -----------------------------------------------------------------------------
# 8. is vs == — diferença fundamental
# ==  → compara VALOR (igualdade)
# is  → compara IDENTIDADE (mesmo objeto na memória)
# -----------------------------------------------------------------------------

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)   # True  — mesmos valores
print(a is b)   # False — objetos distintos na memória
print(a is c)   # True  — c referencia o MESMO objeto que a

# Use 'is' apenas para: None, True, False, e singletons.
# Nunca use 'is' para comparar strings ou números arbitrários.
x = None
print(x is None)   # ✅ correto
print(x == None)   # ⚠️ funciona, mas não é idiomático
