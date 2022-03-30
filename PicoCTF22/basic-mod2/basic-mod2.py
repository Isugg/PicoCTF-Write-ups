data_in = open("message.txt", "r")
decryption_string = "abcdefghijklmnopqrstuvwxyz0123456789_"
message = data_in.read()

nums = message.split()

flag = "picoCTF{"

for n in nums:
    n = int(n)
    result = n%41
    result = pow(result, -1, 41)
    flag += decryption_string[result-1]

print(flag+'}')
