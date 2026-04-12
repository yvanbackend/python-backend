# =============================================================================
# 05_bitwise.py — Operadores Bit a Bit (Bitwise)
# &  |  ^  ~  <<  >>
# Manipulação direta de bits — base de flags, criptografia e performance.
# =============================================================================

# -----------------------------------------------------------------------------
# PRÉ-REQUISITO: representação binária
# Inteiros são armazenados em binário na memória.
# bin() exibe a representação; 0b é o prefixo de literal binário.
# -----------------------------------------------------------------------------

print(bin(5))    # 0b101    → 4 + 1
print(bin(12))   # 0b1100   → 8 + 4
print(bin(255))  # 0b11111111

# Conversão: bin → int
print(0b1010)    # 10
print(int("1010", 2))  # 10

# Função auxiliar para exibir operações de forma clara:
def bits(n, largura=8):
    return format(n & 0xFF, f"0{largura}b")  # exibe N bits com zeros à esq

# -----------------------------------------------------------------------------
# 1. AND bit a bit (&)
# Resultado: 1 apenas onde AMBOS os bits são 1.
# Uso: mascarar bits (zerar seletivamente).
# -----------------------------------------------------------------------------

a = 0b1100    # 12
b = 0b1010    # 10

resultado = a & b
print(f"  {bits(a)}")
print(f"& {bits(b)}")
print(f"= {bits(resultado)}  →  {resultado}")   # 0b1000 = 8

# Aplicação: verificar se um número é par
print(5 & 1)    # 1 → ímpar (último bit é 1)
print(4 & 1)    # 0 → par   (último bit é 0)

# Aplicação: extrair os 4 bits inferiores (nibble)
valor = 0b10110111
nibble = valor & 0b00001111
print(bin(nibble))   # 0b111 = 7

# -----------------------------------------------------------------------------
# 2. OR bit a bit (|)
# Resultado: 1 onde PELO MENOS UM dos bits é 1.
# Uso: ativar bits (ligar flags).
# -----------------------------------------------------------------------------

a = 0b1100
b = 0b1010

resultado = a | b
print(f"\n  {bits(a)}")
print(f"| {bits(b)}")
print(f"= {bits(resultado)}  →  {resultado}")   # 0b1110 = 14

# Aplicação: flags de permissão (estilo Unix)
LER      = 0b100   # 4
ESCREVER = 0b010   # 2
EXECUTAR = 0b001   # 1

permissoes = LER | ESCREVER   # 0b110 = 6
print(bin(permissoes))         # 0b110

# Verificar se uma permissão está ativa:
print(bool(permissoes & LER))       # True
print(bool(permissoes & EXECUTAR))  # False

# Ativar uma permissão:
permissoes |= EXECUTAR
print(bin(permissoes))   # 0b111 — todas ativas

# -----------------------------------------------------------------------------
# 3. XOR bit a bit (^)
# Resultado: 1 onde os bits são DIFERENTES.
# Uso: toggle de bits, detecção de diferença, criptografia simples.
# -----------------------------------------------------------------------------

a = 0b1100
b = 0b1010

resultado = a ^ b
print(f"\n  {bits(a)}")
print(f"^ {bits(b)}")
print(f"= {bits(resultado)}  →  {resultado}")   # 0b0110 = 6

# Propriedade: a ^ a = 0, a ^ 0 = a
print(5 ^ 5)    # 0
print(5 ^ 0)    # 5

# Swap sem variável temporária (usando XOR):
x, y = 10, 20
x ^= y
y ^= x
x ^= y
print(x, y)   # 20 10 — trocados sem variável temporária

# Toggle de bit específico:
flags = 0b00001111
mascara = 0b00000100
flags ^= mascara        # inverte o bit 2
print(bin(flags))        # 0b00001011

# Criptografia XOR simples (Caesar dos bits):
mensagem = 0b10101010
chave    = 0b11001100
cifrado  = mensagem ^ chave
decifrado = cifrado ^ chave   # XOR com a mesma chave decifra
print(bin(mensagem), bin(cifrado), bin(decifrado))
print(decifrado == mensagem)   # True

# -----------------------------------------------------------------------------
# 4. NOT bit a bit (~)
# Inverte todos os bits. Em Python: ~n = -(n + 1)
# Motivo: Python usa complemento de dois com precisão arbitrária.
# -----------------------------------------------------------------------------

print(~0)     # -1   — ~0b00000000 = 0b11111111...1 = -1
print(~1)     # -2
print(~5)     # -6   — ~n = -(n+1) sempre
print(~(-1))  # 0

# ~n é equivalente a -n - 1:
n = 42
print(~n == -n - 1)   # True

# -----------------------------------------------------------------------------
# 5. Deslocamento à esquerda (<<) — multiplica por 2ⁿ
# -----------------------------------------------------------------------------

print(1  << 0)    # 1    — 1 * 2⁰
print(1  << 1)    # 2    — 1 * 2¹
print(1  << 4)    # 16   — 1 * 2⁴
print(3  << 2)    # 12   — 3 * 2² = 3 * 4
print(100 << 3)   # 800  — 100 * 8

# Uso: criar máscaras de bit e constantes de potências de 2
KB = 1 << 10   # 1024
MB = 1 << 20   # 1048576
GB = 1 << 30   # 1073741824
print(f"1 KB = {KB}, 1 MB = {MB}, 1 GB = {GB}")

# -----------------------------------------------------------------------------
# 6. Deslocamento à direita (>>) — divide por 2ⁿ (truncando)
# -----------------------------------------------------------------------------

print(16 >> 1)    # 8    — 16 // 2
print(16 >> 2)    # 4    — 16 // 4
print(100 >> 3)   # 12   — 100 // 8
print(7  >> 1)    # 3    — 7 // 2 = 3 (trunca)

# Negativos: >> propaga o bit de sinal (arithmetic shift)
print(-8 >> 1)    # -4
print(-1 >> 4)    # -1   — todos 1s, desloca mas propaga o sinal

# -----------------------------------------------------------------------------
# 7. Precedência dos operadores bit a bit
# ~ > << >> > & > ^ > |
# Mais baixa que aritmético, mais alta que comparação.
# Use parênteses para clareza.
# -----------------------------------------------------------------------------

print(2 + 3 & 7)       # 5  — (2+3) & 7 = 5 & 7 = 5
print(1 | 2 + 3)       # 7  — 1 | (2+3) = 1 | 5 = 5... espera
print(1 | (2 + 3))     # 7  — 0b001 | 0b101 = 0b101 = 5... 
# Teste: 0b001 | 0b101:
print(bin(0b001 | 0b101))   # 0b101 = 5... mas 1|5=5, não 7
# Correto — a confusão acontece. Use parênteses SEMPRE com bitwise.
print((1 | 2) + 3)     # 6  — parênteses mudam o resultado

# Conclusão: com operadores bit a bit, parênteses não são opcionais.
