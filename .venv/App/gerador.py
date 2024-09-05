from scipy.spatial import distance_matrix
import numpy as np
import itertools
import plotly.express as px
import pandas as pd
import multiprocessing

# Medir tempo da função



# Coordenadas dos pontos de atendimento
locations = {
    "São Jorge - RS": (-28.496389, -51.706667),
    "ARACI THEREZINHA FABRIS DAROS": (-28.5008704, -51.7057256),
    "PEDRO MOACIR FELIPPI": (-28.500555, -51.644722),
    "ISERTINO ROMEO CONTE": (-28.5025, -51.630000),
    "GELSON BORGES VIEIRA": (-28.499722, -51.65),
    "ARACI THEREZINHA FABRIS DAROS": (-28.5008704, -51.7057256),
    "PEDRO MOACIR FELIPPI": (-28.500555, -51.644722),

}

# Lista de localidades
locality_list = list(locations.keys())

# Matriz de coordenadas
coords = np.array(list(locations.values()))

# Matriz de distâncias
dist_matrix = distance_matrix(coords, coords)

# Lista de permutações de rotas possíveis excluindo a primeira e última localidade (São Jorge e Nova Prata)
permutations = itertools.permutations(range(1, len(locality_list) - 1))


# Função para calcular a distância total de uma rota, essa função tem crescimento exponencial dependendo a quantidade de localidades, a mesma será interrompida se passar de 5 segundos.
def total_distance(route):
    
    distance = 0
    # Adiciona a distância de São Jorge até o primeiro ponto
    distance += dist_matrix[0, route[0]]
    # Adiciona a distância entre os pontos intermediários
    for i in range(len(route) - 1):
        distance += dist_matrix[route[i], route[i + 1]]
    # Adiciona a distância do último ponto até Nova Prata
    distance += dist_matrix[route[-1], len(locality_list) - 1]

    return distance

# Encontra a rota com a menor distância total

def rotaOtimizada():
    optimal_route = min(permutations, key=total_distance)
    print(optimal_route)
    return optimal_route

optimal_route = rotaOtimizada()
# Monta a lista de localidades na ordem da rota otimizada
optimized_localities = ["São Jorge - RS"] + [locality_list[i] for i in optimal_route] + ["Nova Prata - RS"]
print(optimized_localities)

def nearest_neighbor(start_index, dist_matrix):
    n = len(dist_matrix)
    visited = [False] * n
    route = [start_index]
    visited[start_index] = True

    for _ in range(n - 1):
        last = route[-1]
        next_city = np.argmin([dist_matrix[last][j] if not visited[j] else float('inf') for j in range(n)])
        route.append(next_city)
        visited[next_city] = True

    return route

# Inicia em São Jorge - RS (índice 0) e encontra a rota otimizada
route_indices = nearest_neighbor(0, dist_matrix)

# Converte os índices da rota para nomes das localidades
optimized_localities = [locality_list[i] for i in route_indices]
print(optimized_localities)
# TESTE

def local_search(route, dist_matrix):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 1):
            for j in range(i + 1, len(route) - 1):
                new_route = route.copy()
                new_route[i], new_route[j] = new_route[j], new_route[i]
                if total_distance(new_route) < total_distance(route):
                    route = new_route
                    improved = True
    return route

# Obter uma solução inicial com o vizinho mais próximo
initial_route = nearest_neighbor(0, dist_matrix)

# Aplicar a busca local
best_route = local_search(initial_route, dist_matrix)

# Criando um DataFrame com as coordenadas da rota otimizada
df = pd.DataFrame({'Latitude': coords[best_route, 0],
                   'Longitude': coords[best_route, 1],
                   'Localidade': [locality_list[i] for i in best_route]})
print(df)

# fig = px.line_geo(df, lat='Latitude', lon='Longitude', scope='south america', hover_name='Localidade')
# fig.show()