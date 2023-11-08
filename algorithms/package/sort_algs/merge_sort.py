# Сортировка слиянием

def merge(a, l, c, r):
    """Функция "сливает" отсортированные массивы в один отсортированный"""
    n = c - l + 1  # Размер первой половины
    m = r - c  # Размер второй половина

    f_half = a[l: c + 1] + [1000000001]  # Первая половина + большое число в конце(для корректной работы алгоритма)
    s_half = a[c + 1: r + 1] + [1000000001]  # Вторая половина + большое число в конце

    iter_f, iter_s = 0, 0  # Будем сдвигать итераторы по мере нахождения минимальных элементов в "подмассивах"

    while iter_f + iter_s < n + m:
        if f_half[iter_f] < s_half[iter_s]:
            a[l + iter_f + iter_s] = f_half[iter_f]
            iter_f += 1
        else:
            a[l + iter_f + iter_s] = s_half[iter_s]
            iter_s += 1


def sort(a, l, r):
    """Непосредственно функция merge sort"""
    if l < r:
        c = (l + r) // 2

        # Делим заданный промежуток пополам
        sort(a, l, c)
        sort(a, c + 1, r)
        merge(a, l, c, r)


def merge_sort(a: list):
    """Функция упрощает использование сортировки"""
    sorted_a = [elem for elem in a]
    sort(sorted_a, 0, len(sorted_a) - 1)

    return sorted_a
