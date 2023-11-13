import heapq

INF = 10 ** 18


class Node:
    """Класс узлов: [вершина, вес пути до вершины]"""
    def __init__(self, v, d):
        self.vert = v
        self.dist = d

    def __lt__(self, other):
        return self.dist < other.dist  # Сравнение проводится за счет веса


def dijkstra(graph, s, f):
    """Алгоритм Дейкстры на основе списка смежности"""
    n = len(graph)
    visited = [False] * n
    dist = [INF] * n

    queue = []  # Эта структура данных позволяет за O(lgN) получать вершину с минимальным весом
    heapq.heappush(queue, Node(s, 0))

    dist[s] = 0
    while queue:
        q = heapq.heappop(queue)  # Достаем верхний(минимальный) элемент кучи и удаляем его
        u, w = q.vert, q.dist

        for edge in graph[u]:
            if not visited[edge[0]]:
                if dist[edge[0]] > w + edge[1] and edge[1] > -1:
                    dist[edge[0]] = w + edge[1]
                    heapq.heappush(queue, Node(edge[0], dist[edge[0]]))  # Добавляем элемент к куче

        visited[u] = True

    res = dist[f] if dist[f] < INF else -1  # Если пути не существует, то выводим -1
    return res
