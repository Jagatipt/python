def capitalize(s):
    i = ord(s[0])
    a = i - 32
    s = chr(a) + (s[1:])
    for i in range(1, len(s)):
        if s[i - 1] == ' ':
            s = s[:i] + chr(ord(s[i]) - 32) + s[i + 1:]
    return s

s = input()
print(capitalize(s))