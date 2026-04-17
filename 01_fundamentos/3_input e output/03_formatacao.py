# =============================================================================
# 03_formatacao.py — Formatação de Strings
# f-string  |  .format()  |  concatenação com +
# Como exibir valores de forma legível e controlada.
# =============================================================================

nome  = "Yvan"
idade = 16
pi    = 3.14159265
saldo = 1500.5

# -----------------------------------------------------------------------------
# 1. Concatenação com + (o jeito básico — e por que não é o melhor)
# -----------------------------------------------------------------------------

# Funciona, mas exige conversão manual de int/float para str:
print("Nome: " + nome)                        # ok — nome já é str
print("Idade: " + str(idade))                 # precisa de str()
print("Pi: " + str(pi))                       # precisa de str()

# Problemas:
# - Verboso (str() em todo número)
# - Difícil de controlar casas decimais
# - Propenso a erros (esquecer o str() causa TypeError)

# Por isso existem formas melhores:

# -----------------------------------------------------------------------------
# 2. f-string (Python 3.6+) — o padrão moderno
# Prefixo f antes das aspas. Variáveis e expressões vão dentro de {}.
# -----------------------------------------------------------------------------

# Interpolação básica:
print(f"Nome: {nome}")                        # Nome: Yvan
print(f"Idade: {idade}")                      # Idade: 16
print(f"{nome} tem {idade} anos")             # Yvan tem 16 anos

# Expressões dentro das chaves:
print(f"Dobro da idade: {idade * 2}")         # 32
print(f"Maior de idade: {idade >= 18}")       # False
print(f"Nome em maiúsculas: {nome.upper()}")  # YVAN

# -----------------------------------------------------------------------------
# 3. Especificadores de formato — controlando como o valor aparece
# Sintaxe: {valor:formato}
# -----------------------------------------------------------------------------

# --- Casas decimais com :.Nf ---
print(f"{pi:.2f}")     # 3.14     — 2 casas decimais
print(f"{pi:.4f}")     # 3.1416   — 4 casas decimais
print(f"{pi:.0f}")     # 3        — 0 casas (arredonda)

print(f"{saldo:.2f}")  # 1500.50  — útil para valores monetários

# --- Largura mínima com :N ---
print(f"{idade:10}")       # '        16'  — ocupa 10 espaços, alinhado à direita
print(f"{nome:10}")        # 'Yvan      '  — str alinha à esquerda por padrão

# --- Alinhamento com < > ^ ---
print(f"{'esquerda':<15}|")    # esquerda       |
print(f"{'direita':>15}|")     #         direita|
print(f"{'centro':^15}|")      #     centro     |

# --- Zero-padding com :0N ---
dia = 5
mes = 3
print(f"{dia:02d}/{mes:02d}/2026")   # 05/03/2026  — útil para datas

# --- Separador de milhar com :, ---
valor_grande = 1000000
print(f"{valor_grande:,}")     # 1,000,000

# --- Percentual com :.N% ---
taxa = 0.075
print(f"{taxa:.1%}")           # 7.5%
print(f"{taxa:.0%}")           # 8%   (arredonda)

# --- Combinando largura e casas decimais ---
print(f"{pi:10.3f}")    # '     3.142'  — largura 10, 3 casas decimais

# -----------------------------------------------------------------------------
# 4. f-string de debug com nome= (Python 3.8+)
# Imprime o nome da variável e seu valor automaticamente.
# -----------------------------------------------------------------------------

x = 42
resultado = x * 2

print(f"{x=}")           # x=42
print(f"{resultado=}")   # resultado=84
print(f"{nome=}")        # nome='Yvan'

# Equivale a escrever: print(f"x = {x}, resultado = {resultado}")
# Muito útil para entender o que está acontecendo no programa.

# -----------------------------------------------------------------------------
# 5. .format() — o jeito anterior ao f-string
# Você vai encontrar isso em código mais antigo.
# Entenda para ler, mas escreva sempre com f-string.
# -----------------------------------------------------------------------------

# Por posição (ordem dos argumentos):
print("Nome: {}, Idade: {}".format(nome, idade))

# Por índice:
print("{0} tem {1} anos. {0} estuda Python.".format(nome, idade))

# Por nome:
print("Nome: {n}, Idade: {i}".format(n=nome, i=idade))

# Especificadores funcionam igual ao f-string:
print("Pi: {:.2f}".format(pi))
print("{:>10}".format("direita"))

# Quando .format() ainda é necessário:
# Quando o template é uma variável (não dá para usar f-string nesse caso).
template_pt = "Olá, {}! Você tem {} anos."
template_en = "Hello, {}! You are {} years old."

idioma = "pt"

if idioma == "pt":
    print(template_pt.format(nome, idade))
else:
    print(template_en.format(nome, idade))

# Com f-string isso não funciona porque o {} do template seria interpretado
# no momento da criação da string — não depois, quando você tem o valor.

# -----------------------------------------------------------------------------
# 6. Formatação de strings diretamente (métodos de str)
# Sem precisar de f-string ou .format()
# -----------------------------------------------------------------------------

texto = "python"

print(texto.upper())        # PYTHON
print(texto.capitalize())   # Python   — primeira letra maiúscula
print(texto.title())        # Python   — cada palavra começa com maiúscula

frase = "  espaços nas bordas  "
print(frase.strip())        # 'espaços nas bordas'
print(frase.lstrip())       # 'espaços nas bordas  '
print(frase.rstrip())       # '  espaços nas bordas'

print("python".replace("py", "PY"))   # PYthon

# Verificações úteis:
print("123".isdigit())      # True  — só dígitos
print("abc".isalpha())      # True  — só letras
print("abc123".isalnum())   # True  — letras e/ou dígitos
print("  ".isspace())       # True  — só espaços

# Comprimento:
print(len("Python"))        # 6
print(len(""))              # 0

# -----------------------------------------------------------------------------
# 7. Qual forma usar — resumo direto
# -----------------------------------------------------------------------------

# f-string   → sempre, no código que você escrever
# .format()  → para ler código antigo ou quando o template é uma variável
# + (concat) → apenas para unir duas strings simples sem formatação especial

# Especificadores mais usados (decorar esses):
# :.Nf  → N casas decimais        (f"{3.14159:.2f}" → "3.14")
# :Nd   → largura N, inteiro      (f"{5:02d}"       → "05")
# :,    → separador de milhar     (f"{1000000:,}"   → "1,000,000")
# :.N%  → percentual              (f"{0.07:.0%}"    → "7%")
# :<N   → alinhado à esquerda
# :>N   → alinhado à direita
# :^N   → centralizado
