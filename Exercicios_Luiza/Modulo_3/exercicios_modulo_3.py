# Exercício 1 – Cadastro de Figurinhas

# Você foi contratado para desenvolver um sistema simples para controlar um álbum de figurinhas da Copa do Mundo.

# O programa deve permitir que o usuário cadastre figurinhas até que ele digite a palavra "fim".

# Ao final, exiba:

# Todas as figurinhas cadastradas.
# A quantidade total de figurinhas.
# A primeira figurinha cadastrada.
# A última figurinha cadastrada.

# Desafio: não permita que o usuário cadastre uma figurinha vazia.

figurinhas = []

while True:

    figurinha = input("Digite o número da figurinha, ou 'fim' para encerrar:")

    if figurinha.lower() == "fim":
        break

    elif figurinha != "":
        figurinhas.append(figurinha)
        print("Figurinha adicionada")

    else:
        print("O campo figurinha são pode ser vazio")

try:
    print(figurinhas)
    print(len(figurinhas))
    print(figurinhas[0])
    print(figurinhas[-1])

except IndexError:
    print("Nenhuma figurinha foi adicionada")

# Exercício 2 – Estatísticas da Partida

# Crie um programa que solicite ao usuário as seguintes informações de uma partida:

# Seleção mandante
# Seleção visitante
# Gols da seleção mandante
# Gols da seleção visitante

# Armazene essas informações em um dicionário.

# Depois:

# Exiba todas as informações utilizando um for com .items().
# Informe qual seleção venceu a partida.
# Caso os gols sejam iguais, informe que a partida terminou empatada.

# Desafio: utilize try/except para garantir que a quantidade de gols seja um número inteiro válido.

validacao_mandante = False
validacao_visitante = False
mandante = input("Digite o nome da seleção mandante:")
visitante = input("Digite o nome da seleção visitante:")

while validacao_mandante == False:

    try:
        gols_mandante = int(input("Insira os gols da seleção mandante:"))
        if gols_mandante >= 0:
            validacao_mandante = True

    except ValueError:
        print("Digite um valor válido, é preciso ser um número")

while validacao_visitante == False:

    try:
        gols_visitante = int(input("Insira os gols da seleção visitante:"))
        if gols_visitante >= 0:
            validacao_visitante = True

    except ValueError:
        print("Digite um valor válido, é preciso ser um número")

partida = {
    "Seleção Mandante": mandante,
    "Seleção Visitante": visitante,
    "Gols Mandante": gols_mandante,
    "Gols Visitante": gols_visitante
}

print("Informações da Partida:")

for descricao, resultado in partida.items():
    print(f"{descricao}: {resultado}")

print("Resultado da Partida:")

if partida["Gols Mandante"] > partida["Gols Visitante"]:
    print(f"A seleção {partida['Seleção Mandante']} venceu!")

elif partida["Gols Visitante"] > partida["Gols Mandante"]:
    print(f"A seleção {partida['Seleção Visitante']} venceu!")

else:
    print("A partida empatou")


# Exercício 3 – Seleções Classificadas

# Durante a fase de grupos, várias seleções foram sendo classificadas.

# Peça ao usuário para informar o nome de 8 seleções.

# Armazene essas seleções em um set.

# Ao final:

# Exiba todas as seleções classificadas.
# Informe quantas seleções diferentes foram cadastradas.

# Depois pergunte ao usuário o nome de uma seleção e informe se ela está classificada utilizando o operador in.

# Desafio: explique por que, mesmo digitando uma seleção repetida, ela aparece apenas uma vez no conjunto.
# Resposta: Aparece apenas uma vez porque o set trabalha com valores unicos então elel armazena o registro de 
# um valor somente uma vez, mesmo que ele tenha sido adicionado mais vezes.

selecoes = set()

for adicao in range(1,9):
    selecao = input("Insira o nome da seleção:")
    print(f"Seleção {adicao} adicionada")
    selecoes.add(selecao)

print(f"Seleções classificadas: {selecoes}")
print(f"Quantidade de seleções: {len(selecoes)}")

selecao_classificada = input("Insira o nome da seleção:")

if selecao_classificada in selecoes:
    print("Seleção classificada")

else: 
    print("Seleção não classificada")


# Exercício 4 – Menu do Álbum

# Desenvolva um programa que simule um álbum de figurinhas.

# Utilize uma lista para armazenar as figurinhas e exiba o seguinte menu:

# 1 - Adicionar figurinha
# 2 - Remover figurinha
# 3 - Buscar figurinha
# 4 - Mostrar álbum
# 5 - Encerrar

# O menu deve permanecer sendo exibido até que o usuário escolha a opção 5.

# Regras:

# Ao adicionar, a figurinha deve ser inserida no final da lista.
# Ao remover, informe caso a figurinha não exista.
# Na busca, informe se a figurinha está ou não no álbum.
# Ao mostrar o álbum, exiba todas as figurinhas utilizando um for.

# Desafio: utilize if, elif, else e while.

figurinhas = []

while True:

    print("Menu de Opções:")
    print("1 - Adicionar figurinha")
    print("2 - Remover figurinha")
    print("3 - Buscar figurinha")
    print("4 - Mostrar álbum")
    print("5 - Encerrar")

    while True:
        try:
            opcao = int(input("Selecione um número das opções acima:"))
            break
        except ValueError:
            print("Digite um número para selecionar a opção")

    if opcao == 1:
        adiciona_figurinha = input("Digite a figurinha que deseja adicionar:")

        if adiciona_figurinha != "":
            figurinhas.append(adiciona_figurinha)
            print("Figurinha adicionada")

        else:
            print("O campo não pode estar vazio")

    elif opcao == 2:
        remove_figurinha = input("Digite a figurinha que deseja remover:")

        if remove_figurinha in figurinhas:
             figurinhas.remove(remove_figurinha)
             print("Figurinha removida")

        else:
            print("Figurinha não existe")

    elif opcao == 3:
        buscar_figurinha = input("Digite a figurinha que deseja buscar:")

        if buscar_figurinha in figurinhas:
            print(f"Figurinha {buscar_figurinha} encontrada")

        else:
            print("Figurinha não encontrada")

    elif opcao == 4:
        for figura_cadastrada in figurinhas:
            print(f"Figurinha cadastrada: {figura_cadastrada}")

    elif opcao == 5:
        print("Seção encerrada")
        break

    else:
        print("Digite uma opção valida")

# Exercício 5 – Ranking de Artilheiros

# Crie uma lista de dicionários para armazenar informações de jogadores.

# O programa deverá perguntar quantos jogadores o usuário deseja cadastrar.

# Para cada jogador, solicite:

# Nome
# Seleção
# Quantidade de gols

# Cada jogador deverá ser armazenado como um dicionário dentro da lista.

# Ao final:

# Exiba todos os jogadores cadastrados.
# Informe qual jogador marcou mais gols.
# Informe a média de gols dos jogadores cadastrados.

# Desafio: utilize try/except para validar a quantidade de gols informada pelo usuário.

jogadores = []
qtd_jogadores = int(input("Insira a quantidade de jogadores que serão cadastrados:"))

for jogador in range(qtd_jogadores):
    nome = input("Insira o nome do jogador:")
    selecao = input("Insira o nome da seleção do jogador:")

    while True:
        try:
            quantidade_gols = int(input("Insira a quantidade de gols:"))
            break

        except ValueError:
            print("Valor inválido, digite um número")

    cadastro_jogador = {
        "Nome": nome,
        "Seleção": selecao,
        "Quantidade_Gols": quantidade_gols
    }

    jogadores.append(cadastro_jogador)

    print("Informações cadastradas")

print("Jogadores cadastrados:")
for cadastro_jogador in jogadores:
    print(cadastro_jogador["Nome"])

top_gols = 0
top_jogador = ""

for jogador in jogadores:
    if jogador["Quantidade_Gols"] > top_gols:
        top_gols = jogador["Quantidade_Gols"]
        top_jogador = jogador["Nome"]

print(f"O jogador com mais gols foi {top_jogador}, com {top_gols} gols.")

total_gols = 0

for jogador in jogadores:
    total_gols += jogador["Quantidade_Gols"]

media_gols = total_gols / len(jogadores)

print(f"A média de gols foi {media_gols}.")

# Exercício 6 – Desafio Final: Sistema da Copa do Mundo

# Desenvolva um programa para cadastrar partidas da Copa do Mundo.

# O programa deverá permanecer em execução até que o usuário decida encerrá-lo.

# Para cada partida, solicite:

# Seleção mandante
# Seleção visitante
# Gols da seleção mandante
# Gols da seleção visitante

# Cada partida deverá ser armazenada em um dicionário, e todos os dicionários deverão ser armazenados em uma lista.

# Ao finalizar o cadastro, exiba:

# A quantidade de partidas cadastradas.
# Todas as partidas registradas.
# Quantas partidas terminaram empatadas.
# A partida com o maior número total de gols.
# A média de gols por partida.

# Requisitos:

# Utilize listas e dicionários.
# Utilize while para controlar o cadastro.
# Utilize for para percorrer as partidas.
# Utilize if, elif e else para identificar o resultado de cada jogo.
# Utilize try/except para validar os gols informados.
# Utilize len() para calcular a quantidade de partidas cadastradas.

partidas = []

while True:
    mandante = input("Digite o nome da seleção mandante:")
    visitante = input("Digite o nome da seleção visitante:")    
    validacao_mandante = False
    validacao_visitante = False

    while validacao_mandante == False:

        try:
            gols_mandante = int(input("Insira os gols da seleção mandante:"))
            if gols_mandante >= 0:
                validacao_mandante = True

            else:
                print("Digite um numero maior ou igual a 0")

        except ValueError:
            print("Digite um valor válido, é preciso ser um número")

    while validacao_visitante == False:

        try:
            gols_visitante = int(input("Insira os gols da seleção visitante:"))
            if gols_visitante >= 0:
                validacao_visitante = True
            
            else:
                print("Digite um numero maior ou igual a 0")

        except ValueError:
            print("Digite um valor válido, é preciso ser um número")

    cadastro_partida = {
        "Seleção Mandante": mandante,
        "Seleção Visitante": visitante,
        "Gols Mandante": gols_mandante,
        "Gols Visitante": gols_visitante
    }

    partidas.append(cadastro_partida)
    print("Informações cadastradas")

    controle = input("Deseja inserir outra partida? Digite 'Sim' ou 'Nao':")

    if controle.lower() == "nao":
        break

print("Quantidade de partidas:")

print(len(partidas))

print("Partidas registradas:")

for numero, partida in enumerate(partidas, start=1):
    print(f"Partida: {numero}")
    print(f"Seleção Mandante: {partida['Seleção Mandante']}")
    print(f"Seleção Visitante: {partida['Seleção Visitante']}")
    print(f"Gols Mandante: {partida['Gols Mandante']}")
    print(f"Gols Visitante: {partida['Gols Visitante']}")

print("Partidas empatadas:")

empates = 0

for partida in partidas:
    if partida["Gols Mandante"] == partida["Gols Visitante"]:
       empates += 1
print(empates)

print("Partida que teve maior numero de gols:")

maior_numero_gols = 0
partida_maior_numero_gols = ""

for partida in partidas:
    total_gols = partida["Gols Mandante"] + partida["Gols Visitante"]

    if total_gols > maior_numero_gols:
        maior_numero_gols = total_gols
        partida_maior_numero_gols = partida

print(f"Maior número de gols: {maior_numero_gols}")
print(f"Partida: {partida_maior_numero_gols['Seleção Mandante']} x {partida_maior_numero_gols['Seleção Visitante']}")

print("Média de gols por partida:")

total_gols = 0

for partida in partidas:
    total_gols += partida["Gols Mandante"]
    total_gols += partida["Gols Visitante"]

media_gols = total_gols / len(partidas)

print(f"Média de gols por partida: {media_gols:.2f}")
