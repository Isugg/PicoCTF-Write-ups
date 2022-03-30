msg = input('msg: ')#.replace(' ','')
N = int(input("rails: "))
L = len(msg)
multiple = 2*(N-1)

padding = multiple - (L % multiple)

for i in range(padding):
    msg+='A'

L = len(msg)
K=int(L/multiple)

for c in msg[0:K]:
    print(c, end='.....')
print()
lines = int((L/(2*K)) - 1)
for i in range(lines):
    string_length = 2*K
    string_pos = i * string_length
    print('.'*(i+1),end='')
    for c in msg[K+string_pos:K+string_pos+string_length]:
        print(c,end='.'*(i+2)*(lines-i))
    print()

print('...',end='')
for c in msg[-9:]:
    print(c, end='.....')
print()

#print(f"multiple:{multiple}")
#print(f"K:{K}")
#print(f"padding:{padding}")
#print(f"lines:{lines}")
