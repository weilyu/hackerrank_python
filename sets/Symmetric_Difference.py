# https://www.hackerrank.com/challenges/symmetric-difference


n1 = input()
line1 = input()
n2 = input()
line2 = input()

s1 = set(line1.split())
s2 = set(line2.split())

cm = set()
lst = list()

for s in s1:
    if s not in s2:
        lst.append(int(s))
for ss in s2:
    if ss not in s1:
        lst.append(int(ss))

lst.sort()
for i in lst:
    print(i)
