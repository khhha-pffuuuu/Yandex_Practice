# Здесь будут храниться вспомогательные, чтобы не мусорить в других файлах

def is_sorted(a):
    """Функция проверяет отсортированность массива"""
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:  # Рассматриваем сортировки по возрастанию
            return False

    return True
