import numpy as np
import sys

import detect
import funcs

sys.setrecursionlimit(10 ** 7)

code = """
def func(n):
    s = 0
    for i in range(n):
        s += i
    return s
"""

modified_code = funcs.modify_code(code)
print('--------------')
print(modified_code)
print('--------------')

exec(modified_code)

x = []
y = []
# for i in range(200, 10200, 200):
#     operate_count = 0
#     test_time = 10
#     for n in range(test_time):
#         ran_list = [random.random() * 1000 for _ in range(i)]
#         exec("func(ran_list)")
#     x.append(i)
#     y.append(operate_count / test_time)

for i in range(1, 101):
    operate_count = 0
    result = exec('func(i)')
    x.append(i)
    y.append(operate_count)

detect.detect_trend(np.array(x), np.array(y))
