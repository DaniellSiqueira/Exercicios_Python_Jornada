# Exercício 1 – Exibindo uma mensagem

# Crie uma função chamada exibir_boas_vindas() que exiba a mensagem: Bem-vindo ao sistema!

# Depois, chame a função para executar a mensagem.

# Requisitos:

# Utilize def.
# A função não deve receber parâmetros.
# A função não precisa retornar nenhum valor.

def exibir_boas_vindas():
    print("Bem-vindo ao sistema!")

exibir_boas_vindas()

# Exercício 2 – Identificando um produto

# Crie uma função chamada exibir_produto() que receba:

# o nome de um produto;
# o preço do produto.

# A função deve exibir uma mensagem no seguinte formato: Produto: Teclado | Preço: R$ 150.00

# Depois, chame a função passando um produto e um preço como argumentos.

# Requisitos:
# Utilize parâmetros.
# Adicione type hints nos parâmetros.
# A função deve retornar None.

def exibir_produto(produto: str, preco: float):
    print(f"Produto: {produto} | Preço: R$ {preco}")

exibir_produto("Teclado", 150.00 )

# Exercício 3 – Calculando o valor de uma compra

# Crie uma função chamada calcular_total() que receba:

# 1. o preço de um produto;
# 2. a quantidade comprada.

# A função deve calcular e retornar o valor total da compra.

# Exemplo:

# total = calcular_total(50.0, 3)
# print(total)

# Resultado esperado: 150.0

# Requisitos:
# preco deve possuir type hint float.
# quantidade deve possuir type hint int.
# A função deve indicar que retorna um float.
# Utilize return para devolver o resultado.

def calcular_total(preco: float, quantidade: int):
    valor_total = preco * quantidade
    return valor_total

total_compra = calcular_total(50.0, 3)
print(f"{total_compra:.2f}")

# Exercício 4 – Calculando a média de avaliações

# Uma plataforma armazena três avaliações dadas por usuários para um produto.

# Crie uma função chamada calcular_media_avaliacoes() que receba três notas e retorne a média entre elas.

# Depois, utilize o resultado retornado pela função para exibir a média das avaliações

# Requisitos:

# Utilize parâmetros e argumentos.
# Adicione type hints.
# Utilize return.
# Adicione uma docstring explicando o que a função recebe e o que retorna.
# Guarde o resultado da função em uma variável antes de exibi-lo.

def calcular_media_avaliacoes(nota1: int, nota2:int, nota3:int):

    """
    Calcula a média das notas.

    Args:
        nota1: primeira nota da avaliação.
        nota2: segunda nota da avaliação.
        nota3: terceira nota da avaliação.

    Returns:
        Média das notas:

    """

    total_notas = nota1 + nota2 + nota3
    media_notas = total_notas / 3
    return media_notas

media_avaliacoes = calcular_media_avaliacoes(5,10,9)
print(f"A média das avaliações foi: {media_avaliacoes:.2f}")

# Exercício 5 – Processando um pedido

# Você precisa criar duas funções para representar uma pequena parte de um sistema de pedidos.

# A primeira função deve se chamar: calcular_valor_final()

# Ela deve receber:

# preço unitário;
# quantidade;
# desconto em formato decimal.
# Por exemplo, 0.10 representa 10% de desconto.

# A função deve calcular e retornar o valor final do pedido após o desconto.

# Depois, crie uma segunda função chamada: exibir_resumo_pedido()

# Ela deve receber:
# número do pedido;
# valor final.

# E exibir uma mensagem como: Pedido #1025 finalizado. Total: R$ 270.00

# Requisitos:
# As duas funções devem possuir type hints.
# calcular_valor_final() deve retornar um float.
# exibir_resumo_pedido() deve retornar None.
# As duas funções devem possuir docstrings.
# O valor retornado por calcular_valor_final() deve ser passado como argumento para exibir_resumo_pedido().
# Não faça o cálculo diretamente fora da função.

def calcular_valor_final(preco: float,
                         quantidade: int,
                         desconto: float):

    """
    Calcula o valor final do pedido após aplicar o desconto.

    Args:
        preco: Valor unitário do produto.
        quantidade: Quantidade do produto no pedido.
        desconto: Valor do desconto.
    
    Returns:
        Valor final da compra
    
    """
    
    subtotal: float = preco * quantidade
    valor_desconto: float = subtotal * desconto
    total: float = subtotal - valor_desconto

    return total

def exibir_resumo_pedido(num_pedido: int, valor_final: float):

    """
    Exibe o resultado final do pedido

    Args:
        num_pedido: Numero de identificação do pedido
        valor_final: Resultado final do pedido depois dos descontos.
    
    Returns:
        Resumo do pedido.
    
    """
        
    print(f"Pedido #{num_pedido} finalizado. Total: R$ {valor_final:.2f}")

valor_final = calcular_valor_final(15.90, 26, 0.5)

exibir_resumo_pedido(1025, valor_final)

# Exercício 6 – Convertendo temperatura

# Crie uma função chamada converter_celsius_para_fahrenheit().

# A função deve receber uma temperatura em Celsius e retornar o valor convertido para Fahrenheit.

# Use a fórmula: fahrenheit = (celsius * 9 / 5) + 32

# Depois, armazene o resultado em uma variável e imprima a temperatura convertida.

# Requisitos:

# Receba a temperatura por parâmetro.
# Utilize type hint float.
# A função deve retornar um float.
# Utilize return.
# Adicione uma docstring explicando a função.

def converter_celsius_para_fahrenheit(celsius: float):

    """
    Converte o valor da temperatura em celsius para fahrenheit.
   
    Args:
        celsius: Valor da temperatura em celsius
    
    Returns:
        Temperatura convertida para fahrenheit
    
    """

    fahrenheit: float = (celsius * 9 / 5) + 32
    return fahrenheit

celsius_fahrenheit = converter_celsius_para_fahrenheit(32.2)
print(f"A conversão do valor para fahrenheit é {celsius_fahrenheit:.2f}")

# Exercício 7 – Calculando consumo médio

# Um veículo percorreu determinada distância utilizando uma quantidade de combustível.

# Crie uma função chamada calcular_consumo_medio() que receba:

# distância percorrida em quilômetros;
# quantidade de litros utilizados.

# A função deve retornar quantos quilômetros o veículo percorreu por litro.

# Exemplo: consumo = calcular_consumo_medio(420.0, 35.0)
# Resultado: 12.0

# Depois, crie uma segunda função chamada exibir_consumo() que receba o resultado e exiba: Consumo médio: {resultado} km/l

# Requisitos:
# As duas funções devem possuir type hints.
# calcular_consumo_medio() deve retornar float.
# exibir_consumo() deve retornar None.
# As duas funções devem possuir docstrings.
# O resultado da primeira função deve ser passado como argumento para a segunda.

def calcular_consumo_medio(distancia: float, litros: float):

    """
    Calcula a média de consumo por litro.
   
    Args:
        distancia: Distância percorrida em quilômetros.
        litros:Quantidade de litros utilizados.
    
    Returns:
        Média de KM por litro.
    
    """

    consumo_litro: float = distancia / litros
    return consumo_litro

def exibir_consumo(consumo: float):

    """
    Exibe a média de consumo por litro.
   
    Args:
        consumo: Média de consumo por litro.
    
    Returns:
        Consumo médio por km/l.
    
    """

    print(f"Consumo médio: {consumo:.2f} km/l")

consumo_por_litro = calcular_consumo_medio(420.0, 35.0)

exibir_consumo(consumo_por_litro)

# Exercício 8 – Verificando uma meta de vendas

# Crie uma função chamada calcular_percentual_meta() que receba:
# 1. valor da meta;
# 2. valor vendido.

# A função deve calcular e retornar o percentual da meta que foi atingido.

# Exemplo: percentual = calcular_percentual_meta(10000.0, 7500.0)
# Resultado: 75.0

# Depois, crie uma função chamada exibir_status_meta() que receba esse percentual.

# Ela deve exibir: Meta atingida!
# caso o percentual seja maior ou igual a 100.

# Caso contrário, deve exibir: Meta ainda não atingida.

# Requisitos:
# Utilize type hints.
# calcular_percentual_meta() deve retornar float.
# exibir_status_meta() deve retornar None.
# Utilize o valor retornado por uma função como argumento da outra.
# Adicione docstrings nas duas funções.
# Não repita o cálculo do percentual fora da função.

def calcular_percentual_meta(valor_meta:float, valor_venda: float):

    """
    Calcula o percentual da meta atingida.
   
    Args:
        valor_meta: Valor da meta a ser atingida.
        valor_venda: Valor da venda.

    Returns:
        Atingimento da meta.
    
    """

    percentual_meta: float = valor_venda / valor_meta * 100
    return percentual_meta

def exibir_status_meta(percentual_meta: float):

    """
    Exibe o status da meta.
   
    Args:
        percentual_meta: Atingimento da meta.

    Returns:
        Status da meta, se foi atingida ou não.
    
    """

    if percentual_meta >= 100.0:
        print("Meta atingida")
    else:
        print("Meta ainda não atingida.")

atingimento_meta = calcular_percentual_meta(10000.0, 9000.0)

exibir_status_meta(atingimento_meta)

print(atingimento_meta)

# Exercício 9 – Analisando uma entrega

# Você está desenvolvendo uma pequena parte de um sistema de entregas.

# Crie uma função chamada calcular_tempo_estimado() que receba:

# 1. distância da entrega em quilômetros;
# 2. velocidade média do veículo em km/h.

# A função deve calcular e retornar o tempo estimado da entrega em horas.

# Use: tempo = distancia / velocidade

# Depois, crie uma função chamada classificar_entrega() que receba o tempo calculado e retorne:

# "Entrega rápida" se o tempo for menor ou igual a 1;
# "Entrega normal" se o tempo for maior que 1 e menor ou igual a 3;
# "Entrega demorada" se o tempo for maior que 3.

# Por fim, crie uma terceira função chamada exibir_resumo_entrega() que receba:
# 1. o tempo estimado;
# 2. a classificação.

# Ela deve exibir algo como:
# Tempo estimado: 2.5 horas
# Classificação: Entrega normal


# Requisitos:
# As três funções devem possuir type hints.
# calcular_tempo_estimado() deve retornar float.
# classificar_entrega() deve retornar str.
# exibir_resumo_entrega() deve retornar None.
# Todas devem possuir docstrings.
# O resultado de calcular_tempo_estimado() deve ser utilizado por classificar_entrega().
# Os resultados das duas primeiras funções devem ser utilizados por exibir_resumo_entrega().
# Cada função deve possuir apenas uma responsabilidade.

def calcular_tempo_estimado(distancia: float, velocidade:float):

    """
    Calcula o tempo estimado da entrega.
   
    Args:
        distancia: Distância da entrega em quilômetros.
        velocidade: Velocidade média do veículo em km/h.

    Returns:
        Tempo estimado da entrega.
    
    """

    tempo: float = distancia / velocidade
    return tempo

def classificar_entrega(tempo: float):

    """
    Classifica a entrega de acordo com o tempo estimado.
   
    Args:
        tempo: Tempo estimado da entrega

    Returns:
        Classificação da entrega, entre: rápida, normal ou demorada.
    
    """

    if tempo <= 1:
        return "Entrega rápida"
    elif tempo <= 3:
        return "Entrega normal"
    else:
        return "Entrega demorada"

def exibir_resumo_entrega(tempo_estimado:float, classificacao:str):

    """
    Exibe o resumo da entrega.
   
    Args:
        tempo_estimado: Tempo estimado da entrega.
        classificacao: Classificação da entrega

    Returns:
        Resumo da entrega com tempo estimado e classificação.
    
    """

    print(f"Tempo estimado: {tempo_estimado:.2f} horas")
    print(f"Classificação: {classificacao}")

tempo_estimado = calcular_tempo_estimado(150.5, 95.5)

classificacao = classificar_entrega(tempo_estimado)

exibir_resumo_entrega(tempo_estimado, classificacao)

# Exercício 10 – Sistema de Aprovação de Empréstimo

# Você está desenvolvendo uma parte de um sistema bancário responsável por analisar solicitações de empréstimo.

# O programa deverá utilizar várias funções, e cada uma terá uma responsabilidade específica.

# 1. Calcular comprometimento da renda
# Crie uma função chamada calcular_comprometimento_renda() que receba:

# renda mensal;
# valor da parcela do empréstimo.
# Ela deve calcular qual percentual da renda mensal seria comprometido pela parcela.

# Use:

# percentual = (parcela / renda) * 100

# A função deve retornar esse percentual.

# 2. Analisar o empréstimo
# Crie uma segunda função chamada analisar_emprestimo() que receba:

# renda mensal;
# valor solicitado;
# percentual de comprometimento da renda.
# A função deve retornar uma das seguintes classificações:

# "Aprovado"
# "Análise manual"
# "Recusado"

# Utilize estas regras:

# Se o comprometimento da renda for maior que 40%, retorne "Recusado".
# Se o comprometimento for menor ou igual a 40%, mas o valor solicitado for maior que 5 vezes a renda mensal, retorne "Análise manual".
# Caso contrário, retorne "Aprovado".

# 3. Calcular o total do pagamento
# Crie uma terceira função chamada calcular_total_pagamento() que receba:

# valor da parcela;
# quantidade de parcelas.
# Ela deve retornar o valor total que será pago ao final do empréstimo.

# Exemplo:

# Parcela: R$ 850.00
# Quantidade: 24
# Total pago: R$ 20400.00

# 4. Exibir o resultado final
# Por fim, crie uma função chamada exibir_resultado() que receba:

# valor solicitado;
# percentual de comprometimento;
# total que será pago;
# resultado da análise.
# Ela deve apenas exibir um resumo como:

# --- Análise do empréstimo ---

# Valor solicitado: R$ 15000.00
# Comprometimento da renda: 28.3%
# Total a pagar: R$ 20400.00

# Resultado: Aprovado

# Essa função não deve retornar nenhuma informação.

# Requisitos
# Todas as funções devem possuir type hints.
# Todas devem possuir docstrings.
# calcular_comprometimento_renda() deve retornar float.
# analisar_emprestimo() deve retornar str.
# calcular_total_pagamento() deve retornar float.
# exibir_resultado() deve retornar None.
# Os cálculos devem acontecer dentro das funções responsáveis por eles.
# Não repita cálculos fora das funções.
# Os valores retornados pelas funções devem ser armazenados em variáveis e reutilizados nas próximas etapas.
# A função exibir_resultado() deve apenas receber os resultados já calculados e exibi-los.
# Não utilize *args, **kwargs, parâmetros com valores padrão ou outros recursos ainda não vistos nesta aula.

# Fluxo esperado

# dados do empréstimo
# ↓
# calcular comprometimento da renda
# ↓
# analisar empréstimo
# ↓
# calcular total do pagamento
# ↓
# exibir resultado final

# O objetivo é organizar um problema maior em funções menores, fazendo com que o retorno de uma etapa seja utilizado pelas próximas.

def calcular_comprometimento_renda(renda: float, parcela: float):

    """
    Calcula comprometimento da renda.
   
    Args:
        renda: Renda mensal.
        parcela: Valor da parcela do empréstimo.

    Returns:
        Valor percentual de comprometimento da renda. 
    
    """

    percentual: float = (parcela / renda) * 100
    return percentual

def analisar_emprestimo(renda: float, valor_solicitado: float, percentual: float):

    """
    Analisa a solicitação do empréstimo.
   
    Args:
        renda: Renda mensal.
        valor_solicitado: Valor do empréstimo.
        percentual: Percentual de comprometimento da renda.

    Returns:
        Status da avaliação do empréstimo. entre: Recusado, Análise manual ou Aprovado.
    
    """

    if percentual > 40:
        return "Recusado"
    elif percentual <= 40 and valor_solicitado > renda * 5:
        return "Análise manual"
    else:
        return "Aprovado"

def calcular_total_pagamento(parcela: float, qtd_parcelas: int):

    """
    Calcula o total a ser pago no final do empréstimo.
   
    Args:
        parcela: Valor da parcela.
        qtd_parcelas: Quantidade de parcelas.

    Returns:
        Valor total a ser pago no empréstimo.
    
    """

    total_pagar: float = parcela * qtd_parcelas
    return total_pagar

def exibir_resultado(valor_solicitado: float, percentual: float, total_pagar: float, resultado: str):

    """
    Exibe o resultado do empréstimo.
   
    Args:
        valor_solicitado: Valor do empréstimo.
        percentual: Valor percentual de comprometimento da renda.
        total_pagar: Valor total a ser pago no empréstimo.
        resultado: Status da avaliação do empréstimo.

    Returns:
        Exibe o resultado do empréstimo com todos os detalhes.
    
    """

    print("--- Análise do empréstimo ---")
    print("")
    print(f"Valor solicitado: {valor_solicitado:.2f}")
    print(f"Comprometimento da renda: {percentual:.2f}%")
    print(f"Total a pagar: R$ {total_pagar:.2f}")
    print("")
    print(f"Resultado: {resultado}")

comprometimento_renda = calcular_comprometimento_renda(2500.0, 850.0)

resultado_analise = analisar_emprestimo(2500.0, 15000.0, comprometimento_renda)

total_a_pagar =calcular_total_pagamento(850.0, 24)

exibir_resultado(15000.0, comprometimento_renda, total_a_pagar, resultado_analise)