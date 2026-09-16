# Exercício 1 – Argumentos posicionais

# Crie uma função chamada apresentar_jogador que receba:

# - nome
# - posicao
# A função deve exibir uma mensagem semelhante a:

# Jogador: Marta | Posição: Atacante
# Faça a chamada da função passando os dois argumentos por posição.

# Exemplo:

# apresentar_jogador("Marta", "Atacante")

def apresentar_jogador (
        nome: str,
        posicao :str
) -> None:
    print(f"Jogador: {nome} | Posição: {posicao}")

apresentar_jogador("Marta", "Atacante")

# Exercício 2 – A ordem dos argumentos

# Crie uma função chamada mostrar_partida que receba:

# - mandante
# - visitante
# A função deve exibir os dois times no formato:

# Brasil x Argentina

# Faça as seguintes chamadas:

# mostrar_partida("Brasil", "Argentina")mostrar_partida("Argentina", "Brasil")

# Observe como a ordem dos argumentos posicionais altera o resultado.

def mostrar_partida(
        mandante: str,
        visitante: str
) -> None:
    print(f"{mandante} x {visitante}")

mostrar_partida("Brasil", "Argentina")
mostrar_partida("Argentina", "Brasil")

# Exercício 3 – Argumentos nomeados

# Crie uma função chamada cadastrar_jogador que receba:

# - nome
# - idade
# - posicao

# Faça a chamada utilizando argumentos nomeados e passe os valores em uma ordem diferente da definida na função.

# Exemplo:

# cadastrar_jogador(posicao="Goleiro", nome="Alisson", idade=33)

def cadastrar_jogador(
        nome: str,
        idade: int,
        posicao: str
) -> None:
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Posição: {posicao}")

cadastrar_jogador(
    posicao="Goleiro",
    nome="Alisson",
    idade=33
)

# Exercício 4 – Posicionais e nomeados juntos

# Crie uma função chamada registrar_gol que receba:

# - jogador
# - time
# - minuto

# Na chamada da função:

# - Passe jogador por posição.
# - Passe time por posição.
# - Passe minuto pelo nome.

# A função deve exibir uma mensagem semelhante a:

# Vini Jr marcou para o Brasil aos 34 minutos.

def registrar_gol(
        jogador: str,
        time: str,
        minuto: int
) -> None:
    print(f"{jogador} marcou para o {time} aos {minuto} minutos")

registrar_gol(
    "Vini Jr",
    "Brasil",
    minuto=34
)

# Exercício 5 – Parâmetro com valor padrão

# Crie uma função chamada criar_partida que receba:

# - time_a
# - time_b
# - estadio

# O parâmetro estadio deve possuir o seguinte valor padrão:

# "Estádio Nacional"

# Depois, faça duas chamadas:

# 1- Uma sem informar o estádio.
# 2- Outra informando um estádio diferente.

def criar_partida(
        time_a: str,
        time_b: str,
        estadio: str = "Estádio Nacional"
) -> None:
    print(f"Time A: {time_a}")
    print(f"Time B: {time_b}")
    print(f"Estádio: {estadio}")

criar_partida(
    "Brasil",
    "Argentina"
)

criar_partida(
    "Brasil",
    "Argentina",
    "Mané Garrincha"
)

# Exercício 6 – Mais de um valor padrão

# Crie uma função chamada registrar_jogador com os seguintes parâmetros:

# nome
# posicao="Não informada"
# titular=False

# A função deve mostrar os dados do jogador.

# Teste as seguintes chamadas:

# registrar_jogador("Marta")
# registrar_jogador("Marta", "Atacante")
# registrar_jogador("Marta", "Atacante", True)

# Depois, faça mais uma chamada alterando apenas o valor de titular, utilizando um argumento nomeado.

def registrar_jogador(
        nome: str,
        posicao: str = "Não informada",
        titular: bool = False
) -> None:
    print(f"Nome: {nome}")
    print(f"Posição: {posicao}")
    print(f"Titular?: {titular}")

registrar_jogador("Marta")
registrar_jogador("Marta", "Atacante")
registrar_jogador("Marta", "Atacante", True)

registrar_jogador("Marta", "Atacante", titular=True)

# Exercício 7 – Alterando apenas um valor padrão

# Crie uma função chamada configurar_camisa que receba:

# nome
# numero
# tamanho="M"
# cor="amarela"

# Faça uma chamada informando uma cor diferente, mas mantendo o tamanho padrão

# Exemplo:

# configurar_camisa("Marta", 10, cor="azul")

# Observe como o argumento nomeado permite alterar cor sem precisar passar um novo valor para tamanho.

def configurar_camisa(
        nome: str,
        numero: int,
        tamanho: str = "M",
        cor: str = "amarela"
) -> None:
    print(f"Nome: {nome}")
    print(f"Número: {numero}")
    print(f"Tamanho: {tamanho}")
    print(f"Cor: {cor}")

configurar_camisa("Marta", 10, cor="azul")

# Exercício 8 – Recebendo vários argumentos com *args

# Crie uma função chamada listar_jogadores que receba uma quantidade variável de nomes utilizando *args.

# def listar_jogadores(*jogadores):

# A função deve percorrer os jogadores recebidos e exibir cada nome.

# Teste a função com diferentes quantidades de argumentos:

# listar_jogadores("Marta")listar_jogadores("Marta","Vini Jr","Alisson")

def listar_jogadores(*jogadores: str) -> None:
    for jogador in jogadores:
        print(jogador)

listar_jogadores("Marta")
listar_jogadores("Marta","Vini Jr","Alisson")

# Exercício 9 – Trabalhando com os valores de *args

# Crie uma função chamada somar_gols que receba uma quantidade indefinida de números utilizando *args.

# A função deve retornar a soma de todos os valores recebidos.

# Exemplo:

# total = somar_gols(2, 1, 3, 2)
# print(total)

# Resultado esperado:

# 8

def somar_gols(*gols: int) -> int:
    return sum(gols)

total_gols = somar_gols(2, 1, 3, 2)
print(total_gols)

# Exercício 10 – Parâmetro normal e *args

# Crie uma função chamada:

# convocar_selecao(pais, *jogadores)

# O primeiro argumento deve representar o país da seleção.

# Todos os argumentos posicionais seguintes devem representar os jogadores convocados.

# Exemplo de chamada:

# convocar_selecao("Brasil","Alisson","Marquinhos","Bruno Guimarães","Vini Jr")

# A função deve mostrar primeiro o país e depois cada jogador convocado.

def convocar_selecao(
        pais: str, 
        *jogadores: str
) -> None:
    print(f"País: {pais} | Jogadores Selecionados: {jogadores}")

convocar_selecao("Brasil","Alisson","Marquinhos","Bruno Guimarães","Vini Jr")


# Exercício 11 – Recebendo argumentos nomeados com **kwargs

# Crie uma função chamada mostrar_jogador que receba uma quantidade variável de argumentos nomeados utilizando **kwargs.

# def mostrar_jogador(**dados):

# Faça uma chamada semelhante a:

# mostrar_jogador(nome="Marta", idade=40, posicao="Atacante")

# # Dentro da função, percorra os dados recebidos e mostre cada chave junto com seu respectivo valor.

def mostrar_jogador(**dados):
    for chave, valor in dados.items():
     print(f"{chave}: {valor}")

mostrar_jogador(nome="Marta", idade=40, posicao="Atacante")

# Exercício 12 – Parâmetro normal e **kwargs

# Crie uma função chamada:

# cadastrar_time(nome, **informacoes)
# O nome do time deve ser obrigatório.

# As demais informações podem variar de uma chamada para outra.

# Exemplo:

# cadastrar_time("Brasil", tecnico="Carlo Ancelotti", continente="América do Sul" ,titulos=5)

# A função deve mostrar o nome do time e depois todas as informações adicionais recebidas.

def cadastrar_time(nome, **informacoes) -> None:
    print(f"Nome do time: {nome}")
    for chave, valor in informacoes.items():
        print(f"{chave}: {valor}")

cadastrar_time("Brasil", tecnico="Carlo Ancelotti", continente="América do Sul" ,titulos=5)

# Exercício 13 – *args e **kwargs juntos

# Crie uma função chamada:

# registrar_partida(time_a, time_b, *eventos, **informacoes):
# Os dois primeiros argumentos devem representar os times da partida.

# Os argumentos posicionais extras devem representar eventos ocorridos durante o jogo.

# Os argumentos nomeados extras devem representar outras informações sobre a partida.

# Exemplo:

# registrar_partida(
# "Brasil",
# "Argentina",
# "Gol do Brasil",
# "Cartão amarelo",
# "Gol da Argentina",
# estadio="Maracanã",
# publico=70000
# ):

# A função deve mostrar:

# - Os dois times.
# - Todos os eventos recebidos.
# - Todas as informações adicionais.

def registrar_partida(
        time_a: str,
        time_b: str,
        *eventos: str,
        **informacoes
)-> None:
    print("\nTimes da partida")
    print(f"Time A: {time_a}")
    print(f"Time B: {time_b}")

    print("\nEventos ocorridos no jogo")
    for evento in eventos:
        print(f"-{evento}")

    print("\nInformações da partida")
    for k, v in informacoes.items():
        print(f"{k}: {v}")

registrar_partida(
"Brasil",
"Argentina",
"Gol do Brasil",
"Cartão amarelo",
"Gol da Argentina",
estadio="Maracanã",
publico=70000
)

# Exercício 14 – Unpacking com * e retorno

# Considere a seguinte lista:

# times = ["Brasil", "Argentina"]
# Crie uma função chamada montar_confronto que receba dois parâmetros:

# - time_a
# - time_b

# A função deve:

# - Utilizar type hints nos parâmetros e no retorno.
# - Possuir uma docstring explicando o que ela faz.
# - Retornar uma string no formato Brasil x Argentina.
# Depois, chame a função desempacotando a lista com *.

# Você não deve acessar os valores manualmente com:

# times[0]
# times[1]

# Exemplo esperado de uso:

# confronto = montar_confronto(*times)
# print(confronto)

times = ["Brasil", "Argentina"]

def montar_confronto(
        time_a: str, 
        time_b: str
) -> str:
    
    """
    Monta uma string representando o confronto entre dois times.
    """
    return f"{time_a} x {time_b}"

confronto = montar_confronto(*times)
print(confronto)

# Exercício 15 – Unpacking com * e valores padrão

# Crie uma função chamada calcular_media com os seguintes parâmetros:

# nota1
# nota2
# nota3
# bonus=0

# A função deve:

# - Utilizar type hints em todos os parâmetros e no retorno.
# - Possuir uma docstring.
# - Calcular a média das três notas.
# - Somar o valor de bonus ao resultado final.
# - Retornar a média calculada.

# Considere:

# notas = [8.5, 7.0, 9.5]

# Chame a função utilizando * para desempacotar as notas:

# resultado = calcular_media(*notas)
# print(resultado)

# Depois, faça uma segunda chamada utilizando a mesma lista, mas informe bonus como argumento nomeado.

# Por fim, altere a lista para possuir quatro notas:

# notas = [8.5, 7.0, 9.5, 10.0]

# Tente realizar novamente:

# calcular_media(*notas)

# Observe o comportamento e explique por que o quarto valor deixa de representar uma nota e passa a ocupar o parâmetro bonus.

def calcular_media(
        nota1: float,
        nota2: float,
        nota3: float,
        bonus: float = 0
) -> float:
    """
    Calcula a média de três notas e soma um bônus opcional.
    """
    media_notas = (nota1+nota2+nota3)/3
    media_bonus = media_notas + bonus
    return media_bonus

notas = [8.5, 7.0, 9.5]
resultado = calcular_media(*notas)
print(resultado)

notas = [8.5, 7.0, 9.5]
resultado = calcular_media(*notas, bonus=5)
print(resultado)

notas = [8.5, 7.0, 9.5, 10.0]
resultado = calcular_media(*notas)
print(resultado)

# o quarto valor vai para o bonus porque o desempacotamento com * não consegue reconhecer o significado dos
# valores somente os distribui na ordem da lista

# Exercício 16 – Unpacking com ** e argumentos nomeados

# Considere o seguinte dicionário:

# jogador = {"nome": "Marta","idade": 40,"posicao": "Atacante"}

# Crie uma função chamada apresentar_jogador que receba:

# - nome
# - idade
# - posicao

# A função deve:

# - Utilizar type hints em todos os parâmetros.
# - Indicar através do type hint que a função não retorna nenhum valor.
# - Possuir uma docstring.
# - Exibir uma mensagem com os dados do jogador.

# Chame a função desempacotando o dicionário com **.

# Você não deve acessar manualmente:

# jogador["nome"]
# jogador["idade"]
# jogador["posicao"]

# Depois, responda em um comentário no código:

# Por que as chaves do dicionário precisam possuir os mesmos nomes dos parâmetros da função?

jogador = {"nome": "Marta","idade": 40,"posicao": "Atacante"}

def apresentar_jogador(
        nome: str,
        idade: int,
        posicao: str
) -> None:
    """
    Retorna as informações dos jogadores.
    """
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Posição: {posicao}")

apresentar_jogador(**jogador)
    
# As chaves do dicionario precisam ter o mesmo nome dos paramentros porque o desempacotamento com **
# só desempacto argumentos nomeados

# Exercício 17 – *args recebendo e * desempacotando

# Crie uma função chamada calcular_total_gols que receba uma quantidade variável de números utilizando *args.

# A função deve:

# - Utilizar type hint no *args.
# - Possuir uma docstring.
# - Somar todos os valores recebidos.
# - Retornar o total de gols.
# Considere as listas:

# primeiro_tempo = [1, 2, 1]
# segundo_tempo = [2, 1]

# Chame a função desempacotando as duas listas na mesma chamada:

# total = calcular_total_gols(*primeiro_tempo,*segundo_tempo)
# print(total)

# Depois, escreva comentários no código explicando a diferença entre:

# def calcular_total_gols(*gols):...
# e:

# calcular_total_gols(*primeiro_tempo)

# Explique qual * está recebendo vários argumentos e qual está desempacotando uma coleção.

def calcular_total_gols(*gols: int) -> int:
    """
    Soma uma quantidade variável de gols e retorna o total.
    """

    total_gols = sum(gols)
    return total_gols

primeiro_tempo = [1, 2, 1]
segundo_tempo = [2, 1]

total = calcular_total_gols(*primeiro_tempo,*segundo_tempo)
print(total)

# em def calcular_total_gols(*gols), o * permite que a função
# receba vários argumentos posicionais e os reúna em uma tupla.

# em calcular_total_gols(*primeiro_tempo), o * desempacota a lista,
# enviando cada valor como um argumento separado para a função.

# Exercício 18 – Parâmetros somente posicionais com /

# Crie uma função chamada registrar_placar com a seguinte assinatura:

# def registrar_placar(time_a: str,time_b: str,/,gols_a: int,gols_b: int) -> str:...

# A função deve:

# - Possuir uma docstring.
# - Utilizar os type hints indicados.
# - Retornar uma string contendo o placar da partida.
# - Exigir que time_a e time_b sejam passados somente por posição.
# - Permitir que gols_a e gols_b sejam passados por posição ou pelo nome.

# Faça uma chamada válida utilizando:

# resultado = registrar_placar("Brasil","Argentina",gols_a=2,gols_b=1)
# print(resultado)

# Depois, tente:

# registrar_placar(time_a="Brasil",time_b="Argentina",gols_a=2,gols_b=1)

# Observe o erro e explique em um comentário qual é a função do / na assinatura.

def registrar_placar(
    time_a: str,
    time_b: str,
    /,
    gols_a: int,
    gols_b: int
) -> str:
    """
    Retorna o placar da partida entre dois times.
    """

    return f"{time_a}: {gols_a} gols, {time_b}: {gols_b} gols."

resultado = registrar_placar("Brasil","Argentina",gols_a=2,gols_b=1)
print(resultado)

registrar_placar(time_a="Brasil",time_b="Argentina",gols_a=2,gols_b=1)

# a função da / é determinar que todos os argumentos a esquerda sejam por posição.

# Exercício 19 – Parâmetros somente nomeados com *

# Crie uma função chamada criar_jogador com a seguinte assinatura:

# def criar_jogador(nome: str,*,posicao: str,numero: int,titular: bool = False) -> str:...

# A função deve:

# - Possuir uma docstring.
# - Utilizar type hints.
# - Utilizar um valor padrão para titular.
# - Retornar uma string com os dados do jogador.
# O parâmetro nome pode ser informado por posição.

# Os parâmetros após * devem ser informados pelo nome.

# Faça uma chamada válida:

# jogador = criar_jogador("Marta",posicao="Atacante",numero=10)
# print(jogador)

# Depois, faça outra chamada informando:

# titular=True

# Por fim, tente executar:

# criar_jogador("Marta","Atacante",10)

# Observe o erro e explique em um comentário por que posicao e numero não podem ser passados por posição.

def criar_jogador(
    nome: str,
    *,posicao: str,
    numero: int,
    titular: bool = False
) -> str:
    """
    Retorna as informações de um jogador.
    """
    return f"Nome: {nome} | Posição: {posicao} | Número: {numero} | Titular: {titular}"

jogador = criar_jogador("Marta",posicao="Atacante",numero=10)
print(jogador)

jogador = criar_jogador("Marta",posicao="Atacante",numero=10, titular=True)
print(jogador)

criar_jogador("Marta","Atacante",10)

# posicao e numero não podem ser passados por posição porque o * determina que os parametros 
# da direita devem ser nomeados.

# Exercício 20 – Desafio final: trabalhando com todos os tipos de argumentos

# Crie uma função chamada registrar_jogo com a seguinte assinatura:

# def registrar_jogo(
# mandante: str,
# visitante: str,
# /,
# competicao: str,
# *eventos: str,
# estadio: str,
# encerrado: bool = True,
# **informacoes
# ) -> dict:

# A função deve possuir uma docstring completa explicando:

# - O objetivo da função.
# - O que cada parâmetro representa.
# - O que a função retorna.

# A função também deve seguir estas regras:

# - mandante e visitante devem ser informados somente por posição.
# - competicao pode ser passada por posição ou pelo nome.
# - *eventos deve receber uma quantidade variável de eventos da partida.
# - estadio deve obrigatoriamente ser informado pelo nome.
# - encerrado deve possuir True como valor padrão.
# - **informacoes deve receber informações adicionais da partida.

# Dentro da função, crie e retorne um dicionário contendo:

# - Mandante.
# - Visitante.
# - Competição.
# - Eventos.
# - Estádio.
# - Situação da partida.
# - Informações adicionais.
# Teste a função com:

# partida = registrar_jogo(
# "Brasil",
# "Argentina",
# "Copa do Mundo",
# "Gol do Brasil",
# "Cartão amarelo",
# "Substituição",
# estadio="Maracanã",
# publico=70000,
# transmissao="TV"
# )
# print(partida)

# Depois, considere os seguintes dados:

# times = ["França", "Espanha"]
# dados = {"estadio": "Stade de France","publico": 65000,"transmissao": "Streaming"}

# Faça uma segunda chamada utilizando:

# - *times para desempacotar os dois primeiros argumentos.
# - Uma competição informada normalmente.
# - Dois ou mais eventos posicionais.
# - **dados para desempacotar as informações nomeadas.

# Ao final, escreva comentários identificando o papel de cada elemento da assinatura:

# /
# *eventos
# estadio
# encerrado=True
# **informacoes

# Explique também a diferença entre:

# *eventos
# na definição da função e:

# *times
# na chamada, assim como a diferença entre:

# **informacoes
# na definição e:

# **dados
# na chamada.

def registrar_jogo(
mandante: str,
visitante: str,
/,
competicao: str,
*eventos: str,
estadio: str,
encerrado: bool = True,
**informacoes
) -> dict:

    """
    Registra os dados de uma partida e retorna essas informações
    organizadas em um dicionário.

    mandante: nome do time da casa.
    visitante: nome do time visitante.
    competicao: competição em que a partida acontece.
    eventos: quantidade variável de eventos da partida.
    estadio: local onde a partida acontece, informado pelo nome.
    encerrado: indica se a partida foi encerrada.
    informacoes: informações adicionais sobre a partida.

    Retorna um dicionário com todos os dados do jogo.
    """
    
    jogo = {
    "Mandante": mandante,
    "Visitante": visitante,
    "Competição": competicao,
    "Eventos": eventos,
    "Estádio": estadio,
    "Situação da partida": encerrado,
    "Informações adicionais": informacoes
    }

    return jogo

partida = registrar_jogo(
"Brasil",
"Argentina",
"Copa do Mundo",
"Gol da França",
"Cartão amarelo",
"Substituição",
estadio="Maracanã",
publico=70000,
transmissao="TV"
)
print(partida)

times = ["França", "Espanha"]
dados = {"estadio": "Stade de France","publico": 65000,"transmissao": "Streaming"}

partida2 = registrar_jogo(
    *times,
    "Copa do Mundo",
    "Gol do Brasil",
    "Cartão amarelo",
    **dados
)
print(partida2)

# / exige que mandante e visitante sejam passados somente por posição.
# *eventos recebe vários argumentos posicionais e os reúne em uma tupla.
# estadio é um parâmetro obrigatório que deve ser informado pelo nome.
# encerrado=True define True como valor padrão para encerrado.
# **informacoes recebe vários argumentos nomeados e os reúne em um dicionário.

# *eventos, na definição, recebe e reúne vários argumentos posicionais.
# *times, na chamada, desempacota uma coleção e envia seus valores separadamente.
# **informacoes, na definição, recebe e reúne vários argumentos nomeados.
# **dados, na chamada, desempacota um dicionário e envia suas chaves como argumentos nomeados.