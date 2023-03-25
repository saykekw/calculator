def CalculatorUS():
    line = 10 * "-"
    print("----- CALCULATOR V1 -----")
    print("Created by Say") # Credits :D
    print(line)

    while True:
        num1 = input("Type a number: ")
        num2 = input("Type another one: ")
        operator = input("Type an operator: \r\n- Sum(+)\r\n- Subtraction(-)\r\n- Multiplication(*)\r\n- Divide(/): ")

        valid_numbers = None

        print(line)

        try:
            num1_float = float(num1)
            num2_float = float(num2)
            valid_numbers = True
        except:
            valid_numbers = None
        
        if valid_numbers is None:
            print("One of both numbers are invalid.")
            print(line)
            continue

        allowed_operators = "+ - / *"

        if operator not in allowed_operators:
            print("Operator is invalid.")
            print(line)
            continue
        
        if len(operator) > 1:
            print("Type only one operator.")
            print(line)
            continue
        
        sum_result = num1_float + num2_float
        subtraction_result = num1_float - num2_float
        multiplication_result = num1_float * num2_float
        divide_result = num1_float / num2_float

        if operator == "+": 
            print(f"Result of {num1_float} {operator} {num2_float} is {sum_result}")
        elif operator == "-":
            print(f"Result of {num1_float} {operator} {num2_float} is {subtraction_result}")
        elif operator == "*":
            print(f"Result of {num1_float} {operator} {num2_float} is {multiplication_result}")
        elif operator == "/":
            print(f"Result of {num1_float} {operator} {num2_float} is {divide_result}")
        else:
            print("Not supposed to arrive here")
        
        print(line)
        another_sum = input("Want to use the calculator again? s/n ").lower().startswith("s")

        if another_sum:
            print(line)
            continue
        else:
            print(line)
            print("Thank you for using the CALCULATOR V1")
            break

def CalculadoraBR():
    linha = 10 * "-"
    print("----- CALCULADORA V1 -----")
    print("Criada por Say") # Créditos :D
    print(linha)

    while True:
        num1 = input("Digite um número: ")
        num2 = input("Digite outro número: ")
        operador = input("Digite um operador: \r\n- Adição(+)\r\n- Subtração(-)\r\n- Multiplicação(*)\r\n- Divisão(/): ")

        numeros_validos = None

        print(linha)

        try:
            num1_float = float(num1)
            num2_float = float(num2)
            numeros_validos = True
        except:
            numeros_validos = None
        
        if numeros_validos is None:
            print("Um ou ambos os números digitados são inválidos.")
            print(linha)
            continue

        operadores_permitidos = "+ - / *"

        if operador not in operadores_permitidos:
            print("Operador não é válido.")
            print(linha)
            continue
        
        if len(operador) > 1:
            print("Digite apenas um operador.")
            print(linha)
            continue
        
        resultado_adicao = num1_float + num2_float
        resultado_subtracao = num1_float - num2_float
        resultado_multiplicacao = num1_float * num2_float
        resultado_divisao = num1_float / num2_float

        if operador == "+": 
            print(f"O resultado de {num1_float} {operador} {num2_float} é {resultado_adicao}")
        elif operador == "-":
            print(f"O resultado de {num1_float} {operador} {num2_float} é {resultado_subtracao}")
        elif operador == "*":
            print(f"O resultado de {num1_float} {operador} {num2_float} é {resultado_multiplicacao}")
        elif operador == "/":
            print(f"O resultado de {num1_float} {operador} {num2_float} é {resultado_divisao}")
        else:
            print("Não deveria chegar aqui.")
        
        print(linha)
        outra_conta = input("Deseja fazer outra conta? s/n: ").lower().startswith("s")

        if outra_conta:
            print(linha)
            continue
        else:
            print(linha)
            print("Obrigado por usar a CALCULADORA V1")
            break

w = input("Bem-vindo à CALCULADORA V1, escolha seu idioma:"
"\nWelcome to the CALCULATOR V1, choose your language:"
"\r\n[1]EN-US \r\n[2]PT-BR: ")

if w == "1":
    CalculatorUS()
elif w == "2":
    CalculadoraBR()

