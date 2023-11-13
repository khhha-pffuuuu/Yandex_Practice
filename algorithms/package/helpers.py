# Здесь будут храниться вспомогательные, чтобы не мусорить в других файлах

def is_sorted(a):
    """Функция проверяет отсортированность массива"""
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:  # Рассматриваем сортировки по возрастанию
            return False

    return True


def print_graph(graph, graph_type):
    """Функция выводит граф. Если граф задан матрицей смежности, то выводит матрицу, если списком смежности - список"""
    if graph_type == 'l':  # l = list
        for i in range(len(graph)):
            print(f'{i}: ', end='')
            if graph[i]:
                for j in range(len(graph[i])):
                    print(graph[i][j], end=' ')
                print()
            else:
                print('emp')  # Пусто
    if graph_type == 'm':  # m = matrix
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                print(graph[i][j] if graph[i][j] > -1 else 'emp', end=' ')
            print()
