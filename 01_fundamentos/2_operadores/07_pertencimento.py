# =============================================================================
# 07_pertencimento.py — Operadores de Pertencimento
# in  /  not in
# Verificação de presença em coleções — e por que a escolha da estrutura importa.
# =============================================================================

# -----------------------------------------------------------------------------
# 1. Sintaxe básica
# elemento in coleção   → True se elemento pertence à coleção
# elemento not in coleção → True se elemento NÃO pertence
# -----------------------------------------------------------------------------

print(3 in [1, 2, 3, 4])      # True
print(5 in [1, 2, 3, 4])      # False
print(5 not in [1, 2, 3, 4])  # True

# -----------------------------------------------------------------------------
# 2. Comportamento em cada tipo de coleção
# -----------------------------------------------------------------------------

# LIST — O(n): percorre do início ao fim até encontrar
lista = [10, 20, 30, 40, 50]
print(30 in lista)    # True
print(99 in lista)    # False

# TUPLE — O(n): idêntico à lista
tupla = (10, 20, 30)
print(20 in tupla)    # True

# SET — O(1) amortizado: usa tabela hash, lookup instantâneo
conjunto = {10, 20, 30, 40, 50}
print(30 in conjunto)   # True  — muito mais rápido que lista para grandes volumes
print(99 in conjunto)   # False

# DICT — O(1) amortizado: verifica nas CHAVES por padrão
dicionario = {"nome": "Yvan", "idade": 16, "ativo": True}
print("nome"  in dicionario)   # True  — verifica chaves
print("Yvan"  in dicionario)   # False — "Yvan" é valor, não chave
print("Yvan"  in dicionario.values())  # True — verificar valores: O(n)
print(("nome", "Yvan") in dicionario.items())  # True — par chave-valor

# STRING — O(n): verifica substring
texto = "Python é poderoso"
print("Python" in texto)      # True
print("Java"   in texto)      # False
print("é"      in texto)      # True — caractere simples
print(""       in texto)      # True — string vazia sempre está contida
print("po"     in "poderoso") # True — substring

# RANGE — O(1): calcula matematicamente sem iterar
intervalo = range(1, 1_000_000)
print(999_999 in intervalo)   # True  — instantâneo, não itera 1M de elementos
print(1_000_000 in intervalo) # False

# -----------------------------------------------------------------------------
# 3. Complexidade de tempo — a escolha da estrutura define a performance
# -----------------------------------------------------------------------------

import time

tamanho = 100_000
lista_grande   = list(range(tamanho))
set_grande     = set(range(tamanho))
alvo           = tamanho - 1   # pior caso para lista (último elemento)

# Benchmark: list vs set
inicio = time.perf_counter()
for _ in range(1000):
    _ = alvo in lista_grande
tempo_lista = time.perf_counter() - inicio

inicio = time.perf_counter()
for _ in range(1000):
    _ = alvo in set_grande
tempo_set = time.perf_counter() - inicio

print(f"Lista: {tempo_lista:.4f}s")
print(f"Set:   {tempo_set:.6f}s")
print(f"Set é ~{tempo_lista / tempo_set:.0f}x mais rápido (pior caso)")

# Regra: se você vai fazer múltiplos 'in' em uma coleção → use set.
# O custo de converter list → set é O(n), mas cada lookup depois é O(1).

ids_validos = [1, 5, 7, 12, 44, 99, 200]
ids_set = set(ids_validos)   # converte uma vez

requisicoes = [5, 200, 999, 7, 1000, 1]
for req in requisicoes:
    if req in ids_set:   # O(1) por verificação
        print(f"  ID {req}: autorizado")
    else:
        print(f"  ID {req}: negado")

# -----------------------------------------------------------------------------
# 4. 'in' com strings — distinção importante
# Verifica SUBSTRING, não apenas caractere.
# -----------------------------------------------------------------------------

email = "yvan@exemplo.com"
print("@"        in email)   # True
print(".com"     in email)   # True  — substring
print("exemplo"  in email)   # True
print("gmail"    in email)   # False

# Uso: validação simples de formato
def email_valido_simples(e):
    return "@" in e and "." in e.split("@")[-1]

print(email_valido_simples("yvan@gmail.com"))  # True
print(email_valido_simples("invalido.com"))    # False
print(email_valido_simples("@sem.dominio"))    # True (limitação da validação simples)

# Para validação real de email, use: re.match() ou bibliotecas dedicadas.

# -----------------------------------------------------------------------------
# 5. 'in' em loops — iteração
# O operador 'in' também é o mecanismo de iteração do for.
# -----------------------------------------------------------------------------

frutas = ["maçã", "banana", "uva"]
for fruta in frutas:       # 'in' aqui é iteração, não busca
    print(fruta)

# É o mesmo protocolo: Python chama __iter__ e __contains__ por baixo.

# -----------------------------------------------------------------------------
# 6. __contains__ — o protocolo por trás de 'in'
# Qualquer classe pode definir o comportamento de 'in'.
# -----------------------------------------------------------------------------

class Intervalo:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim    = fim

    def __contains__(self, valor):
        return self.inicio <= valor <= self.fim

    def __repr__(self):
        return f"Intervalo({self.inicio}, {self.fim})"

adultos = Intervalo(18, 64)
print(20 in adultos)    # True  — chama __contains__
print(17 in adultos)    # False
print(65 in adultos)    # False

# -----------------------------------------------------------------------------
# 7. Padrões idiomáticos com 'in'
# -----------------------------------------------------------------------------

# Verificar múltiplos valores:
status = "ativo"
if status in ("ativo", "pendente", "revisao"):   # tupla é mais rápida que lista para isso
    print("Status válido")

# Substituir múltiplos 'or':
# ❌ verboso:
if status == "ativo" or status == "pendente" or status == "revisao":
    pass

# ✅ Pythônico:
if status in {"ativo", "pendente", "revisao"}:   # set → O(1)
    pass

# Filtrar elementos presentes em outra coleção:
permitidos = {"admin", "editor", "viewer"}
usuarios   = ["admin", "hacker", "editor", "root"]
validos    = [u for u in usuarios if u in permitidos]
print(validos)   # ['admin', 'editor']
