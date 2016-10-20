# https://www.hackerrank.com/challenges/python-mutations


first_line = input()
second_line = input().split()
l = list(first_line)
index = int(second_line[0])
new_char = second_line[1]
l[index] = new_char
l = ''.join(l)
print(l)
