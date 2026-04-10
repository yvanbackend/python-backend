# =============================================================================
# 02_comparacao.py — Operadores de Comparação
# ==  !=  >  <  >=  <=  — sempre retornam bool.
# Encadeamento, comparação de tipos mistos e armadilhas.
# =============================================================================

# -----------------------------------------------------------------------------
# 1. Operadores básicos
# -----------------------------------------------------------------------------

x = 10

print(x == 10)   # True  — igual a
print(x != 10)   # False — diferente de
print(x >  5)    # True  — maior que
print(x <  5)    # False — menor que
print(x >= 10)   # True  — maior ou igual
print(x <= 9)    # False — menor ou igual

# -----------------------------------------------------------------------------
# 2. Encadeamento de comparações — exclusivo do Python
# Python avalia como: a < b < c → (a < b) and (b < c)
# b é avaliado UMA ÚNICA vez, mesmo sendo uma expressão complexa.
# -----------------------------------------------------------------------------

print(1 < 5 < 10)          # True
print(1 < 5 > 3)           # True  — equivale a: 1<5 and 5>3
print(10 == 10 == 10)      # True
print(1 < 5 < 3)           # False — 5 < 3 é False

# Uso real: validação de intervalo
nota = 7.5
print(0 <= nota <= 10)     # True — mais legível que nota >= 0 and nota <= 10

idade = 20
print(18 <= idade < 65)    # True — adulto não aposentado

# -----------------------------------------------------------------------------
# 3. Comparação de strings — ordem lexicográfica (Unicode)
# -----------------------------------------------------------------------------

print("a" < "b")       # True  — 'a' (97) < 'b' (98) no Unicode
print("b" < "a")       # False
print("abc" < "abd")   # True  — compara char por char até divergir
print("Z" < "a")       # True  — maiúsculas (65-90) < minúsculas (97-122)
print("banana" > "abacaxi")  # True — 'b' > 'a' na primeira posição

# Verificando o valor Unicode:
print(ord("A"))   # 65
print(ord("a"))   # 97
print(ord("Z"))   # 90

# Para comparação case-insensitive:
s1, s2 = "Python", "python"
print(s1 == s2)              # False — maiúscula diferente
print(s1.lower() == s2.lower())  # True  — normaliza antes

# -----------------------------------------------------------------------------
# 4. Comparação de listas e tuplas — lexicográfica elemento a elemento
# -----------------------------------------------------------------------------

print([1, 2, 3] == [1, 2, 3])   # True
print([1, 2, 3] <  [1, 2, 4])   # True  — 3 < 4 na posição 2
print([1, 2]    <  [1, 2, 0])   # True  — lista menor é "menor" se prefixo
print([1, 3]    >  [1, 2, 999]) # True  — 3 > 2 na posição 1, para aí

# -----------------------------------------------------------------------------
# 5. Comparação com None
# None só é igual a None.
# NUNCA use > < >= <= com None — TypeError em Python 3.
# -----------------------------------------------------------------------------

print(None == None)    # True
print(None == False)   # False
print(None == 0)       # False
print(None is None)    # True  — forma idiomática (use 'is', não '==')

# None < 5  ← TypeError: '<' not supported between 'NoneType' and 'int'

# -----------------------------------------------------------------------------
# 6. Comparação entre tipos diferentes
# Em Python 3, comparar tipos incompatíveis com <, >, etc. lança TypeError.
# Python 2 permitia isso silenciosamente — era um bug famoso.
# -----------------------------------------------------------------------------

print(1 == "1")       # False — sem erro, mas sem coerção
print(1 == True)      # True  — bool é subclasse de int
print(0 == False)     # True
print(1 == 1.0)       # True  — int e float são comparáveis

# "1" > 1  ← TypeError: '>' not supported between 'str' and 'int'

# -----------------------------------------------------------------------------
# 7. Retorno de comparações é bool — pode ser usado diretamente
# -----------------------------------------------------------------------------

resultado = (5 > 3)
print(resultado)          # True
print(type(resultado))    # <class 'bool'>

# Somando booleanos (herança de int):
notas = [7, 8, 4, 9, 3]
aprovados = sum(nota >= 5 for nota in notas)
print(f"Aprovados: {aprovados}")   # 3

# -----------------------------------------------------------------------------
# 8. __eq__ — comparação é um protocolo, não magia
# Qualquer classe pode sobrescrever o comportamento de ==
# -----------------------------------------------------------------------------

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, outro):
        return self.x == outro.x and self.y == outro.y

p1 = Ponto(1, 2)
p2 = Ponto(1, 2)
p3 = Ponto(3, 4)

print(p1 == p2)   # True  — __eq__ customizado
print(p1 == p3)   # False
