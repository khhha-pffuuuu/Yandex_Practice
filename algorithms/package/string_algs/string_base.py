def prefix_func(s):
    """Префикс функция создает массив, где на i-ом элементе стоит длина совпадающих суффикса и префикс"""
    n = len(s)
    prefix_list = [0] * n
    for i in range(1, n):
        j = prefix_list[i - 1]
        while j > 0 and s[i] != s[j]:
            j = prefix_list[j - 1]
        if s[i] == s[j]:
            j += 1
        prefix_list[i] = j

    return pf_list


def str_base(s):
    """Функция ищет основание строки"""
    pf_list = prefix_func(s)

    s_len = 0
    for i in range(len(s)):
        if pf_list[i] == 1:
            s_len = i
        if pf_list[i] == 0:
            s_len = i + 1

    return s_len
