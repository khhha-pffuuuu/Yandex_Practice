import package.adjuster as alg
from package.helpers import is_sorted

from random import randint as rand


def main():
    # Проверка сортировочных алгоритмов
    for _ in range(100):
        n = rand(0, 100)
        a = []
        for _ in range(n):
            a.append(rand(0, n * 100))

        print(f'Массив: {a}')

        rad_sort = alg.radix_sort(a)
        print(f'Поразрядная сортировка: {rad_sort}')
        if not is_sorted(rad_sort):
            print('Неправильный результат работы алгоритма')
            exit()

        q_sort = alg.quick_sort(a)
        print(f'Быстрая сортировка: {q_sort}')
        if not is_sorted(q_sort):
            print('Неправильный результат работы алгоритма')
            exit()

        m_sort = alg.merge_sort(a)
        print(f'Сортировка слиянием: {m_sort}')
        if not is_sorted(m_sort):
            print('Неправильный результат работы алгоритма')
            exit()

        ins_sort = alg.insertion_sort(a)
        print(f'Сортировка вставками: {ins_sort}')
        if not is_sorted(ins_sort):
            print('Неправильный результат работы алгоритма')
            exit()

        print()


if __name__ == '__main__':
    main()
