# Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

texto = input("Escreva um texto: ")

texto_maiusculo = texto.upper()

print(texto_maiusculo)
# Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

nome = input("Escreva o seu nome completo: ")

nome_minusculo = nome.lower()

print(nome_minusculo)
# Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

frase = input("Escreva uma frase: ")

frase_strip = frase.strip()

print(frase_strip)
# Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

data = input("Digite uma data qualquer no formato dd/mm/AAAA: ")

# >> SLICING
dia = data[:2]
mes = data[3:5]
ano = data[6:]

print(f"A data escolhida foi o dia {dia} do mês {mes} do ano {ano}.")
# Escreva um programa que concatene duas strings fornecidas pelo usuário.

nome = input("Digite o seu nome: ")
sobrenome = input("Digite o seu sobrenome: ")

login = nome.lower() + "." + sobrenome.lower() + "@dom.com.br"

print(f"O seu login será: {login}.")