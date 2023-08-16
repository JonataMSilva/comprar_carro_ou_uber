"""
Sabemos que andar somente por aplicativo nos dá muitas facilidades, como não precisar investir em garagem, seguro e nem encontrar um bom mecânico. Além disso, o custo fixo em andar por aplicativo é zero, porém o custo variável é bem mais alto do que ao possuir um carro. Sem contar que ao investir o dinheiro ao invés de comprar um carro à vista, isso ainda geraria uma renda pelos investimentos, que seria utilizada para abater parte dos custos da viagem pelo Uber.

Vamos aos números:
Valor base de um veículo: R$ 41.150,00
Seguro anual do veículo: 8%
Custo de combustível por km: R$ 0,32
Custo de revisão por km: R$ 0,42
Estacionamento anual: R$ 3600,00
IPVA (anual): 1528,40

Custo por km utilizando um aplicativo: R$ 1,92
Rendimento anual do investimento: 13,65%

Percebe-se que se o usuário percorre pequenas distâncias mensalmente, vale muito a pena andar por aplicativo e não se preocupar em possuir um veículo.

Construa um programa que, com base nos dados acima, informa ao usuário qual a distância mínima percorrida mensalmente por uma pessoa para valer a pena comprar um carro e não andar de Uber.
"""

valor_carro = 41150.00
seguro_anual = valor_carro * 0.08
custo_combustivel_km = 0.32
custo_revisao_km = 0.42
estacionamento_anual = 3600
ipva = 1528.40

custo_uber_km = 1.92
rendimento_anual = valor_carro * 0.1365

gasto_fixo_por_mes = (valor_carro + seguro_anual + estacionamento_anual +
                      ipva) / 12
gasto_variavel_por_km = custo_combustivel_km + custo_revisao_km

rendimento_mes = rendimento_anual / 12

km_mensal = float(input("Digite quantos KM você anda no mês: "))

custo_carro = km_mensal * gasto_variavel_por_km + gasto_fixo_por_mes
custo_uber = km_mensal * custo_uber_km - rendimento_mes

#print(custo_carro)
#print(custo_uber)

if custo_carro < custo_uber:
  print("Melhor comprar um carro")
else:
  print("Andar de Uber é mais vantajoso")
