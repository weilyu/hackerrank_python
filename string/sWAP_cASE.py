# https://www.hackerrank.com/challenges/swap-case


raw = input()
result = ''
for letter in raw:
    if letter.islower():
        result += letter.toupper()
    else:
        result += letter.tolower()
print(result)
