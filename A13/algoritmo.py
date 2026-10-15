import time
import tracemalloc
import itertools
import random
from heapq import heappush, heappop

def generate_synthetic_graph(num_nodes: int, weighted: bool = True):
    """Genera un grafo sintético completo y ponderado representado como matriz de adyacencia."""
    graph = [[0.0] * num_nodes for _ in range(num_nodes)]
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i == j:
                graph[i][j] = 0.0
            elif j > i:
                weight = float(random.randint(1, 100)) if weighted else 1.0
                graph[i][j] = weight
                graph[j][i] = weight
    return graph

def run_dijkstra(graph, start: int, end: int):
    tracemalloc.start()
    start_time = time.perf_counter()
    
    n = len(graph)
    distances = {i: float('inf') for i in range(n)}
    distances[start] = 0.0
    pq = [(0.0, start)]
    paths = {start: [start]}
    nodes_visited = 0

    while pq:
        current_distance, u = heappop(pq)
        nodes_visited += 1

        if u == end:
            break

        if current_distance > distances[u]:
            continue

        for v in range(n):
            weight = graph[u][v]
            if weight > 0 and u != v:
                distance = current_distance + weight
                if distance < distances[v]:
                    distances[v] = distance
                    paths[v] = paths[u] + [v]
                    heappush(pq, (distance, v))

    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    execution_time_ms = (end_time - start_time) * 1000
    path_cost = distances[end] if distances[end] != float('inf') else -1
    path = paths.get(end, [])

    return {
        "execution_time_ms": round(execution_time_ms, 4),
        "memory_consumed_kb": round(peak / 1024, 2),
        "nodes_visited": nodes_visited,
        "path_cost": path_cost,
        "path": path
    }

def run_tsp_greedy(graph, start: int = 0):
    tracemalloc.start()
    start_time = time.perf_counter()
    
    n = len(graph)
    unvisited = set(range(n))
    current = start
    unvisited.remove(current)
    path = [current]
    total_cost = 0.0
    nodes_visited = 1

    while unvisited:
        next_node = min(unvisited, key=lambda node: graph[current][node])
        total_cost += graph[current][next_node]
        current = next_node
        unvisited.remove(current)
        path.append(current)
        nodes_visited += 1

    # Regresar al nodo inicial para cerrar el ciclo
    total_cost += graph[current][start]
    path.append(start)

    end_time = time.perf_counter()
    current_mem, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    execution_time_ms = (end_time - start_time) * 1000

    return {
        "execution_time_ms": round(execution_time_ms, 4),
        "memory_consumed_kb": round(peak / 1024, 2),
        "nodes_visited": nodes_visited,
        "path_cost": total_cost,
        "path": path
    }

def run_tsp_exact(graph):
    """Algoritmo exacto para TSP usando Programación Dinámica (Held-Karp) para soportar hasta 15 nodos."""
    tracemalloc.start()
    start_time = time.perf_counter()
    
    n = len(graph)
    memo = {}
    nodes_visited = 0

    def visit(mask, pos):
        nonlocal nodes_visited
        nodes_visited += 1
        if mask == (1 << n) - 1:
            return graph[pos][0], [pos, 0]
        
        if (mask, pos) in memo:
            return memo[(mask, pos)]

        ans = float('inf')
        best_path = []

        for nxt in range(n):
            if not (mask & (1 << nxt)) and graph[pos][nxt] > 0:
                new_cost, new_path = visit(mask | (1 << nxt), nxt)
                cost = graph[pos][nxt] + new_cost
                if cost < ans:
                    ans = cost
                    best_path = [pos] + new_path

        memo[(mask, pos)] = (ans, best_path)
        return ans, best_path

    min_cost, path = visit(1, 0)

    end_time = time.perf_counter()
    current_mem, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    execution_time_ms = (end_time - start_time) * 1000

    return {
        "execution_time_ms": round(execution_time_ms, 4),
        "memory_consumed_kb": round(peak / 1024, 2),
        "nodes_visited": nodes_visited,
        "path_cost": min_cost,
        "path": path
    }