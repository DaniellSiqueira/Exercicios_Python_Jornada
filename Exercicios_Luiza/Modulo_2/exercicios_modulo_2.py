# Exercício 1 – Descobrindo os tipos

# Observe os valores abaixo:

# nome = "Brasil"
# gols = 3
# posse_bola = 58.7
# classificado = True

# Crie um programa que mostre o tipo de cada uma dessas variáveis utilizando type().
# Ao executar, o programa deve permitir identificar quais valores são str, int, float e bool.

nome = "Brasil"
gols = 3
posse_bola = 58.7
classificado = True

print(type(nome))
print(type(gols))
print(type(posse_bola))
print(type(classificado))

# Exercício 2 – Verificando os tipos

# Considere as variáveis:

# numero_camisa = 10
# jogador = "Raphinha"

# Utilize isinstance() para verificar:

# se numero_camisa é um int;
# se numero_camisa é uma str;
# se jogador é uma str.

# Mostre o resultado de cada verificação na tela.

numero_camisa = 10
jogador = "Raphinha"

print(isinstance(numero_camisa, int))
print(isinstance(numero_camisa, str))
print(isinstance(jogador, str))

# Exercício 3 – Encontre o Erro e Corrija

# O código abaixo apresenta um erro:

# gols = "2"
# novo_gol = gols + 1

# print(novo_gol)

# Execute o código, observe a mensagem apresentada pelo Python e responda:
# Qual erro ocorreu?
# TypeError: can only concatenate str (not "int") to str
# Quais são os tipos dos valores envolvidos?
# Na variável gols o valor é uma string e na novo_gol um inteiro 
# Por que esses valores não podem ser utilizados dessa forma?
# Porque operações matemáticas só podem ser feitas onde as variveis sejam int ou float.
# Corrija o programa para que o resultado exibido seja 3.

gols = 2
novo_gol = gols + 1

print(novo_gol)

# Exercício 4 – Trabalhando com input()

# Crie um programa que pergunte ao usuário quantos gols uma seleção marcou em uma partida.

# Depois:

# descubra o tipo do valor recebido diretamente pelo input();
# converta esse valor para int;
# mostre novamente o tipo depois da conversão;
# calcule quantos gols a seleção teria caso marcasse mais um.

# Exemplo de entrada:

# Quantos gols a seleção marcou? 2
# Resultado esperado ao final:
# Com mais um gol, a seleção teria 3 gols.

gols = input("Quantos gols a seleção marcou?")

print(type(gols))

qtd_gols = int(gols)

print(type(qtd_gols))

gols_total = qtd_gols + 1

print(f"Com mais um gol, a seleção teria {gols_total} gols")

# Exercício 5 – Convertendo valores decimais

# Crie um programa que peça ao usuário:

# o nome de um jogador;
# sua nota na partida.

# A nota pode possuir casas decimais, como 8.5.

# Converta a nota para o tipo adequado e exiba uma mensagem semelhante a:

# Vinicius recebeu a nota 8.5.

# Antes de finalizar, utilize type() para verificar se a nota foi realmente convertida para o tipo esperado.

nome_jogador = input("Insira o nome do jogador:")
nota = input("Insira a nota do jogador")

nota_c = float(nota)

print(f"{nome_jogador} recebeu a nota {nota_c}")

print(type(nota_c))

# Exercício 6 – Quando precisamos de str

# Considere:

# numero = 10
# jogador = "Rodrygo"

# Crie uma mensagem que resulte em:

# O jogador Rodrygo veste a camisa 1.

# Para este exercício, faça a construção da mensagem utilizando +.

# Observe o erro que acontece ao tentar concatenar diretamente numero com os textos e depois utilize str() para corrigir o problema.

# Explique por que a conversão foi necessária.

numero = 10
jogador = "Rodrygo"

camisa = str(numero)

print("O jogador " + jogador + " veste a camisa " + camisa)

# A conversão foi necessaria porque só é possivel concatenar duas variáveis utilizando o "+" se forem do tipo string.

# Exercício 7 – Deixando os valores explícitos

# Crie as seguintes variáveis utilizando Type Hint:

# nome da seleção → texto;
# quantidade de vitórias → número inteiro;
# aproveitamento → número decimal;
# seleção classificada → valor booleano.

# Atribua um valor para cada variável.

# Depois, altere propositalmente uma delas para um valor de outro tipo e observe o comportamento do Python.

# Com base no que aconteceu, responda:

# O Type Hint impede que uma variável receba outro tipo de valor durante a execução?

nome_seleção: str = "Brasil"
quantidade_vitorias: int = 5
aproveitamento: float = 8.0
seleção_classificada: bool = True

qtd_vitorias = str(quantidade_vitorias)

print(type(qtd_vitorias))

# O Type Hint não impede a variável de receber outro valor, ele é somente para indicar o tipo de valor esperado na variável.

# Exercício 8 – Impedindo o programa de quebrar

# Crie um programa que pergunte a idade do usuário:

# Converta a resposta para int.

# Use try/except para impedir que o programa seja encerrado caso alguém digite algo como: vinte

# Se a conversão funcionar, mostre:
# Idade registrada com sucesso.
# Se ocorrer um ValueError, mostre:
# Digite a idade utilizando apenas números.

idade = input("Insira sua idade:")

try:
    idade_correta = int(idade)
    print("Idade registrada com sucesso")

except ValueError:
    print("Digite a idade utilizando apenas números")

# Exercício 9 – Tratando entrada e validando o valor

# Uma avaliação de jogador deve receber uma nota entre 0 e 10.

# Crie um programa que peça essa nota ao usuário.

# O programa deve:

# tentar converter a entrada para float;
# tratar um possível ValueError;
# verificar se a nota está entre 0 e 10;
# informar quando a nota estiver fora desse intervalo.

# Exemplos:

# Digite a nota: oito
# Valor inválido. Digite um número.

# Digite a nota: 15
# A nota deve estar entre 0 e 10.

# Digite a nota: 8.5
# Nota registrada: 8.5

nota = input("Insira a nota do jogador:")

try:
    nota_jogador = float(nota)

    if nota_jogador >= 0 and nota_jogador <= 10:
        print(f"Nota registrada:{nota_jogador}")

    else:
        print("A nota deve estar entre 0 e 10.")

except ValueError:
    print("Valor inválido. Digite um número.")

# Exercício 10 – Continue perguntando até receber um valor válido

# Crie um programa para registrar a quantidade de gols de uma seleção.

# O programa deve continuar perguntando:

# Quantos gols a seleção marcou?

# até que o usuário forneça um número inteiro válido e maior ou igual a zero.

# Considere situações como:

# Quantos gols a seleção marcou? três
# Entrada inválida.

# Quantos gols a seleção marcou? -2
# A quantidade de gols não pode ser negativa.

# Quantos gols a seleção marcou? 4
# Quantidade de gols registrada: 4

# Para resolver o exercício, utilize os conteúdos estudados até aqui, incluindo:

# input();
# conversão com int();
# try/except;
# ValueError;
# condição;
# while.

# O programa só deve parar de solicitar a informação quando receber um valor válido.

numero_valido: bool = False

while numero_valido == False:
    try:
        gols = int(input("Quantos gols a seleção marcou?"))

        if gols >= 0:
            numero_valido = True
            print(f"Quantidade de gols registrada: {gols}")
        else:
            print("A quantidade de gols não pode ser negativa.")
 
    except ValueError:
        print("Entrada inválida")