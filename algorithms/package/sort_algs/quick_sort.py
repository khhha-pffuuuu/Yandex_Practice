# Быстрая сортировка
from random import randint as rand


def partition(a, l, r, x):
    """Функция разделяет массив на три части: меньшую заданного x, равную и большую"""
    eq_index = l
    ge_index = l

    for i in range(l + 1, r + 1):
        if a[i] < x:
            add = a[i]
            a[i] = a[ge_index]
            a[ge_index] = a[eq_index]
            a[eq_index] = add

            eq_index += 1
            ge_index += 1
        elif a[i] == x:
            a[ge_index], a[i] = a[i], a[ge_index]
            ge_index += 1

    return eq_index, ge_index


def sort(a, l, r):
    """Непосредственно сама quick sort"""
    if l < r:
        rand_index = rand(l, r)  # Случайный индекс в заданном промежутке
        a[l], a[rand_index] = a[rand_index], a[l]
        parts = partition(a, l, r, a[l])

        # На основе индексов, полученных из partition, делим заданный
        # промежуток на две части(не включая часть равную x)
        sort(a, l, parts[0] - 1)
        sort(a, parts[1], r)


def quick_sort(a: list):
    """Функция вызывает quick sort в удобном для пользователя формате"""
    sorted_a = [elem for elem in a]
    sort(sorted_a, 0, len(sorted_a) - 1)

    return sorted_a
