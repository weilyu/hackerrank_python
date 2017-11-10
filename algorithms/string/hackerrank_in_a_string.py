#!/bin/python3

import sys


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    # your code goes here
    hackerrank = list('hackerrank')
    for c in list(s):
        if len(hackerrank) == 0:
            break
        if c == hackerrank[0]:
            hackerrank.remove(hackerrank[0])
    if len(hackerrank) > 0:
        print('NO')
    else:
        print('YES')
