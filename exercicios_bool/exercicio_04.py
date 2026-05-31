# Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

valor1 = input("Digite uma expressão booleana: ") == "True"
valor2 = input("Digite outra expressão booleana: ") == "True"

verifica_and = valor1 and valor2

print(verifica_and)
# Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

verifica_or = valor1 or valor2

print(verifica_or)
# Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

invert = not (valor1)
print(invert)
# Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

verifica_igual = num1 == num2

print(f"{verifica_igual}!")
# Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

verifica_igual = num1 != num2

print(f"{verifica_igual}!")