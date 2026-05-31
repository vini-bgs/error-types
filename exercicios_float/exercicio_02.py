# 1. Escreva um programa que receba dois números flutuantes e realize sua adição.

num1 = float(input("Digite um número decimal (use '.' como separador decimal): "))
num2 = float(input("Digite outro número decimal: "))

soma = num1 + num2

print(f"A soma de {num1} com {num2} é igual a {soma}.")
# 2. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

media = soma / 2

print(f"A média entre {num1} e {num2} é igual a {media}.")

# 3. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

potencia = num1 ** num2

print(f"O número {num1} elevado a {num2} é igual a {potencia}")

# 4. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

celcius = num1
fahrenheit = (celcius * 1.8) + 32

print(f"Convertendo {celcius}°C para °F temos a temperatura é igual a {fahrenheit}.")

# 5. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

raio = num2
pi = 3.14
area_circulo = pi * (raio ** 2)

print(f"Se {num2}cm é o raio de uma circunferência, então a área dela será {area_circulo}cm².")