from scipy.spatial import distance_matrix
import numpy as np
import itertools

# Coordenadas dos pontos de atendimento
locations = {
    "São Jorge - RS": (-28.496389, -51.706667),
    "ARACI THEREZINHA FABRIS DAROS": (-28.5008704, -51.7057256),
    "PEDRO MOACIR FELIPPI": (-28.500555, -51.644722),
    "ISERTINO ROMEO CONTE": (-28.5025, -51.630000),
    "GELSON BORGES VIEIRA": (-28.499722, -51.65),
    "JOSE DOMINGOS SIMIONI": (-28.490833, -51.659722),
    "ANTONIO SIMIONI": (-28.489999, -51.658888),
    "ADEMIR BASSOLI": (-28.481944, -51.667222),
    "DIONISIO BRESOLIN": (-28.482500, -51.662777),
    "PEDRINHO POLLI": (-28.493611, -51.6625),
    "EDEGAR POLLI": (-28.498055, -51.665555),
    "ADAIR JOSE PONTEL": (-28.51, -51.654444),
    "WALTER VIAPIANA": (-28.506944, -51.65),
    "ULISSES VIAPIANA": (-28.5001528, -51.7051189),
    "Nova Prata - RS": (-28.779167, -51.611944)
}

# Lista de localidades
locality_list = list(locations.keys())

# Matriz de coordenadas
coords = np.array(list(locations.values()))

# Matriz de distâncias
dist_matrix = distance_matrix(coords, coords)

# Lista de permutações de rotas possíveis excluindo a primeira e última localidade (São Jorge e Nova Prata)
permutations = itertools.permutations(range(1, len(locality_list) - 1))

# Função para calcular a distância total de uma rota
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
optimal_route = min(permutations, key=total_distance)

# Monta a lista de localidades na ordem da rota otimizada
optimized_localities = ["São Jorge - RS"] + [locality_list[i] for i in optimal_route] + ["Nova Prata - RS"]
print(optimized_localities)



#Caso der erro

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
