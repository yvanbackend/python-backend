# =============================================================================
# 01_variaveis.py — Variáveis em Python
# O que são, como funcionam e o que o Python faz por baixo dos panos.
# =============================================================================

# -----------------------------------------------------------------------------
# 1. O que é uma variável?
# Em Python, uma variável é um RÓTULO que aponta para um objeto na memória.
# Não existe "caixa com valor dentro" — existe um objeto e um nome que o referencia.
# -----------------------------------------------------------------------------

nome = "Yvan"           # str
idade = 16              # int
altura = 1.75           # float
ativo = True            # bool

# Verificando o tipo de cada variável
print(type(nome))       # <class 'str'>
print(type(idade))      # <class 'int'>
print(type(altura))     # <class 'float'>
print(type(ativo))      # <class 'bool'>

# -----------------------------------------------------------------------------
# 2. Tipagem Dinâmica
# Python é dinamicamente tipado: a variável pode mudar de tipo em runtime.
# Isso é flexível, mas é uma fonte clássica de bugs silenciosos.
# -----------------------------------------------------------------------------

x = 10
print(type(x))   # <class 'int'>

x = "agora sou string"
print(type(x))   # <class 'str'>

# -----------------------------------------------------------------------------
# 3. Tipagem Forte
# Apesar de dinâmico, Python é FORTEMENTE tipado.
# Ele não faz coerção implícita entre tipos incompatíveis.
# -----------------------------------------------------------------------------

# print("Tenho " + 16 + " anos")  # ← TypeError: must be str, not int
print("Tenho " + str(16) + " anos")  # Correto: conversão explícita

# -----------------------------------------------------------------------------
# 4. Múltiplas atribuições
# -----------------------------------------------------------------------------

a, b, c = 1, 2, 3          # Desempacotamento
x = y = z = 0              # Mesmo objeto referenciado por três nomes

print(a, b, c)             # 1 2 3
print(x, y, z)             # 0 0 0

# -----------------------------------------------------------------------------
# 5. Convenção de nomenclatura (PEP 8)
# -----------------------------------------------------------------------------

# ✅ snake_case para variáveis e funções
nome_completo = "Yvan Oliveira"

# ✅ SCREAMING_SNAKE_CASE para constantes
LIMITE_MAXIMO = 100

# ❌ Evite: nomes sem significado
# x1 = 42  ← o que isso representa?

# -----------------------------------------------------------------------------
# 6. id() — endereço do objeto na memória
# Demonstra que variáveis são referências, não caixas.
# -----------------------------------------------------------------------------

a = 10
b = 10
print(id(a) == id(b))  # True — Python reutiliza objetos pequenos (int cache)

a = [1, 2, 3]
b = [1, 2, 3]
print(id(a) == id(b))  # False — listas são objetos distintos
