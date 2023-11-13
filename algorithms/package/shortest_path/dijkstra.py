INF = 10 ** 18


def dijkstra(graph, s, f):
    """Базовый алгоритм Дейкстры с использованием матрицы смежности"""
    n = len(graph)
    visited = [False] * n  # Список посещённых нами вершин(если мы проверили все ребра от этой вершины)
    dist = [INF] * n  # Список веса путей от вершины s до остальных вершин

    dist[s] = 0
    u = s
    while not visited[u]:
        for v in range(n):
            if not visited[v]:  # Имеет смысл рассматривать только непосещённые вершины
                if dist[v] > dist[u] + graph[u][v] and graph[u][v] > -1:  # Меняем вес пути только если он уменьшается
                    dist[v] = dist[u] + graph[u][v]

        visited[u] = True

        # Проводим линейный поиск непосещённой вершины с минимальным весом
        min_v, min_weight = s, INF
        for v in range(n):
            if not visited[v] and min_weight > dist[v]:
                min_v = v
                min_weight = dist[v]

        u = min_v

    res = dist[f] if dist[f] < INF else -1  # Если пути не существует, то выводим -1
    return res
