for i in range(int(input())): #More than 4 lines will result in 0 score. Blank lines won't be counted. 
    a = int(input()); 
    A = set(input().split()) 
    b = int(input()); 
    B = set(input().split())
    flag = True
    for item in A:
        if item not in B:
            flag = False
            print(flag)
            break
    if flag:
        print('True')
