# https://www.hackerrank.com/challenges/python-tuples
n = int(input())
data = input().split()
new_data = list()
for d in data:
    new_data.append(int(d))
my_tuple = tuple(new_data)

print(hash(my_tuple))
