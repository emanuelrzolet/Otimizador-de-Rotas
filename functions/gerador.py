from scipy.spatial import distance_matrix
import numpy as np
import itertools
import threading
import json
def generate(locations):
    otimizadedList =list()
    
    # Coordenadas dos pontos de atendimento

    # Lista de localidades
    locality_list = list(locations.keys())

    # Matriz de coordenadas
    coords = np.array(list(locations.values()))

    # Matriz de distâncias
    dist_matrix = distance_matrix(coords, coords)

    # Lista de permutações de rotas possíveis excluindo a primeira e última localidade (São Jorge e Nova Prata)
    permutations = itertools.permutations(range(1, len(locality_list) - 1))

    # Função para calcular a distância total de uma rota.
    def total_distance(route):
        distance = 0
        # Adiciona a distância de São Jorge até o primeiro ponto
        distance += dist_matrix[0, route[0]]
        # Adiciona a distância entre os pontos intermediários
        for i in range(len(route) - 1):
            distance += dist_matrix[route[i], route[i + 1]]
        # Adiciona a distância do último ponto até o destino
        distance += dist_matrix[route[-1], len(locality_list) - 1]
        return distance

    # Função para controlar o tempo limite de execução
    def rotaOtimizadaComTimeout(timeout):
        resultado = [None]  # Lista mutável para capturar o retorno da função

        def funcaoComTimeout():
            resultado[0] = rotaOtimizada()

        # Criar thread para executar a função
        thread = threading.Thread(target=funcaoComTimeout)
        thread.start()

        # Aguarda o término da thread ou o timeout
        thread.join(timeout)

        # Verificar se a função terminou a execução no tempo
        if thread.is_alive():
            print("Devido ao grande número de combinações, a rota será gerada usando o algoritmo de Nearest_neighbor")
            
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

            # Impressão formatada de nome e coordenadas
            for i in route_indices:
                otimizadedList.append(f"{locality_list[i]}, https://www.google.com/maps/search/?api=1&query={locations[locality_list[i]]}")
                return otimizadedList

        else:
            return resultado[0]  # Se terminou no tempo, retornamos o resultado

    # Função para encontrar a rota otimizada
    def rotaOtimizada():
        optimal_route = min(permutations, key=total_distance)
        return optimal_route

    # Executar a função com limite de tempo
    optimal_route = rotaOtimizadaComTimeout(5)

    # Verificar se a rota otimizada foi encontrada dentro do tempo e imprimir
    if optimal_route:
        optimized_localities = [locality_list[0]] + [locality_list[i] for i in optimal_route] + [locality_list[-1]]
        
        # Impressão formatada de nome e coordenadas
        for i in optimal_route:
            otimizadedList.append(f"{locality_list[i]}, https://www.google.com/maps/search/?api=1&query={locations[locality_list[i]]}")
        return otimizadedList