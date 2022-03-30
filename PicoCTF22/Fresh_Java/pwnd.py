text = open("freshJava.raw", 'r').read()

chars = text.split('!=')

flag = ""

for c in chars:
    try:
        c = c[c.index("'")+1]
        flag += c
    except Exception:
        c=""
print(flag[::-1])
