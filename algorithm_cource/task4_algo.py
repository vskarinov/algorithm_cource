u"""
Стек с поддержкой максимума
    Реализовать стек с поддержкой операций push, pop и max.

Вход.
    Последовательность запросов push, pop и max . Выход. Для каждого запроса max вывести максимальное число, находящееся на стеке.

Форматвхода.
    Первая строка содержит число запросов q.Каждая из последующих q строк задаёт запрос в одном из следующих фор-
    матов:push v, pop, or max.
Формат выхода.
    Для каждого запроса max выведите (в отдельной строке) текущий максимум на стеке.
Ограничения.
    1 ≤ q ≤ 400000, 0 ≤ v ≤ 100000.
"""
# import sys

n = 8
q = ['push 5', 'pop', 'push 3', 'max', 'push 9', 'pop', 'push 7', 'max']
for k in q:
    print(k, end='\n')


# n = int(input())
# q = str()
#
# for line in sys.stdin:
#     if '' == line.rstrip():
#         break
#     q += line

stack_1, stack_2 = [], []

query_stack = list(map(lambda x: tuple(x.split(' ')) if 'push' in x else x, q))


def make_pop():
    stack_1.pop()
    stack_2.pop()


def make_max():
    if stack_2:
        result = stack_2[-1]
        print(result, end='\n')
        return result
    else:
        return


def make_push(v):
    stack_1.append(v)
    if stack_2:
        top = stack_2.pop()
        if top >= v:
            stack_2.append(top)
            stack_2.append(top)
            return
        else:
            stack_2.append(top)
            stack_2.append(v)
    else:
        stack_2.append(v)


stack_commands = {'push': make_push,
                  'pop': make_pop,
                  'max': make_max}


def execute_stack_logic():
    for i in range(n):

        query_to_execute = query_stack[i]

        if type(query_to_execute) is tuple:
            stack_commands[query_to_execute[0]](int(query_to_execute[1]))
        else:
            stack_commands[query_to_execute]()

        # print(stack_1)
        # print(stack_2)

execute_stack_logic()


