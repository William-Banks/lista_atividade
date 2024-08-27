# Declaração das variáveis e armazenamento dos inputs do usuário
num1 = int(input(("Digite o primeiro número: ")))
num2 = int(input(("Digite o segundo número: ")))
num3 = int(input(("Digite o terceiro número: ")))

# Declaração da variável da média aritmética a partir de seu cálculo
media = (num1 + num2 + num3) / 3

# Impressão da média baseando-se nos números recebidos
print(f"A média aritmética dos números é: {media:.1f}")