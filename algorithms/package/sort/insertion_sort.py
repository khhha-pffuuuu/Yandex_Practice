# Сортировка вставками

def insertion_sort(a: list):
    """Функция сортировки вставками(ура, обошлось без дополнительных функций)"""
    sorted_a = [elem for elem in a]

    for i in range(1, len(sorted_a)):
        for j in reversed(range(i)):
            # Суем j+1-ый элемент в отсортированную часть
            if sorted_a[j + 1] < sorted_a[j]:
                (sorted_a[j], sorted_a[j + 1]) = (sorted_a[j + 1], sorted_a[j])
            else:  # Заканчиваем, когда элемент встанет на место
                break

    return sorted_a
