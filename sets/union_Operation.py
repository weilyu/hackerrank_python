# https://www.hackerrank.com/challenges/py-set-union


n1 = input()
l1 = input().split()
n2 = input()
l2 = input().split()

set1 = set(l1)
set2 = set(l2)

combine = set1.union(l2)
print(len(combine))
