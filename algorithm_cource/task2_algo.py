u"""
Высота дерева
    Вычислить высоту данного дерева.
Вход.
    Корневое дерево с вершинами {0, . . . , n−1}, заданное как последовательность parent ,...,parent ,где parent —
    родитель i-й вершины.
Выход.
        Высота дерева.

Формат входа.
    Первая строка содержит натуральное числоn. Вторая
    строка содержит n целых чисел parent0, . . . , parentn−1. Для каждо-
    го 0 ≤ i ≤ n−1, parent — родитель вершины i; если parent = −1, ii
    то i является корнем. Гарантируется, что корень ровно один. Га- рантируется,
    что данная последовательность задаёт дерево.
Формат выхода.
    Высота дерева.

"""

n = int('5')
parents = '4 -1 4 1 1'

# n = int(input())
#
# parents = input()


def depth_node(parents, k , depth):

    if depth[k] != 0:
        return

    if parents[k] == -1:
        depth[k] = 1
        return

    if depth[parents[k]] == 0:
        depth_node(parents, parents[k], depth)

    depth[k] = depth[parents[k]] + 1


def height_tree(num, parents):

    parents = list(map(lambda x: int(x), parents.split()))

    depth = [0 for k in range(num)]

    for i in range(num):
        depth_node(parents, i, depth)

    ht = depth[0]
    for i in range(1, num):
        ht = max(ht, depth[i])

    return ht


print(height_tree(n, parents))


test_input = {
             '1 5 5 2 2 -1 3': (7, 4),
             '-1 0 0 1 1 3 5': (7, 5),
             '-1 0 4 0 3': (5, 4),
             '4 -1 4 1 1': (5, 3)
             }


def test_method(i, o):
    assert height_tree(o[0], i) == o[1]


for i, o in test_input.items():
    test_method(i, o)