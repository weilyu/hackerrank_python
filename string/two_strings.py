def twoStrings(s1, s2):
    char_set = set()
    for c in s1:
        char_set.add(c)
    for c in s2:
        if c in char_set:
            return "YES"
    return "NO"
