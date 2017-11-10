#!/bin/python3

import sys


def sockMerchant(n, ar):
    # Complete this function
    stock = []
    count = 0
    for i in ar:
        if i in stock:
            stock.remove(i)
            count += 1
        else:
            stock.append(i)
    return count


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
