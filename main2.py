import re

import pandas as pd
import matplotlib.pyplot as plt

# Letra A
# extração da tabela
endereco = "https://en.wikipedia.org/wiki/List_of_chemical_elements"
Dd = pd.read_html(endereco, match="List of chemical elements")
print(Dd)

lista_liquido = []
lista_solido = []
lista_gasoso = []
lista_desconhecido = []


def coluna_tabela(nome_coluna):
    for coluna in Dd[0].columns:
        if nome_coluna in coluna:
            return coluna


coluna_fase = coluna_tabela('Phase at r.t.[j]')
coluna_nome = coluna_tabela('Name')
# Letra b
for element in Dd[0].to_dict(orient="records"):
    estado_do_elemento = element.get(coluna_fase)
    if estado_do_elemento == 'liquid':
        lista_liquido.append(element.get(coluna_nome))
    elif estado_do_elemento == 'solid':
        lista_solido.append(element.get(coluna_nome))
    elif estado_do_elemento == 'gas':
        lista_gasoso.append(element.get(coluna_nome))
    else:
        lista_desconhecido.append(element.get(coluna_nome))
print(f"Elementos solidos: {lista_solido}")
print(f"Elementos liquidos: {lista_liquido}")
print(f"Elementos gasosos: {lista_gasoso}")
print(f"Elementos desconhecidos: {lista_desconhecido}")

# Letra c
list_dict = []
for element in Dd[0].to_dict(orient="records"):
    elemento = {
        "periodo": element.get(coluna_tabela('Period')),
        "peso atomico": element.get(coluna_tabela("Standard atomic weight Ar°(E)[a]")),
        "densidade": element.get(coluna_tabela("Density[b][c]")),
        "temperatura de fusao": element.get(coluna_tabela("Melting point[d]")),
        "tempartura de ebuliçao": element.get(coluna_tabela("Boiling point[e]")),
        "capacidade calorifica": element.get(coluna_tabela("Specific heat capacity[f]")),
        "eletronegatividade": element.get(coluna_tabela("Unnamed: 12_level_2")),
        "abundacia na tera": element.get(coluna_tabela("Abundance in Earth's crust[h]"))
    }
    list_dict.append(elemento)
print(list_dict)

# Letra D
x = []
y = []
for e in list_dict:
    x_clean = re.sub('[^0-9.]', '', str(e.get("peso atomico")))
    y_clean = re.sub('[^0-9.]', '', str(e.get("eletronegatividade")))
    if x_clean != str(e.get("peso atomico")) or y_clean != str(e.get("eletronegatividade")):
        continue
    x.append(float(x_clean))
    y.append(float(y_clean))

plt.scatter(x, y)
plt.xlabel("peso atomico")
plt.ylabel("eletronegatividade")
plt.show()