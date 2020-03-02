u"""
Максимум в скользящем окне
    Найти максимум в каждом окне размера m данного массива чисел A[1...n].

Вход.
    Массив чисел A[1...n] и число 1 ≤ m ≤ n.
Выход.
    Максимум подмассива A[i . . . i + m − 1] для всех 1 ≤ i ≤ n − m + 1.

Форматвхода.
    Первая строка входа содержит число n,вторая — масив A[1...n], третья — число m.
Формат выхода.
    n − m + 1 максимумов, разделённых пробелами.
Ограничения.
    1≤n≤105,1≤m≤n,0≤A[i]≤105 длявсех1≤i≤ n.
"""
# n = int(input())
#
# a = input()
#
# m = int(input())

n = 3
a = '3 7 2'
m = 1


def get_simple_algorithm(n, a, m):

    a = list(map(lambda x: int(x), a.split()))

    res = []

    buf = list()

    for k in range(len(a)):

        window = a[k:m+k:]

        if len(window) == m:
            buf.append(max(window))

    for k in range(n - m + 1):

        print(buf[k], end=' ')

        res.append(buf[k])

    print('\n')
    return res


# get_simple_algorithm(n, a, m)

# https://habr.com/en/post/116236/

def get_better_algorithm(n, a, m):

    a = list(map(lambda x: int(x), a.split()))

    b, c, res = [0 for _ in range(n)], [k for k in a[::-1]], []

    for i in range(n):

        b[i] = max(a[i], b[i-1]) \
            if i % (m - 1 if m > 1 else m) != 0 \
            else a[i]

    for i in reversed(range(n-1 if m > 1 else n)):

        c[i] = max(a[i], c[i+1]) \
            if (i+1) % (m - 1 if m > 1 else m) != 0 \
            else a[i]

    for k in range(n - m + 1):
        r = max(c[k], b[k + m - 1])

        print(max(c[k], b[k + m - 1]), end=' ')

        res.append(r)

    print('\n')
    return res

# get_better_algorithm(n, a, m)


# TESTS

test_input = ((15, '73 65 24 14 44 20 65 97 27 6 42 1 6 41 16 ', 7, '73 97 97 97 97 97 97 97 42'),
              (15, '28 7 64 40 68 86 80 93 4 53 32 56 68 18 59', 12, '93 93 93 93'),
              (15, '16 79 20 19 43 72 78 33 40 52 70 79 66 43 60', 12, '79 79 79 79'),
              (15, '34 51 61 90 26 84 2 25 7 8 25 78 21 47 25', 3, '61 90 90 90 84 84 25 25 25 78 78 78 47'),
              (15, '27 83 29 77 6 3 48 2 16 72 46 38 55 2 58', 5, '83 83 77 77 48 72 72 72 72 72 58'),
              (22, '3 7 2 4 9 2 1 10 3 8 11 10 4 17 9 20 22 8 20 4 3 9', 5, '9 9 9 10 10 10 11 11 11 17 17 20 22 22 22 '
                                                                            '22 22 20'),
              (8, '1 4 5 6 1 1 1 1', 4, '6 6 6 6 1'),
              (3, '2 3 9', 3, '9'),
              (3, '2 1 5', 1, '2 1 5'),
              (5, '5 2 2 1 9', 4, '5 9'),
              (3, '3 7 2', 1, '3 7 2'),
              )


def test_method(n, a, m, res=None):

    simple = ' '.join([str(elem) for elem in get_simple_algorithm(n, a, m)])

    complex = ' '.join([str(elem) for elem in get_better_algorithm(n, a, m)])

    assert simple == res

    assert complex == res

    assert complex == simple


for k in test_input:
    test_method(*k)
