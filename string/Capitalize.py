# https://www.hackerrank.com/challenges/capitalize

line = input()
last_is_space = True
result = ''
for letter in line:
    if last_is_space and letter.islower:
        result += letter.upper()
    else:
        result += letter
    if letter == ' ':
        last_is_space = True
    else:
        last_is_space = False
print(result)
