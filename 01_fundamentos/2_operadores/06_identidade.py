# =============================================================================
# 06_identidade.py — Operadores de Identidade
# is  /  is not
# Compara ENDEREÇOS DE MEMÓRIA, não valores. A distinção que junior ignora.
# =============================================================================

# -----------------------------------------------------------------------------
# 1. Diferença fundamental: == vs is
# ==  → chama __eq__ → compara VALOR
# is  → compara id() → compara IDENTIDADE (mesmo objeto na memória)
# -----------------------------------------------------------------------------

a = [1, 2, 3]
b = [1, 2, 3]   # lista diferente, mas com o mesmo conteúdo
c = a           # c aponta para O MESMO objeto que a

print(a == b)   # True  — valores iguais
print(a is b)   # False — objetos distintos na memória
print(a is c)   # True  — mesmo objeto

print(id(a))    # ex: 140234567890
print(id(b))    # ex: 140234567910  ← diferente
print(id(c))    # mesmo que id(a)

# Consequência crítica: modificar c modifica a
c.append(4)
print(a)   # [1, 2, 3, 4] ← a foi alterada!

# -----------------------------------------------------------------------------
# 2. is not — negação de identidade
# -----------------------------------------------------------------------------

x = [1, 2]
y = [1, 2]

print(x is not y)    # True  — objetos distintos
print(x is not x)    # False — x é o mesmo que x

# -----------------------------------------------------------------------------
# 3. Onde usar 'is': None, True, False e singletons
# None é um SINGLETON — existe um único objeto None em todo o programa.
# -----------------------------------------------------------------------------

valor = None

# ✅ Correto e idiomático:
print(valor is None)       # True
print(valor is not None)   # False

# ⚠️ Funciona, mas não é idiomático:
print(valor == None)    # True — mas sobrecarregável via __eq__

# Por que 'is None' é mais correto?
# Qualquer classe pode redefinir __eq__ para retornar True ao comparar com None.
# 'is' nunca pode ser enganado — verifica o endereço diretamente.

class Enganador:
    def __eq__(self, outro):
        return True   # "igual" a tudo, inclusive None

obj = Enganador()
print(obj == None)    # True  — __eq__ customizado
print(obj is None)    # False — identidade real

# -----------------------------------------------------------------------------
# 4. Small int cache — comportamento que confunde juniors
# Python mantém objetos pré-criados para inteiros de -5 a 256.
# Isso faz 'is' retornar True para esses valores, mas é um DETALHE DE IMPLEMENTAÇÃO.
# NUNCA use 'is' para comparar inteiros ou strings.
# -----------------------------------------------------------------------------

a = 100
b = 100
print(a is b)   # True  — CPython reutiliza o objeto (cache)

a = 1000
b = 1000
print(a is b)   # False — fora do cache, objetos distintos

# O comportamento VARIA entre implementações (CPython, PyPy, Jython).
# É um detalhe de otimização, não uma garantia da linguagem.

# -----------------------------------------------------------------------------
# 5. String interning — mesmo fenômeno para strings
# Strings curtas e "identifier-like" são internadas (compartilhadas).
# -----------------------------------------------------------------------------

s1 = "python"
s2 = "python"
print(s1 is s2)   # True  — internada (detalhe de implementação do CPython)

s1 = "python é legal"
s2 = "python é legal"
print(s1 is s2)   # False (geralmente) — string com espaço não é internada

# sys.intern() força o interning de qualquer string:
import sys
s1 = sys.intern("python é legal")
s2 = sys.intern("python é legal")
print(s1 is s2)   # True — agora compartilham o mesmo objeto

# Uso real: dicionários com muitas chaves repetidas podem se beneficiar de intern.

# -----------------------------------------------------------------------------
# 6. Casos de uso legítimos de 'is'
# -----------------------------------------------------------------------------

# ✅ 1. Verificar None
def processar(dado=None):
    if dado is None:
        print("Nenhum dado fornecido")
        return
    print(f"Processando: {dado}")

processar()
processar(42)

# ✅ 2. Verificar singletons True/False (raro, mas existente)
resultado = True
if resultado is True:
    print("Exatamente True, não apenas truthy")

# ✅ 3. Verificar identidade de objetos em estruturas de dados
lista = [[1, 2], [3, 4]]
sub  = lista[0]
print(sub is lista[0])   # True — mesmo objeto

# ✅ 4. Sentinelas personalizadas (padrão avançado)
_NULO = object()   # objeto único, diferente de None, False, 0, ""

def buscar(chave, padrao=_NULO):
    dicionario = {"a": 0, "b": False, "c": None}
    resultado = dicionario.get(chave, _NULO)
    if resultado is _NULO:
        print(f"Chave '{chave}' não existe")
    else:
        print(f"Valor encontrado: {repr(resultado)}")

buscar("a")   # Valor encontrado: 0     (0 seria falsy, mas não é _NULO)
buscar("b")   # Valor encontrado: False (seria falsy, mas não é _NULO)
buscar("c")   # Valor encontrado: None  (é None, mas não é _NULO)
buscar("z")   # Chave 'z' não existe

# -----------------------------------------------------------------------------
# 7. Regra final: quando usar cada um
# == para comparar VALORES    → sempre (exceto singletons)
# is para comparar IDENTIDADE → None, True, False, sentinelas
# -----------------------------------------------------------------------------
