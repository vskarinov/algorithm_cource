
# #
# size, n = 1, 2
# q = '0 1\n0 1'

size, n = 0, 2
q = '0 1\n0 1'

# size = 2
# n = 8
# packages = [(0, 0), (0, 0), (0, 0), (1, 0), (1, 0), (1, 1), (1, 2), (1, 3)]
# packages = [(0, 0), (0, 0), (0, 0), (1, 1), (1, 0), (1, 0), (1, 2), (1, 3)]

# size = 2
# n = 3
# packages = [(1, 100),(1, 100), (1, 0)]
#
# size, n = 3, 6
# q = '0 7\n0 0\n2 0\n3 3\n4 4\n 5 5'
# '''0 7 7 -1 -1 -1'''
# size, n = 2, 6
# q = '0 2\n0 0\n2 0\n3 0\n4 0\n5 0'
# '''0 2 2 3 4 5'''

# size = 3
# n = 6
# packages = [(0, 2), (0, 0), (2, 0), (3, 0), (4, 0), (5, 0)]


# size = 1
# n = 5
# q = '999999 1\n1000000 0\n1000000 1\n1000000 0\n1000000 0'

#
# size, n = 2, 8
# q = '''0 0
# 0 0
# 0 0
# 1 0
# 1 0
# 1 1
# 1 2
# 1 3'''

# Ответ: 0 0 0 1 1 1 2 -1
# size, n = 3, 8
# q= '1 1\n2 2\n3 3\n4 4\n5 5\n6 6\n7 7\n8 8'
# 'Ответ: 1 2 4 7 11 -1 16 -1'


import sys
#
# size, n = list(map(lambda x: int(x), input().split(' ')))
#
# q = str()
#
# for line in sys.stdin:
#     if '' == line.rstrip():
#         break
#     q += line


packages = [tuple(int(k) for k in (el.split())) for el in q.split('\n') if q]


buffer = []
t_0, t_end = 0, 0
proc = []

for k in packages[:n:]:

    if not buffer:
        buffer.append(k[0])
        t_0 = k[0]
        t_end = k[0]+k[1]
    else:
        if k[0] == t_0 and len(buffer) < size:
            t_end += k[1] if t_end > k[0] + k[1] else 0
            buffer.append(t_end)
        elif k[0] < t_end and len(buffer) < size:
            buffer.append(t_end)
        elif k[0] >= t_end and len(buffer) <= size:
            go_to_process = buffer[0]
            while buffer.count(go_to_process) != 0:
                proc.append(buffer.pop(0))

            t_0 = k[0]
            buffer.append(t_0)
            t_end =  k[0] + k[1]
        else:
            buffer.append(-1)

while len(buffer) != 0:
    proc.append(buffer.pop(0))


sys.stdout.write(' '.join(list(map(lambda x:str(x), proc))))





