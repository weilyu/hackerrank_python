# https://www.hackerrank.com/challenges/string-validators


def run(string):
    answer = [False, False, False, False, False]
    for letter in string:
        if letter.isalnum():
            answer[0] = True
        if letter.isalpha():
            answer[1] = True
        if letter.isdigit():
            answer[2] = True
        if letter.islower():
            answer[3] = True
        if letter.isupper():
            answer[4] = True
    return answer


raw_data = input()
my_answer = run(raw_data)
for a in my_answer:
    print(a)
