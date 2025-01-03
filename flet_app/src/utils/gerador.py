from scipy.spatial import distance_matrix
import numpy as np
import itertools
import threading

def generate(locations):
    otimizadedList = []

    # Lista de localidades
    locality_list = list(locations.keys())

    # Função para verificar e converter coordenadas
    def parse_coordinates(value):
        if isinstance(value, str):
            try:
                return [float(coord.strip()) for coord in value.split(",")]
            except ValueError:
                print(f"Erro ao converter coordenadas: {value}")
                return None
        return value

    # Criar a matriz de coordenadas filtrando coordenadas válidas
    coords = np.array([parse_coordinates(value) for value in locations.values() if parse_coordinates(value) is not None])
    if len(coords) < len(locations):
        print("Algumas localidades têm coordenadas inválidas e foram ignoradas.")

    # Matriz de distâncias
    dist_matrix = distance_matrix(coords, coords)

    # Função para calcular a distância total de uma rota
    def total_distance(route):
        distance = 0
        distance += dist_matrix[0, route[0]]  # Distância de partida
        for i in range(len(route) - 1):
            distance += dist_matrix[route[i], route[i + 1]]  # Distância entre localidades
        distance += dist_matrix[route[-1], len(locality_list) - 1]  # Distância de chegada
        return distance

    # Função para encontrar a rota otimizada usando permutações
    def rotaOtimizada():
        # Permutações de rotas possíveis (excluindo primeira e última localidade)
        permutations = itertools.permutations(range(1, len(locality_list) - 1))
        optimal_route = min(permutations, key=total_distance)
        return optimal_route

    # Função nearest_neighbor para rotas grandes
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

    # Função com timeout para controle
    def rotaOtimizadaComTimeout(timeout):
        resultado = [None]

        def funcaoComTimeout():
            resultado[0] = rotaOtimizada()

        thread = threading.Thread(target=funcaoComTimeout)
        thread.start()
        thread.join(timeout)

        if thread.is_alive():
            print("Devido ao grande número de combinações, a rota será gerada usando o algoritmo de Nearest_neighbor")
            return nearest_neighbor(0, dist_matrix)  # Gerar usando nearest neighbor se o timeout ocorrer
        else:
            return resultado[0]

    # Executar função com timeout
    optimal_route = rotaOtimizadaComTimeout(5)

    print(f"Rota otimizada: {optimal_route}")

    if optimal_route:
        # Gerar lista otimizadedList com o nome das localidades e links do Google Maps
        if isinstance(optimal_route, tuple):  # Se usou rotaOtimizada
            optimized_localities = [locality_list[0]] + [locality_list[i] for i in optimal_route] + [locality_list[-1]]
        else:  # Se usou nearest_neighbor
            optimized_localities = [locality_list[i] for i in optimal_route]

        print(f"Localidades otimizadas: {optimized_localities}")

        for i in range(len(optimized_localities)):
            localidade = optimized_localities[i]
            otimizadedList.append(f"{localidade}, https://www.google.com/maps/search/?api=1&query={locations[localidade]}")

    return otimizadedList
