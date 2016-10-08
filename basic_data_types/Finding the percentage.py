# https://www.hackerrank.com/challenges/finding-the-percentage

n = int(input())
book = dict()
for i in range(n):
    curr = input().split()
    name = curr[0]
    avg_score = (float(curr[1]) + float(curr[2]) + float(curr[3])) / 3
    book[name] = avg_score
print("%.2f" % round(book[input()], 2))
