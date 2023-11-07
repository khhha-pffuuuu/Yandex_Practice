# Поразрядная сортировка

def max_digits_count(a):
    """Функция ищет максимальный разряд чисел в массиве"""
    max_digits = 0

    for elem in a:
        digits_count = len(str(elem))
        max_digits = max(digits_count, max_digits)

    return max_digits


def radix_sort(a: list):
    """Непосредственно сама сортировка"""
    sorted_a = [elem for elem in a]

    radix = 10  # Основание системы счисления
    buckets = [[] for _ in range(10)]
    digits_count = max_digits_count(sorted_a)

    for i in range(digits_count):
        for elem in sorted_a:
            digit = (elem // radix ** i) % radix  # Получаем цифру нужного разряда
            buckets[digit].append(elem)

        a_index = 0
        for j in range(len(buckets)):
            for k in range(len(buckets[j])):
                sorted_a[a_index] = buckets[j][k]
                a_index += 1

        buckets = [[] for _ in range(10)]

    return sorted_a
