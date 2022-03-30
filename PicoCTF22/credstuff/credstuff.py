import pwn

with open("./leak/usernames.txt", "r") as file:
    users = [line.rstrip() for line in file]

with open("./leak/passwords.txt", "r") as file:
    passwords = [line.rstrip() for line in file]

pos = users.index("cultiris")
encrypted_pass = passwords[pos]

print(encrypted_pass)

for c in encrypted_pass:
    if not c == '{' and not c == '}':
        print(chr(ord(c)-13),end='')
    else:
        print(c,end='')
print()
