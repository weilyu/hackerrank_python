# https://www.hackerrank.com/challenges/py-set-add


num = int(input())
countries = set()
for i in range(num):
    countries.add(input().rstrip())
print(len(countries))
