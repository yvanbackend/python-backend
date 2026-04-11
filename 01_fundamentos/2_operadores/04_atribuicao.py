# =============================================================================
# 04_atribuicao.py — Operadores de Atribuição
# =  +=  -=  *=  /=  //=  %=  **=  &=  |=  ^=  >>=  <<=  :=
# O que cada um faz por baixo dos panos e quando usar cada forma.
# =============================================================================

# -----------------------------------------------------------------------------
# 1. Atribuição simples (=)
# Não copia um valor — cria um RÓTULO que aponta para um objeto.
# -----------------------------------------------------------------------------

x = 10           # x aponta para o objeto int 10
nome = "Yvan"    # nome aponta para o objeto str 'Yvan'
lista = [1, 2]   # lista aponta para um objeto list

# Atribuição múltipla (mesmo objeto)
a = b = c = 0
print(a, b, c)       # 0 0 0
print(id(a) == id(b) == id(c))  # True — todos apontam para o MESMO objeto

# Isso importa para objetos mutáveis:
x = y = []
x.append(1)
print(y)   # [1] ← y também foi afetado! Ambos apontam para a mesma lista.

# Solução: criar objetos separados
x = []
y = []
x.append(1)
print(y)   # [] ← y independente

# Desempacotamento (unpacking)
a, b, c = 1, 2, 3
print(a, b, c)   # 1 2 3

primeiro, *resto = [10, 20, 30, 40]
print(primeiro)  # 10
print(resto)     # [20, 30, 40]

*inicio, ultimo = [10, 20, 30, 40]
print(inicio)    # [10, 20, 30]
print(ultimo)    # 40

# Swap sem variável temporária (Pythônico)
a, b = 1, 2
a, b = b, a
print(a, b)   # 2 1

# -----------------------------------------------------------------------------
# 2. Operadores de atribuição composta
# x += y  é equivalente a  x = x + y  MAS pode ser mais eficiente
# para tipos mutáveis (como list), pois usa __iadd__ (in-place).
# -----------------------------------------------------------------------------

# += adição composta
x = 10
x += 5
print(x)   # 15

# -= subtração composta
x -= 3
print(x)   # 12

# *= multiplicação composta
x *= 2
print(x)   # 24

# /= divisão composta — resultado SEMPRE float
x /= 4
print(x)        # 6.0
print(type(x))  # <class 'float'>

# //= divisão inteira composta
x = 17
x //= 5
print(x)   # 3

# %= módulo composto
x = 17
x %= 5
print(x)   # 2

# **= exponenciação composta
x = 2
x **= 8
print(x)   # 256

# -----------------------------------------------------------------------------
# 3. In-place vs nova referência — diferença crítica para tipos mutáveis
# -----------------------------------------------------------------------------

# Para LISTAS: += usa __iadd__ (modifica o objeto existente)
lista_a = [1, 2]
lista_b = lista_a
lista_a += [3, 4]
print(lista_a)          # [1, 2, 3, 4]
print(lista_b)          # [1, 2, 3, 4] ← lista_b também foi afetada (mesmo objeto)

# Para STRINGS (imutáveis): += cria um NOVO objeto
s1 = "ab"
s2 = s1
s1 += "cd"
print(s1)           # 'abcd'
print(s2)           # 'ab' ← s2 não mudou (string é imutável)
print(id(s1) == id(s2))  # False — s1 agora aponta para novo objeto

# -----------------------------------------------------------------------------
# 4. Operadores de atribuição bit a bit composta
# (explicação completa dos operadores bit a bit: ver 05_bitwise.py)
# -----------------------------------------------------------------------------

# &=  AND bit a bit
flags = 0b1111
flags &= 0b1010
print(bin(flags))   # 0b1010

# |=  OR bit a bit
flags = 0b1010
flags |= 0b0101
print(bin(flags))   # 0b1111

# ^=  XOR bit a bit
flags = 0b1111
flags ^= 0b1010
print(bin(flags))   # 0b101

# >>= deslocamento à direita
x = 16
x >>= 2
print(x)   # 4  (16 // 2² = 4)

# <<= deslocamento à esquerda
x = 4
x <<= 2
print(x)   # 16  (4 * 2² = 16)

# -----------------------------------------------------------------------------
# 5. Walrus Operator := (Python 3.8+) — atribuição dentro de expressão
# Permite atribuir e usar o valor na mesma expressão.
# -----------------------------------------------------------------------------

# Sem walrus — lê a lista duas vezes ou usa variável extra
numeros = [1, 2, 3, 4, 5]
n = len(numeros)
if n > 3:
    print(f"Lista grande: {n} elementos")

# Com walrus — atribui e testa em uma linha
if (n := len(numeros)) > 3:
    print(f"Lista grande: {n} elementos")

# Uso clássico: processar dados de entrada sem repetir chamada
import re
texto = "Yvan tem 16 anos"
if m := re.search(r"\d+", texto):
    print(f"Número encontrado: {m.group()}")   # 16

# Uso em while — substitui padrão verbose de leitura em loop
dados = [10, 20, 0, 30, 40]
i = 0
while (valor := dados[i]) != 0:
    print(f"Processando: {valor}")
    i += 1
# Para em 0

# ⚠️ Walrus não substitui = em atribuições normais.
# Use apenas quando a atribuição DENTRO da expressão reduz duplicação real.
# Abuso gera código ilegível.
