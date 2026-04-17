# =============================================================================
# 02_input.py — Entrada de Dados com input()
# input(prompt='') → str
# SEMPRE retorna str. Conversão é responsabilidade do programador.
# =============================================================================

# -----------------------------------------------------------------------------
# 1. Comportamento fundamental
# input() exibe o prompt, aguarda o usuário digitar e pressionar Enter,
# e retorna tudo que foi digitado como str (sem o \n do Enter).
# -----------------------------------------------------------------------------

nome = input("Qual seu nome? ")
print("Você digitou:", nome)
print("Tipo:", type(nome))    # sempre <class 'str'>

# -----------------------------------------------------------------------------
# 2. O erro mais comum: esquecer que input() retorna str
# -----------------------------------------------------------------------------

# Isso vai dar erro:
# idade = input("Sua idade: ")
# print(idade + 1)   # TypeError: can only concatenate str (not "int") to str

# Porque "16" (str) + 1 (int) não faz sentido para o Python.
# Você precisa converter explicitamente:

entrada = input("Sua idade: ")    # retorna "16" (str)
idade   = int(entrada)            # converte para 16 (int)
print("Em 10 anos você terá:", idade + 10)

# Forma compacta (mais comum na prática):
idade = int(input("Sua idade: "))
print("Em 10 anos você terá:", idade + 10)

# -----------------------------------------------------------------------------
# 3. Tipos de conversão mais usados
# -----------------------------------------------------------------------------

# int() — para números inteiros:
quantidade = int(input("Quantos itens? "))
print("Total com taxa:", quantidade + 2)

# float() — para números decimais:
altura = float(input("Sua altura em metros (ex: 1.75): "))
print("Altura em cm:", altura * 100)

# str() — raramente necessário, pois input() já retorna str.
# Mas é útil para converter outros tipos em string:
numero = 42
texto  = str(numero)
print(type(texto))   # <class 'str'>

# O que NÃO funciona para bool:
# bool(input("Ativo? "))  — qualquer string não-vazia retorna True
# "False" como str → bool("False") = True  ← armadilha!
# Você vai aprender a lidar com isso quando chegar em controle de fluxo.

# -----------------------------------------------------------------------------
# 4. .strip() — limpando espaços acidentais
# O usuário frequentemente digita espaços antes ou depois do valor.
# -----------------------------------------------------------------------------

entrada = input("Seu nome: ")         # usuário digita "  Yvan  "
print(repr(entrada))                  # '  Yvan  '  ← espaços visíveis

entrada_limpa = entrada.strip()       # remove espaços das bordas
print(repr(entrada_limpa))            # 'Yvan'

# Na prática, sempre use .strip() ao ler texto:
nome = input("Seu nome: ").strip()
print("Olá,", nome)

# Variações de strip():
texto = "   python   "
print(repr(texto.lstrip()))    # 'python   '  — remove só da esquerda
print(repr(texto.rstrip()))    # '   python'  — remove só da direita
print(repr(texto.strip()))     # 'python'     — remove dos dois lados

# -----------------------------------------------------------------------------
# 5. Validação simples com if/elif
# input() não garante que o usuário digitou o que você espera.
# Com o que você já sabe (if/elif), dá para fazer validações diretas.
# -----------------------------------------------------------------------------

resposta = input("Você é maior de idade? (s/n): ").strip().lower()

if resposta == "s":
    print("Acesso liberado.")
elif resposta == "n":
    print("Acesso negado.")
else:
    print("Resposta inválida. Digite s ou n.")

# .lower() converte para minúsculas — assim "S", "s", não importa:
opcao = input("Continuar? (s/n): ").strip().lower()
print("Você digitou:", opcao)

# -----------------------------------------------------------------------------
# 6. Validação com while — repetir até receber entrada válida
# ⚠ VOCÊ JÁ VIU while — mas se ainda não tiver seguro, leia os comentários.
# while repete o bloco enquanto a condição for verdadeira.
# -----------------------------------------------------------------------------

# Repetir até o usuário digitar um número inteiro válido:
entrada_valida = False
numero = 0

while not entrada_valida:
    entrada = input("Digite um número inteiro: ").strip()
    if entrada.lstrip("-").isdigit():   # isdigit() checa se é só dígitos
        numero = int(entrada)
        entrada_valida = True
    else:
        print("Isso não é um número inteiro. Tente novamente.")

print("Número aceito:", numero)

# Repetir até o usuário digitar s ou n:
resposta_valida = False

while not resposta_valida:
    resposta = input("Continuar? (s/n): ").strip().lower()
    if resposta == "s" or resposta == "n":
        resposta_valida = True
    else:
        print("Digite apenas s ou n.")

print("Você escolheu:", resposta)

# -----------------------------------------------------------------------------
# 7. Lendo vários valores em sequência
# Basta chamar input() mais de uma vez.
# -----------------------------------------------------------------------------

print("--- Cadastro ---")
nome      = input("Nome: ").strip()
idade_str = input("Idade: ").strip()
cidade    = input("Cidade: ").strip()

idade = int(idade_str)

print("--- Resumo ---")
print("Nome:", nome)
print("Idade:", idade)
print("Cidade:", cidade)
print("Maior de idade:", idade >= 18)

# -----------------------------------------------------------------------------
# 8. Regras de ouro
# -----------------------------------------------------------------------------

# 1. input() SEMPRE retorna str — converta explicitamente com int() ou float()
# 2. Sempre use .strip() ao ler texto — usuários digitam espaços acidentalmente
# 3. Use .lower() ou .upper() para ignorar maiúsculas/minúsculas
# 4. Valide a entrada antes de converter — int("abc") causa erro
# 5. Use while para repetir até receber uma entrada válida
