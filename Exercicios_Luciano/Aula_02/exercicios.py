#Exercícios

#Inteiros (int)
#1-Escreva um programa que soma dois números inteiros inseridos pelo usuário.

primeiro_numero = int(input("Usuário 1, insira o seu número:"))
segundo_numero = int(input("Usuário 2, insira o seu número:"))
resultado = primeiro_numero + segundo_numero
print("A soma é:", resultado)

#2-Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

numero_usuario = int(input("Insira o seu número:"))
resto_divisao = numero_usuario % 5
print("O resto da divisão por 5 é:", resto_divisao)

#3-Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

primeiro_numero = int(input("Usuário 1, insira o seu número:"))
segundo_numero = int(input("Usuário 2, insira o seu número:"))
resultado = primeiro_numero * segundo_numero
print("A multiplicação é:", resultado)

#4-Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

primeiro_numero = int(input("Usuário 1, insira o seu número:"))
segundo_numero = int(input("Usuário 2, insira o seu número:"))
resultado = primeiro_numero // segundo_numero
print("A divisão inteira é:", resultado)

#5-Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

numero_usuario = int(input("Insira o seu número:"))
quadrado = numero_usuario ** 2
print("O quadrado do número fornecido é:", quadrado)

#Números de Ponto Flutuante (float)
#6-Escreva um programa que receba dois números flutuantes e realize sua adição.

primeiro_numero = float(input("Usuário 1, insira o seu número:"))
segundo_numero = float(input("Usuário 2, insira o seu número:"))
resultado = primeiro_numero + segundo_numero
print("A soma é:", resultado)

#7-Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

primeiro_numero = float(input("Usuário 1, insira o seu número:"))
segundo_numero = float(input("Usuário 2, insira o seu número:"))
resultado =(primeiro_numero + segundo_numero) / 2
print("A média é:", resultado)

#8-Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

base = float(input("Insira o seu número:"))
expoente = float(input("Insira a potencia:"))
potencia = base ** expoente
print("A potencia é:", resultado)

#9-Faça um programa que converta a temperatura de Celsius para Fahrenheit.

celsius = float(input("Insira a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"A temperatura {celsius}°C é igual a {fahrenheit}°F")

#10-Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

raio = float(input("Digite o raio do círculo: "))
area = 3.14159 * raio ** 2
print("A área do círculo é:", area)

#Strings (str)
#11-Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

string_usuario = str(input("Insira uma palavra toda em letra minuscula:"))
string_usuario_maiuscula = string_usuario.upper()
print(string_usuario_maiuscula)

#12-Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

nome_completo = str(input("Insira seu nome completo:"))
nome_completo_minuscula = nome_completo.lower()
print(nome_completo_minuscula)

#13-Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

frase = str(input("Insira uma frase:"))
frase_sem_espacos = frase.strip()
print(frase_sem_espacos)

#14-Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

data = str(input("Insira uma data:"))
dia, mes, ano = data.split("/")
print("Dia:", dia)
print("Mês:", mes)
print("Ano:", ano)

#15-Escreva um programa que concatene duas strings fornecidas pelo usuário.

nome = str(input("Insira seu nome:"))
sobrenome = str(input("Insira seu sobrenome:"))
nome_sobrenome = nome +'_'+ sobrenome
print(nome_sobrenome)

#Booleanos (bool)
#16-Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

valor1 = bool(input("Insira o valor 'True' ou 'False':"))
valor2 = bool(input("Insira o valor 'True' ou 'False':"))
resultado_and = valor1 and valor2
print("Resultado do AND lógico:", resultado_and)

#17-Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

valor1 = bool(input("Insira o valor 'True' ou 'False':"))
valor2 = bool(input("Insira o valor 'True' ou 'False':"))
resultado_or = valor1 or valor2
print("Resultado do OR lógico:", resultado_or)

#18-Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

valor1 = bool(input("Insira o valor 'True' ou 'False':"))
resultado_not = not valor1
print("Resultado do NOT lógico:", resultado_not)

#19-Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

num1 = 5
num2 = 4
resultado_igualdade = (num1 == num2)
print("Resultado da igualdade:", resultado_igualdade)

#20-Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

num1 = 5
num2 = 4
resultado_igualdade = (num1 != num2)
print("Resultado da igualdade:", resultado_igualdade)


#Exercício 21: Conversor de Temperatura
#Escreva um programa que converta a temperatura de Celsius para Fahrenheit. 
#O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. 
#Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

try: 
   celsius = float(input("Insira a temperatura em Celsius: "))
   fahrenheit = (celsius * 9/5) + 32
   print(f"A temperatura {celsius}°C é igual a {fahrenheit}°F")
except ValueError:
   print("O valor inserido não está em Celsius, digite novamnete um valor válido, ex:2.0")

#Exercício 22: Verificador de Palíndromo
#Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). 
#Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.

entrada = input("Digite uma palavra ou frase: ")
if isinstance(entrada, str):
    formatado = entrada.replace(" ", "").lower()
    if formatado == formatado[::-1]:
      print("É um palíndromo.")
    else:
      print("Não é um palíndromo.")
else:
    print("Entrada inválida. Por favor, digite uma palavra ou frase.")

#Exercício 23: Calculadora Simples
#Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. 
#Use try-except para lidar com divisões por zero e entradas não numéricas. 
#Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.

try:
    numero1 = int(input("Insira o primeiro número:"))
    numero2 = int(input("Insira o segundo número:"))
    operador = input("Insira um dos operadores +, -, *, /:")

    if operador == "+":
         resultado_soma = numero1 + numero2
         print("O resultado da soma é:", resultado_soma)

    elif operador == "-":
         resultado_sub = numero1 - numero2
         print("O resultado da subtração é:", resultado_sub)

    elif operador == "*":
         resultado_mult = numero1 * numero2
         print("O resultado da multiplicação é:", resultado_mult)

    elif operador == "/" and numero2 != 0:
         resultado_div = numero1 / numero2
         print("O resultado da divisão é:", resultado_div)

    else:
         print("Operador inválido ou divisão por zero.")

except ValueError:
    print("Erro: Entrada inválida. Certifique-se de inserir números.")

#Exercício 24: Classificador de Números
#Escreva um programa que solicite ao usuário para digitar um número. 
#Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". 
#Adicionalmente, identifique se o número é "par" ou "ímpar".

try:
    numero = int(input("Insira um número inteiro:"))

    if numero > 0:
        print("O número é positivo")
    elif numero < 0:
        print("O número é negativo")
    else:
        print("O número é zero")
    
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")

except ValueError:
    print("Entrada inválida, digite um número inteiro")

#Exercício 25: Conversão de Tipo com Validação
#Crie um script que solicite ao usuário uma lista de números separados por vírgula. 
#O programa deve converter a string de entrada em uma lista de números inteiros. 
#Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. 
#Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. 
#Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.

entrada_lista = input("Digite uma lista de números separados por vírgula: ")
numeros_str = entrada_lista.split(",")
numeros_int = []
try:
    for num in numeros_str:
        numeros_int.append(int(num.strip()))
    print("Lista de inteiros:", numeros_int)
except ValueError:
    print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")