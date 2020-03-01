u"""
Скобки в коде

Проверить, правильно ли расставлены скобки в данном коде.
    Вход. Исходный код программы.
    Выход. Проверить, верно ли расставлены скобки. Если нет, выдать индекс первой ошибки.

Формат входа.
    Строка s[1 . . . n], состоящая из заглавных и пропис- ных букв латинского алфавита, цифр,
    знаков препинания и ско- бок из множества []{}().

Формат выхода.
    Если скобки в s расставлены правильно, выведите строку “Success".
    В противном случае выведите индекс (исполь- зуя индексацию с единицы) первой закрывающей скобки, для которой нет
    соответствующей открывающей. Если такой нет, выведите индекс первой открывающей скобки,
    для которой нет соответствующей закрывающей.
"""

input_string = '*{}'

# input_string = input()


def check_code(string):

    string_data = [k[0] for k in zip(enumerate(string))]

    stack_list = []

    for char in string_data:
        if char[1] in '({[':
            stack_list.append(char)
        elif char[1] not in '([{}])':
            continue
        else:
            if len(stack_list) == 0:
                return char[0] + 1
            else:
                top = stack_list.pop()
                if (top[1] == '(' and char[1] == ')') or \
                        (top[1] == '[' and char[1] == ']') or \
                        (top[1] == '{' and char[1] == '}'):
                    continue
                elif char[1] not in '([{}])':
                    stack_list.append(top)
                else:
                    return char[0] + 1
    return stack_list.pop()[0] + 1 if len(stack_list) != 0 else 'Success'


print(check_code(input_string))

# Test Cases

test_input = {'([](){([])})': 'Success',
              '()[]}': 5,
              '{{[()]]': 7,
              '{{{[][][]': 3,
              '{*{{}': 3,
              '[[*': 2,
              '{*}': 'Success',
              '{{': 2,
              '{}': 'Success',
              '': 'Success',
              '}': 1,
              '*{}': 'Success',
              '{{{**[][][]': 3,
              }


def test_method(i, o):
    assert check_code(i) == o


for i, o in test_input.items():
    test_method(i,o)


