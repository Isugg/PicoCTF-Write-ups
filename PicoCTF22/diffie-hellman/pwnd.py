key = "H98A9W_H6UM8W_6A_9_D6C_5ZCI9C8I_CB5EJHB6"

#Diffie-hellman calculator online, although because it relies on a FUCKING CAESAR CIPHER you could just brute force this one reeeeeeeee

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

print("picoCTF{",end='')

for c in key:
    if not c == '_':
        print(alpha[alpha.index(c)-5], end='')
    else:
        print(c,end='')

print("}")
