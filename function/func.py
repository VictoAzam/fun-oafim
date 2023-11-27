import numpy as np
import matplotlib.pyplot as plt

def funcao_primeiro_grau(x, a, b):
    return a * x + b

def plotar_grafico(a, b):
    # Gerar valores de x
    x = np.linspace(-10, 10, 100)
    
    # Calcular os valores correspondentes de y
    y = funcao_primeiro_grau(x, a, b)
    
    # Plotar o gráfico
    plt.plot(x, y, label=f'{a}x + {b}')
    
    # Adicionar linhas vermelhas em y=0 e x=0
    plt.axhline(y=0, color='red', linestyle='--', label='y=0')
    plt.axvline(x=0, color='red', linestyle='--', label='x=0')
    
    # Adicionar rótulos e título ao gráfico
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Função de Primeiro Grau')
    
    # Adicionar a legenda
    plt.legend()
    
    # Exibir o gráfico
    plt.grid(True)
    plt.show()

# Obter os coeficientes a e b do usuário
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))

# Chamar a função para plotar o gráfico
plotar_grafico(a, b)
