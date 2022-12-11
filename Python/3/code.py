from typing import List


def min_digits_sum(arr: List[int]) -> int:
    res = ['0' , '0']
    arr = sorted(arr)
    switch = False
    k_null = arr.count(0)
    for i in range(k_null , len(arr)):
        temp = str(arr[i])
        if switch:
            res[1] += temp
            switch = False
        else:
            res[0] += temp
            switch = True
    return int(res[0]) + int(res[1])
