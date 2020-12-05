def f1(s):
    return s[::-1]

def f2(s):
    s1 = s[:int(len(s)/2)]
    s2 = s[int(len(s)/2):]
    o = ""
    for i in range(int(len(s)/2)):
        o += s1[i] + s2[i]
    return o

def f3(s):
    r = ''
    for c in s:
        r += chr(ord(c) ^ 0xf)
    return r

def f5(s):
    r = ''
    for c in s:
        r += chr(ord(c) - 1 if ord(c) != 32 else 126)
    return r

def f4(s):
    r = ''
    for c in s:
        r += chr(ord(c) + 1 if ord(c) != 126 else 32)
    return r

def f6(s):
    r = ''
    order = [10, 27, 28, 8, 5, 3, 12, 18, 22, 4, 23, 15, 20, 13, 29, 19, 2, 1, 21, 24, 26, 17, 11, 7, 25, 6, 14, 9, 16, 0]
    out = {}
    for i in range(30):
        out[order[i]] = s[i]
    for i in range(30):
        r += out[i]
    return r

def f7(s):
    return s.swapcase()

def f8(s):
    r = ''
    for c in s:
        if 'a'<=c<='z':
            r += chr((ord(c)-ord('a') + 13)%26 + ord('a'))
        else:
            r += c
    return r

def f9(s):
    r = ''
    for c in s:
        if 'A'<=c<='Z':
            r += chr((ord(c)-ord('A') + 13)%26 + ord('A'))
        else:
            r += c
    return r

def f10(s):
    return s[1:] + s[0]

print(f9(f1(f4(f10(f5(f4(f3(f8(f7(f3(f5(f2(f9(f2(f8(f5(f5(f8(f4(f10(f1(f2(f8(f2(f2(f2(f5(f3(f3(f7(f6(f2(f6(f5(f6(f8(f9(f2(f8(f6(f7(f6(f5(f5(f10(f7(f1(f2(f6(f6('XHFS%~p8#j:&ih<jim~NYFj5i!oEX%')))))))))))))))))))))))))))))))))))))))))))))))))))
