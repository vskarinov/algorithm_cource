
# #
# size = 1
# n = 2
# packages = [(0, 1), (0, 1), (2, 2), (3, 3)]

# size = 2
# n = 8
# packages = [(0, 0), (0, 0), (0, 0), (1, 0), (1, 0), (1, 1), (1, 2), (1, 3)]
# packages = [(0, 0), (0, 0), (0, 0), (1, 1), (1, 0), (1, 0), (1, 2), (1, 3)]

# size = 2
# n = 3
# packages = [(1, 100),(1, 100), (1, 0)]
#
# size = 3
# n = 6
# packages = [(0, 7), (0, 0), (2, 0), (3, 3), (4, 0), (5, 0)]
'''0 7 7 -1 -1 -1'''
# size = 2
# n = 6
# packages = [(0, 2), (0, 0), (2, 0), (3, 0), (4, 0), (5, 0)]
# '''0 2 2 3 4 5'''

# size = 3
# n = 6
# packages = [(0, 2), (0, 0), (2, 0), (3, 0), (4, 0), (5, 0)]

#
# size = 1
# n = 5
# packages = [(999999, 1), (1000000, 0), (1000000, 1), (1000000, 0), (1000000, 0)]


size, n = 2, 8
q = '''0 0
0 0
0 0
1 0
1 0
1 1
1 2
1 3'''

# Ответ: 0 0 0 1 1 1 2 -1


import sys

# size, n = list(map(lambda x: int(x), input().split(' ')))



# q = str()
#
# for line in sys.stdin:
#     if '' == line.rstrip():
#         break
#     q += line


packages = [tuple(int(k) for k in (el.split())) for el in q.split('\n')]

buf = 0
proc = []
proc_time = None

for k in packages[:n:]:

    if not proc_time:
        proc_time = k[1]
        proc.append(k[0])
        buf+=1
        continue

    if k[1] + k[0] > proc_time :
        proc.append(k[1])
        proc_time = k[1]
        buf = 0

    elif k[1] == 0 and buf == size and k[0] == proc_time:
        proc.append(proc_time)
        buf -=1

    elif k[1] + k[0] < proc_time and buf < size:
        proc.append(proc_time)
        buf += 1

    # elif k[1] + k[0] == proc_time:
    #     if buf == size:
    #         proc.append(-1)
    #     else:
    #         proc.append(proc_time)

    else:
        proc.append(-1)



print(*proc)


