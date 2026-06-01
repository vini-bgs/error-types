# Crie um script que solicite ao usuário uma lista de números separados por vírgula. 
# 
# O programa deve converter a string de entrada em uma lista de números inteiros. 
# 
# Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. 
# 
# Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. 
# 
# Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.

numeros = input("Digite uma lista de números separados por vírgula: ")

lista_numeros = numeros.split(",")

try:

    lista_numeros_inteiros = []

    for n in lista_numeros:
        valor_incorreto = n
        lista_numeros_inteiros.append(int(n))
        
    print(lista_numeros_inteiros)
    
except ValueError as err:
    print(f"Atenção! '{valor_incorreto}' não é um número.")