# Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). 
# 
# Utilize try-except para garantir que a entrada seja uma string. 
# Dica: Utilize a função isinstance() para verificar o tipo da entrada.

palavra = input("Escreva uma palavra: ").strip()

try:
    if not isinstance(palavra, str):
        raise TypeError("A palavra difitada deve ser uma string")
    
    apenas_letras = "".join(l for l in palavra if l.isalpha)

    if len(apenas_letras) == 0:
        raise ValueError("Nenhuma letra foi digitada")
    
    elif len(apenas_letras) == 1:
        raise ValueError("Digite pelo menos 2 letras.")
    
    palavra_limpa = apenas_letras.lower()
    palavra_contrario = palavra_limpa[::-1]

    if palavra_limpa == palavra_contrario:
        print(f"{palavra} é um políndromo!")

    else:
        print(f"{palavra} não é um polídromo :(")
        
except TypeError as e:
    print(f"Erro de tipo: {e}")

except ValueError as e:
    print(f"Entrada inválida: {e}")