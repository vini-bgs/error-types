#Escreva um programa que solicite ao usuário para digitar um número. 
# 
# Utilize try-except para assegurar que a entrada seja numérica 
# 
# e utilize if-elif-else para classificar o número como positivo, negativo ou zero. 
# 
# Adicionalmente, identifique se o número é par ou ímpar.

try:

    valor = input("Digite um número: ")

    if "," in valor:
        raise Exception("Utilize '.' como separador decimanal ao invés de ','.")
    
    valor = float(valor)

    if valor < 0:
        classificacao = "negativo"

    elif valor > 0:
        classificacao = "positivo"

    else:
        classificacao = "zero"

    if classificacao == "zero" or valor != int(valor):
        paridade = "nem par nem impar"

    elif valor % 2 == 0:
        paridade = "par"

    else:
        paridade = "impar"

    print(f"O número {valor} é {classificacao} e {paridade}.")

except ValueError as err:
    print(f"Atenção: {err}")

except Exception as err:
    print(f"Atenção! {err}")