n = int(input())  # Number of lines
my_list = list()
for i in range(n):
    cur_input = input().split()
    if cur_input[0] == 'print':
        print(my_list)
    else:
        if cur_input[0] == 'insert':
            my_list.insert(int(cur_input[1]), int(cur_input[2]))
        elif cur_input[0] == 'remove':
            my_list.remove(int(cur_input[1]))
        elif cur_input[0] == 'append':
            my_list.append(int(cur_input[1]))
        elif cur_input[0] == 'sort':
            my_list.sort()
        elif cur_input[0] == 'pop':
            my_list.pop()
        elif cur_input[0] == 'reverse':
            my_list.reverse()
