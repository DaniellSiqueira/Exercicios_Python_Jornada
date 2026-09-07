# Questão: Cálculo de Bônus com Entrada do Usuário
# Escreva um programa em Python que solicita ao usuário para digitar seu nome, 
# o valor do seu salário mensal e o valor do bônus que recebeu. 
# O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e 
# informando o valor do salário em comparação com o bônus recebido.

Nome = input("Por favor, digite o seu nome: ")
Salario = float(input("Agora digite o seu salário: "))
Bonus = float(input("Digite o valor do seu bonus: "))
Valor_bonus = 1000 + Salario * Bonus

print(f"Olá {Nome}, o seu bônus foi de {Valor_bonus}")
