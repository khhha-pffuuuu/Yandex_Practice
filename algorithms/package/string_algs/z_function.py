def z_function(s):
    """Z-функция возвращает список, где на i-ой позиции стоит k совпадающих символов
    префикса строки (т.е. s[0: z[i]]) и префикса подстроки s[i: i + z[i]]"""
    n = len(s)

    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        z[i] = max(0, min(r - i, z[i - l]))  # Лемма

        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1

        if i + z[i] > r:
            r = i + z[i]
            l = i

    return z


def search_substrings(t, s):
    """Функция возвращает индексы, где в строчке s встречается шаблон t (|t|<=|s|)"""
    n = len(t)
    strs_unit = f'{t}${s}'
    z = z_function(strs_unit)

    indexes = []
    for i in range(n + 1, len(z)):
        if z[i] == n:
            indexes.append(i - n - 1)

    return indexes
