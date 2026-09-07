#Desafio - Refatorar o projeto da aula anterior evitando Bugs!
#Para resolver os bugs identificados — tratamento de entradas inválidas que não podem ser convertidas para um número de ponto flutuante
#e prevenção de valores negativos para salário e bônus, você pode modificar o código diretamente. 
#Isso envolve adicionar verificações adicionais após a tentativa de conversão para garantir que os valores sejam positivos.

try:
    Nome = input("Digite seu nome: ")

    if len(Nome) == 0:
        raise ValueError("O nome não pode estar vazio.")
    elif any(char.isdigit() for char in Nome):
        raise ValueError("O nome não deve conter números.")
    else:
        print("Nome válido:", Nome)
except ValueError as e:
    print(e)

try:
    Salario = float(input("Digite o valor do seu salário: "))
    if Salario < 0:
        print("Por favor, digite um valor positivo para o salário.")
except ValueError:
    print("Entrada inválida para o salário. Por favor, digite um número.")

try:
    Bonus = float(input("Digite o valor do bônus recebido: "))
    if Bonus < 0:
        print("Por favor, digite um valor positivo para o bônus.")
except ValueError:
    print("Entrada inválida para o bônus. Por favor, digite um número.")

Bonus_final = Bonus * 1.2  
Kpi = (Salario + Bonus_final) / 1000  

print(f"Seu KPI é: {Kpi:.2f}")
print(f"{Nome}, seu salário é R${Salario:.2f} e seu bônus final é R${Bonus_final:.2f}.")