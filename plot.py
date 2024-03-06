import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('texto.txt', sep=',')

plt.plot(df['X'], df['Y'], df['Z'], label='PLT1')
plt.plot(df['Z'], df['Y'], df['X'], label='PLT2')
plt.title('Gráfico')
plt.legend()
plt.xlabel('Eixo X')
plt.ylabel("Eixo Y")
plt.show()
