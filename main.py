import random
import numpy as np
import sys

import detect
import funcs

sys.setrecursionlimit(10 ** 7)

code = """
def func(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
"""

modified_code = funcs.modify_code(code)
print('--------------')
print(modified_code)
print('--------------')

exec(modified_code)

x = []
y = []

for i in range(200, 10200, 200):
    operate_count = 0
    test_time = 100
    for n in range(test_time):
        ran_list = [random.random() * 1000 for _ in range(i)]
        exec("func(ran_list)")
    x.append(i)
    y.append(operate_count / test_time)

detect.detect_trend(np.array(x), np.array(y))
