# https://www.hackerrank.com/challenges/text-wrap

def wrap(para, n):
    if len(para) > n:
        print(para[:n])
        wrap(para[n:], n)
    else:
        print(para)


line = input()
num = int(input())
wrap(line, num)
