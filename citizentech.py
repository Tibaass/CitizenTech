import os
import matplotlib.pyplot as plt
os.system('cls')

# Nossa ideia para a CitizenTech foi aplicar um  meio de prevenir o golpe digital (FiqueLigado) e para isso criamos uma projeção do crescimento de golpes digitais no país, a partir do ano de 2023, um dado real encontrado no canal do Senado Federal. O nosso objetivo é prevenir que adultos de 30 a 50 anos que fazem muitas transações bancarias e idosos não caiam nessas tentativas de fraude digital. 

print("---------------------------------------------------------------------")
print("Verifique o crescimento de casos de golpe digital a partir de 2023!")
print("---------------------------------------------------------------------")

anoEstimado = int(input("Digite em quantos anos você quer saber a projeção: "))

print("1 - Cenario Atual (Fator de crescimento de 26.3% ao ano)")
print("2 - Cenario com o FiqueLigado (Fator reduzido para 15% ao ano)")
escolha_cenario = int(input("Escolha o Cenario de simulação: "))

if escolha_cenario == 2:
    fator = 1.15
    nome_cenario = "com a aplicação do FiqueLigado"
else:
    fator = 1.263
    nome_cenario = "atual (sem intervenção)"

projecao = 222700 * fator ** anoEstimado

anoFinal = 2023 + anoEstimado

print(f"No ano de 2023, houve um aumento de 222.7 mil casos de golpes, segundo o\n Senado Federal e em {anoFinal} ({nome_cenario}) se tem uma projeção de {projecao:.0f} casos")

# ----- Gráfico da projeção -----
anos = []
casos_atual = []
casos_fiqueligado = []

for i in range(anoEstimado + 1):
    anos.append(2023 + i)
    casos_atual.append(222700 * 1.263 ** i)
    casos_fiqueligado.append(222700 * 1.15 ** i)

plt.figure(figsize=(10, 6))
plt.plot(anos, casos_atual, marker='o', color='red', label='Cenário atual (+26,3% ao ano)')
plt.plot(anos, casos_fiqueligado, marker='o', color='green', label='Com o FiqueLigado (+15% ao ano)')

# Destaca o ponto final do cenário que o usuário escolheu
plt.scatter([anoFinal], [projecao], s=200, color='black', zorder=5, label=f'Sua projeção ({nome_cenario})')

plt.title('Projeção de golpes digitais no Brasil a partir de 2023')
plt.xlabel('Ano')
plt.ylabel('Quantidade de casos')
plt.xticks(anos)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

print("\n                  CitizenTech © GPT Intelligency         ")

# Como pode-se observar a formula é basicamente formada pelo
# - f(x) = projecao
# - 222700 = quantidade inicial de registro a partir de 2023
# - fator = taxa de crescimento anual definida  pelo cenário escolhido:
#    - 1.263 (Cenario 1): crescimento atual de aproximadamente 26.3% ao ano sem intervenção
#    - 1.15 (Cenario 2): crescimento reduzido para 15% ao ano com a prevenção do FiqueLigado
# - anoEstimado (exponente) = quantidade de anos que o usuario queira saber a projeção

# GPT Intelligency
# Gustavo Suzuki Arakaki - RM 574700
# Pedro Henrique Pereira da Costa - RM 574484
# Tiago Faria de Almeida Ferreira - RM 562129