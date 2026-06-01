# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. 
# 
# Use try-except para lidar com divisões por zero e entradas não numéricas. 
# 
# Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. 
# 
# Imprima o resultado ou uma mensagem de erro apropriada.



try:

    num1 = float(input("Digite o número: "))

    num2 = float(input("Digite o número: "))

    operador = input("Qual operador deseja? ")
    
    if operador == "+":
        calculo = num1 + num2
    
    elif operador == "-":
        calculo = num1 - num2

    elif operador == "*":
        calculo = num1 * num2

    elif operador == "/":
        calculo = num1 / num2

    else:
        raise Exception(f"'{operador}' não é um operador válido.")

    print(calculo)

except ValueError as err:
    print("Atenção! Você não digitou um número.")

except ZeroDivisionError:
    print("Atenção! Não é possível realizar uma divisão por 0.")

except Exception as err:
    print(f"Atenção! {err}")