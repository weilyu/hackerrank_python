# https://www.hackerrank.com/challenges/find-a-string

raw_data = input()
string = input()
begin = 0
count = 0

while True:
    begin = raw_data.find(string, begin) + 1
    if begin == 0:
        break
    else:
        count += 1
print(count)
