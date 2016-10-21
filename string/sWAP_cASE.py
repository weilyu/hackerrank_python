line = input()
l = list(line)
for i in range(len(l)):
    if l[i].isupper():
        l[i] = l[i].lower()
    elif l[i].islower():
        l[i] = l[i].upper()
print(''.join(l))
